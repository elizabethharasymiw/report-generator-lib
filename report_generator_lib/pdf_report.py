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

    # Table
    pdf.ln(10)

    # Define the hardcoded dictionary
    data = {
        "Column 1": "Row 1, Data 1",
        "Column 1": "Row 2, Data 1",
        "Column 1": "Row 3, Data 1",
        "Column 1": "Row 4, Data 1",

        "Column 2": "Row 1, Data 2",
        "Column 2": "Row 2, Data 2",
        "Column 2": "Row 3, Data 2",
        "Column 2": "Row 4, Data 2",

        "Column 3": "Row 1, Data 3",
        "Column 3": "Row 2, Data 3",
        "Column 3": "Row 3, Data 3",
        "Column 3": "Row 4, Data 3",

        "Column 4": "Row 1, Data 4",
        "Column 4": "Row 2, Data 4",
        "Column 4": "Row 3, Data 4",
        "Column 4": "Row 4, Data 4",

        "Column 5": "Row 1, Data 5",
        "Column 5": "Row 2, Data 5",
        "Column 5": "Row 3, Data 5",
        "Column 5": "Row 4, Data 5"
    }

    # Define table header colors and set font
    pdf.set_fill_color(0, 0, 128)  # Dark blue
    pdf.set_text_color(255, 255, 255)  # White
    pdf.set_font("Arial", style='B', size=12)

    # Define column width and height
    col_width = pdf.w / 5.5  # Adjusting the column width
    row_height = 10

    # Add table header (using keys from the first item)
    headers = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"]
    for header in headers:
        pdf.cell(col_width, row_height, header, border=1, align='C', fill=True)
    pdf.ln(row_height)

    # Reset font and text color for table body
    pdf.set_font("Arial", size=12, style='')
    pdf.set_text_color(0, 0, 0)  # Black

    # Define the data for the table
    rows = [
        ["R 1, D 1", "R 1, D 2", "R 1, D 3", "R 1, D 4", "R 1, D 5"],
        ["R 2, D 1", "R 2, D 2", "R 2, D 3", "R 2, D 4", "R 2, D 5"],
        ["R 3, D 1", "R 3, D 2", "R 3, D 3", "R 3, D 4", "R 3, D 5"],
        ["R 4, D 1", "R 4, D 2", "R 4, D 3", "R 4, D 4", "R 4, D 5"]
    ]

    # Add table rows
    for row in rows:
        for item in row:
            pdf.cell(col_width, row_height, item, border=1, align='L')
        pdf.ln(row_height)

    # Add Owl mascot
    pdf.image("./tests/test-images/owl-2.png", x=10, y=240, w=20)

    # Footer Text
    pdf.ln(50)

    pdf.set_font("Arial", style='', size=8.5)

    # Define text with hyperlinks
    text1 = "This report was auto-generated with the "
    link_text1 = "FreeCAD Beginner Assistant"
    text2 = "."
    link1 = "https://github.com/alekssadowski95/FreeCAD-Beginner-Assistant/tree/main"

    # Add text with hyperlink for the first line
    pdf.write(6, text1)
    pdf.set_text_color(0, 0, 255)  # Blue color for the link text
    link1_id = pdf.add_link()
    pdf.write(6, link_text1, link1)
    pdf.set_text_color(0, 0, 0)  # Reset color to black
    pdf.write(6, text2)
    pdf.ln(6)

    pdf.cell(200, 6, txt="Do you like getting automatic feedback while working with FreeCAD? Help us improve the project.", ln=True, align='L')

    # Save the PDF with name .pdf
    pdf.output("example.pdf")
