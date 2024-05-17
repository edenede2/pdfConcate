import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

def concatenate_pdfs(pdf_files):
    pdf_writer = PdfWriter()

    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    output = io.BytesIO()
    pdf_writer.write(output)
    output.seek(0)
    return output

st.title("PDF Concatenator")

st.write("This app concatenates multiple PDF files into a single PDF file.")

new_file_name = st.text_input("Enter a title for the concatenated PDF file", "concatenated.pdf")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if st.button("Concatenate PDFs") and uploaded_files:
    concatenated_pdf = concatenate_pdfs(uploaded_files)
    st.success("PDF files concatenated successfully!")
    st.download_button(
        label="Download Concatenated PDF",
        data=concatenated_pdf,
        file_name=new_file_name,
        mime="application/pdf"
    )