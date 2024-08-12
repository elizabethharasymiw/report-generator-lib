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
    pdf.cell(200, 20, txt="Report", ln=True, align='L')

    # Title subtext
    pdf.set_font("Arial", style='', size=8.5)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(200, 5, txt="FreeCAD Beginner Assistant", ln=True, align='L')

    # FreeCAD Model Image
    pdf.image("./tests/test-images/freecad_model_test_file.png", x=10, y=30, w=200)

    # Save the PDF with name .pdf
    pdf.output("example.pdf")
