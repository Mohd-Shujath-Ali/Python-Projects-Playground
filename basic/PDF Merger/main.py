from PyPDF2 import PdfWriter
import os
import sys

merger = PdfWriter()

# Step 1: We ask the user for total number of PDFs he/she wants to merge
try:
    total = int(input("Enter total number of PDF files to merge: "))
    if total <= 1:
        print("Please enter a number greater than 1.")
        sys.exit()
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    sys.exit()

# Step 2: store file names from the user into an empty List
pdf_files = []
for i in range(total):
    file_name = input(f"Enter the name of PDF file {i+1}: ")
    pdf_files.append(file_name.strip())

# Step 3: Check if all files exist and are valid PDFs
for pdf in pdf_files:
    if not pdf.lower().endswith('.pdf'):
        print(f"Error: '{pdf}' is not a PDF file (missing .pdf extension).")
        sys.exit()
    if not os.path.isfile(pdf):
        print(f"Error: File '{pdf}' not found in the current directory.")
        sys.exit()

# Step 4: Merge PDFs
try:
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()
    print("\nPDF files merged successfully into 'merged-pdf.pdf'.")
except Exception as e:
    print(f"An error occurred while merging: {e}")
    sys.exit()
