# PDF Merger

## Overview
This script merges multiple PDF files into a single PDF file using the `PyPDF2` library.

## Prerequisites
Ensure you have Python installed along with the `PyPDF2` library. You can install it using:

```bash
pip install pypdf2
```

## How It Works
1. The script defines a list of PDF files to merge.
2. It initializes a `PdfMerger` object.
3. Each PDF file is opened, read, and appended to the merger.
4. Finally, the merged PDF is written to a new file named `merged.pdf`.

## Usage
1. Place the PDF files in the same directory as the script.
2. Update the `pdfiles` list with the correct filenames.
3. Run the script using:

```bash
python script.py
```

