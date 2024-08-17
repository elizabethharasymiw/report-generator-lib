from fpdf import FPDF

def freecad_assistant_pdf_report_header(freecad_report_pdf):
    # Title Main Text
    freecad_report_pdf.set_font("Arial", style='B', size=21)
    freecad_report_pdf.cell(200, 10, txt="Report", ln=True, align='L')
    # Title subtext
    freecad_report_pdf.set_font("Arial", style='', size=8.5)
    freecad_report_pdf.set_text_color(128, 128, 128)
    freecad_report_pdf.cell(200, 5, txt="FreeCAD Beginner Assistant", ln=True, align='L')
    return freecad_report_pdf

def freecad_assistant_pdf_report_summary_text(freecad_report_pdf):
    freecad_report_pdf.set_text_color(0, 0, 0)
    freecad_report_pdf.set_font("Arial", style='', size=13.5)
    freecad_report_pdf.cell(200, 8, txt="Points: 14 / 21", ln=True, align='L')
    freecad_report_pdf.cell(200, 8, txt="Rank: Bronze", ln=True, align='L')
    freecad_report_pdf.set_font("Arial", style='', size=8.5)
    freecad_report_pdf.cell(200, 6, txt="Date: 01.01.2024", ln=True, align='L')
    freecad_report_pdf.cell(200, 6, txt="File: test_file.FCStd", ln=True, align='L')
    return freecad_report_pdf

def freecad_assistant_pdf_report_table(freecad_report_pdf):
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
    freecad_report_pdf.set_fill_color(0, 0, 128)  # Dark blue
    freecad_report_pdf.set_text_color(255, 255, 255)  # White
    freecad_report_pdf.set_font("Arial", style='B', size=12)

    # Define column width and height
    num_cols = 5;
    col_width = freecad_report_pdf.w / ( num_cols + .5)
    id_col_width = col_width / 4
    status_col_width = col_width / 2
    text_col_width = col_width + (id_col_width/2) + (status_col_width/2)
    row_height = 10

    # Add table header (using keys from the first item)
    headers = ["ID", "Text 1", "Text 2", "Text 3", "Status"]
    for header in headers:
        col_new_width = text_col_width
        if(header == "ID"):
            col_new_width = id_col_width
        if(header == "Status"):
            col_new_width = status_col_width
        freecad_report_pdf.cell(col_new_width, row_height, header, border=1, align='C', fill=True)
    freecad_report_pdf.ln(row_height)

    # Reset font and text color for table body
    freecad_report_pdf.set_font("Arial", size=12, style='')
    freecad_report_pdf.set_text_color(0, 0, 0)  # Black

    # Define the data for the table
    rows = [
        ["1", "R 1, D 2", "R 1, D 3", "R 1, D 4", "R 1, D 5"],
        ["2", "R 2, D 2", "R 2, D 3", "R 2, D 4", "R 2, D 5"],
        ["3", "R 3, D 2", "R 3, D 3", "R 3, D 4", "R 3, D 5"],
        ["4", "R 4, D 2", "R 4, D 3", "R 4, D 4", "R 4, D 5"]
    ]

    # Add table rows
    i = 0;
    for row in rows:
        for item in row:
            col_new_width = text_col_width
            if(i == 0):
                col_new_width = id_col_width
            if(i == 4):
                col_new_width = status_col_width
            freecad_report_pdf.cell(col_new_width, row_height, item, border=1, align='L')
            i = i + 1;
        freecad_report_pdf.ln(row_height)
        i = 0
    return freecad_report_pdf

def freecad_assistant_pdf_report_footer(freecad_report_pdf):
    # Add Owl mascot
    freecad_report_pdf.image("./tests/test-images/owl-2.png", x=10, y=240, w=20)

    # Add Space
    freecad_report_pdf.ln(50)

    freecad_report_pdf.set_font("Arial", style='', size=8.5)

    # Define text with hyperlinks
    text1 = "This report was auto-generated with the "
    link_text1 = "FreeCAD Beginner Assistant"
    text2 = "."
    link1 = "https://github.com/alekssadowski95/FreeCAD-Beginner-Assistant/tree/main"

    # Add text with hyperlink for the first line
    freecad_report_pdf.write(6, text1)
    freecad_report_pdf.set_text_color(0, 0, 255)  # Blue color for the link text
    link1_id = freecad_report_pdf.add_link()
    freecad_report_pdf.write(6, link_text1, link1)
    freecad_report_pdf.set_text_color(0, 0, 0)  # Reset color to black
    freecad_report_pdf.write(6, text2)
    freecad_report_pdf.ln(6)

    freecad_report_pdf.cell(200, 6, txt="Do you like getting automatic feedback while working with FreeCAD? Help us improve the project.", ln=True, align='L')

    return freecad_report_pdf

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

    # Add Report Header
    pdf = freecad_assistant_pdf_report_header(pdf)

    # FreeCAD Model Image
    pdf.image("./tests/test-images/freecad_model_test_file.png", x=10, y=20, w=200)

    # Add Space
    pdf.ln(100)

    # Points, Rank, Date, File
    pdf = freecad_assistant_pdf_report_summary_text(pdf)

    # Table
    pdf = freecad_assistant_pdf_report_table(pdf)

    # Add Space
    pdf.ln(10)

    # Footer Text
    pdf = freecad_assistant_pdf_report_footer(pdf)

    # Save the PDF with name .pdf
    pdf.output("example.pdf")
