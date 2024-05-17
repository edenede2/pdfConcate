from pypdf import PdfReader, PdfWriter

# Paths to the PDF files
pdf1_path = '/Users/edeneldar/Library/Mobile Documents/com~apple~CloudDocs/Maman1.pdf'
pdf2_path = '/Users/edeneldar/Library/Mobile Documents/com~apple~CloudDocs/Maman2.pdf'
pdf3_path = '/Users/edeneldar/Library/Mobile Documents/com~apple~CloudDocs/Maman3.pdf'
output_path = '/Users/edeneldar/Library/Mobile Documents/com~apple~CloudDocs/Maman.pdf'

# Create PdfReader objects for each PDF file
pdf1_reader = PdfReader(pdf1_path)
pdf2_reader = PdfReader(pdf2_path)
pdf3_reader = PdfReader(pdf3_path)

# Create a PdfWriter object
pdf_writer = PdfWriter()

# Add pages from the first PDF
for page_num in range(len(pdf1_reader.pages)):
    pdf_writer.add_page(pdf1_reader.pages[page_num])

# Add pages from the second PDF
for page_num in range(len(pdf2_reader.pages)):
    pdf_writer.add_page(pdf2_reader.pages[page_num])

# Add pages from the third PDF
for page_num in range(len(pdf3_reader.pages)):
    pdf_writer.add_page(pdf3_reader.pages[page_num])

# Write the combined PDF to a file
with open(output_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print(f"PDF files have been concatenated and saved as {output_path}")
