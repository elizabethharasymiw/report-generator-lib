from fpdf import FPDF

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

# Takes in a formatted dict to generate a FreeCAD assistant PDF report.
# <Insert link to markdown that defined the dict format>
def freecad_assistant_pdf_report(freecad_report_dict):
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Title
    pdf.set_font("Arial", style='B', size=21)
    pdf.cell(200, 10, txt="Report", ln=True, align='L')

    # Title subtext
    pdf.set_font("Arial", style='', size=8.5)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(200, 5, txt="FreeCAD Beginner Assistant", ln=True, align='L')

    # FreeCAD Model Image
    pdf.image("./tests/test-images/freecad_model_test_file.png", x=10, y=20, w=200)

    # Points, Rank, Date, File
    pdf.ln(100)

    pdf.set_text_color(0, 0, 0)

    pdf.set_font("Arial", style='', size=13.5)
    pdf.cell(200, 8, txt="Points: 14 / 21", ln=True, align='L')
    pdf.cell(200, 8, txt="Rank: Bronze", ln=True, align='L')

    pdf.set_font("Arial", style='', size=8.5)
    pdf.cell(200, 6, txt="Date: 01.01.2024", ln=True, align='L')
    pdf.cell(200, 6, txt="File: test_file.FCStd", ln=True, align='L')

    # Save the PDF with name .pdf
    pdf.output("example.pdf")
