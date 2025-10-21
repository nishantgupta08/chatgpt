#!/usr/bin/env python3
"""
extract_pdf_to_confluence_json.py

Extract text, tables and images from a PDF and produce a Confluence-like JSON payload.

Outputs:
- /mnt/data/extracted_page_html.json
- extracted images -> /mnt/data/extracted_images/
"""

import os
import json
import traceback
from pathlib import Path

# ---------- CONFIG ----------
PDF_PATH = "/mnt/data/Optimus Recommendation Rejection_105ba7c854034b278806e34c248a0d88-191025-2240-1706.pdf"
OUT_DIR = Path("/mnt/data/extracted_images")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = Path("/mnt/data/extracted_page_html.json")
# ----------------------------

def try_import(name):
    try:
        return __import__(name)
    except Exception:
        return None

pdfplumber = try_import("pdfplumber")
fitz = try_import("fitz")      # PyMuPDF
PyPDF2 = try_import("PyPDF2")

extracted_text = []
tables_html = []
image_filenames = []

# 1) Extract text and tables with pdfplumber if available
if pdfplumber:
    try:
        import pdfplumber
        with pdfplumber.open(PDF_PATH) as pdf:
            for i, page in enumerate(pdf.pages):
                txt = page.extract_text() or ""
                extracted_text.append({"page": i+1, "text": txt})
                # table extraction
                try:
                    tbls = page.extract_tables()
                except Exception:
                    tbls = []
                for t_idx, tbl in enumerate(tbls):
                    if not tbl:
                        continue
                    header = tbl[0]
                    body = tbl[1:] if len(tbl) > 1 else []
                    html = '<table class="confluenceTable"><thead><tr>'
                    for cell in header:
                        html += f"<th>{(cell or '').strip()}</th>"
                    html += "</tr></thead><tbody>"
                    for row in body:
                        html += "<tr>"
                        for cell in row:
                            html += f"<td>{(cell or '').strip()}</td>"
                        html += "</tr>"
                    html += "</tbody></table>"
                    tables_html.append({"page": i+1, "table_index": t_idx, "html": html})
    except Exception:
        traceback.print_exc()
else:
    # fallback to PyPDF2 for text
    if PyPDF2:
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(PDF_PATH)
            for i, page in enumerate(reader.pages):
                try:
                    txt = page.extract_text() or ""
                except Exception:
                    txt = ""
                extracted_text.append({"page": i+1, "text": txt})
        except Exception:
            traceback.print_exc()
    else:
        extracted_text.append({"page": 1, "text": ""})

# 2) Extract images using fitz (PyMuPDF) if available
if fitz:
    try:
        import fitz
        doc = fitz.open(PDF_PATH)
        for page_index in range(len(doc)):
            page = doc[page_index]
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                ext = base_image.get("ext", "png")
                fname = OUT_DIR / f"page{page_index+1}_img{img_index+1}.{ext}"
                with open(fname, "wb") as f:
                    f.write(image_bytes)
                image_filenames.append(str(fname))
    except Exception:
        traceback.print_exc()

# 3) If no extracted images and pdfplumber can only provide bbox info, create placeholders
if not image_filenames and pdfplumber:
    try:
        import pdfplumber
        with pdfplumber.open(PDF_PATH) as pdf:
            for i, page in enumerate(pdf.pages):
                imgs = page.images or []
                for j, im in enumerate(imgs):
                    fname = OUT_DIR / f"page{i+1}_image{j+1}_bbox.txt"
                    with open(fname, "w") as f:
                        f.write(json.dumps(im))
                    image_filenames.append(str(fname))
    except Exception:
        traceback.print_exc()

# 4) Build the Confluence-like storage HTML
title = Path(PDF_PATH).stem
html_parts = []
html_parts.append(f"<h1>{title}</h1>")

for p in extracted_text:
    page_num = p["page"]
    text = (p["text"] or "").strip()
    if text:
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        if lines:
            html_parts.append(f"<h2>Page {page_num} text</h2>")
            # limit number of lines to avoid huge output; adjust as needed
            for ln in lines[:500]:
                # Escape or sanitize if necessary (here we simply insert)
                html_parts.append(f"<p>{ln}</p>")

# add tables
if tables_html:
    for t in tables_html:
        html_parts.append(f"<h3>Table (page {t['page']})</h3>")
        html_parts.append(t["html"])

# add extracted images as <ac:image> references (filename used as attachment name)
for fname in image_filenames:
    basename = os.path.basename(fname)
    html_parts.append("<p>Extracted image:</p>")
    html_parts.append(f'<ac:image><ri:attachment ri:filename="{basename}" /></ac:image>')

storage_value = "\n".join(html_parts)

# 5) Metadata counts (pdf_export style)
metadata = {
    "pdf_export": {
        "original_filename": os.path.basename(PDF_PATH),
        "pages_in_pdf": len(extracted_text) if extracted_text else None,
        "tables_detected": len(tables_html),
        "visual_elements": {
            "images": len(image_filenames),
            "diagrams": 0,
            "charts": 0,
            "total_pages": len(extracted_text) if extracted_text else None
        },
        "has_visuals": len(image_filenames) > 0
    }
}

payload = {
    "type": "page",
    "title": title,
    "space": {"key": "LOCAL"},
    "body": {
        "storage": {
            "value": storage_value,
            "representation": "storage"
        }
    },
    "metadata": metadata,
    "attachments": [{"filename": os.path.basename(p), "path": p} for p in image_filenames]
}

# 6) Save JSON
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print("Extraction complete.")
print("JSON saved to:", OUT_JSON)
print("Extracted images count:", len(image_filenames))
if image_filenames:
    print("First few images:", image_filenames[:5])
