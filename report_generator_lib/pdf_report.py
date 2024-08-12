from fpdf import FPDF

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def freecad_assistant_pdf_report():
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set Title font
    pdf.set_font("Arial", style='B', size=32)

    # Add a cell
    pdf.cell(200, 10, txt="Welcome to FPDF!", ln=True, align='C')

    # Save the PDF with name .pdf
    pdf.output("example.pdf")
