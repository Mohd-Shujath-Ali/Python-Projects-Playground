# PDF Merger Script

## Overview

This Python script merges multiple PDF files into a single consolidated document.  
It validates user input, ensures all specified files exist and are valid PDFs, and produces an output file named `merged-pdf.pdf`.

The tool is designed for simplicity, reliability, and clear error handling, making it suitable for both personal and professional use.

---

## Features

- Validates the total number of files before merging.
- Verifies that each file:
  - Exists in the current working directory.
  - Has a valid `.pdf` file extension.
- Handles invalid input and missing files gracefully.
- Produces a single merged PDF file named `merged-pdf.pdf`.

---

## Requirements

### Python Version
- **Python 3.7** or later

### Dependencies

The script requires **one external module**:

| Module  | Purpose                 | Installation Required |
|----------|-------------------------|------------------------|
| `PyPDF2` | PDF reading and writing | ✅ Yes                 |

---

### Standard Library Modules

| Module | Purpose | Used For |
|---------|----------|----------|
| `os` | Provides a way to interact with the operating system. | Used to check whether a file exists in the current working directory before attempting to merge it. |
| `sys` | Provides access to system-specific parameters and functions. | Used to safely terminate the program (`sys.exit()`) when invalid input or errors occur. |

These modules are part of Python’s **standard library** and do **not** require installation.

---

## Installation

Install the required dependency using `pip`:

```bash
pip install PyPDF2
