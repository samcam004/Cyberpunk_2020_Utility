import pytesseract
from PIL import Image
import fitz
import os
from fpdf import FPDF

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path
)


def pdf_to_images(pdf_path):
    """Convert PDF pages to images."""
    pdf_document = fitz.open(pdf_path)
    images = []

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img_path = f"page_{page_num + 1}.png"
        pix.save(img_path)
        images.append(img_path)

    return images


def ocr_image(image_path):
    """Perform OCR on an image."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def ocr_pdf_to_text(pdf_path):
    """Perform OCR on a PDF file and return the extracted text."""
    images = pdf_to_images(pdf_path)
    full_text = ""

    for image_path in images:
        text = ocr_image(image_path)
        full_text += text + "\n"
        os.remove(image_path)  # Remove the image file after OCR is done

    return full_text


def text_to_pdf(text, output_pdf_path):
    """Create a PDF from the extracted text."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(output_pdf_path)


if __name__ == "__main__":
    pdf_path = input(
        "Enter path to your pdf file: "
    )  # Update with the path to your PDF file
    output_pdf_path = "ocr_output"  # Specify the output PDF file path

    text = ocr_pdf_to_text(pdf_path)
    text_to_pdf(text, output_pdf_path)

    print(f"OCR completed. The extracted text has been saved to {output_pdf_path}")
