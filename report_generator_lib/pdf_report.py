# 1 inch = 25.4 mm
ONE_INCH_MARGIN_SIZE = 25.4

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
    table_width = freecad_report_pdf.w - (2 * ONE_INCH_MARGIN_SIZE)
    num_cols = 5;
    row_height = 10
    all_equal_col_width = table_width / num_cols

    # Custom column variables
    id_col_width = all_equal_col_width * (1/3)
    id_col_neg_space = all_equal_col_width - id_col_width
    status_col_width = all_equal_col_width * (2/3)
    status_col_neg_space = all_equal_col_width - status_col_width
    total_neg_space = id_col_neg_space + status_col_neg_space
    custom_col_width_count = 2;

    # Text column variables
    equal_col_count = num_cols - custom_col_width_count
    text_col_width = all_equal_col_width + total_neg_space/equal_col_count

    TABLE_DATA = (
        ( # Row 1, Header
            "ID",
            "What the user has done",
            "What negative (and positive) effect that has",
            "How to resolve the issue",
            "Status"
        ),
        ("1", "12", "22", "32", "Passed"),
        ("2", "13", "23", "33", "Passed"),
        ("3", "14", "24", "34", "Passed"),
        ("4", "15", "25", "35", "Passed"),
        ("5", "16", "26", "36", "Passed"),
    )
    freecad_report_pdf.set_font("Times", size=16)
    with freecad_report_pdf.table(width=table_width, col_widths=(id_col_width, text_col_width, text_col_width, text_col_width, status_col_width)) as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    return freecad_report_pdf

def freecad_assistant_pdf_report_footer(freecad_report_pdf):
    # Add Owl mascot
    freecad_report_pdf.image("./tests/test-images/owl-2.png", x=ONE_INCH_MARGIN_SIZE, y=freecad_report_pdf.y, w=20)

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

    # Set 1 inch page margins
    pdf.set_left_margin(ONE_INCH_MARGIN_SIZE)
    pdf.set_right_margin(ONE_INCH_MARGIN_SIZE)
    pdf.set_top_margin(ONE_INCH_MARGIN_SIZE)
    pdf.set_auto_page_break(auto=True, margin=ONE_INCH_MARGIN_SIZE)

    # Add a page
    pdf.add_page()

    # Add Report Header
    pdf = freecad_assistant_pdf_report_header(pdf)

    # Add Space
    pdf.ln(10)

    # FreeCAD Model Image
    pdf.image("./tests/test-images/freecad_model_test_file.png", x=ONE_INCH_MARGIN_SIZE, y=pdf.y, w=(pdf.w - (2 * ONE_INCH_MARGIN_SIZE)))

    # Add Space
    pdf.ln(90)

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
