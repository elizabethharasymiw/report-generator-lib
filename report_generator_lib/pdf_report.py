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
    id_col_width = all_equal_col_width * (1/4)
    id_col_neg_space = all_equal_col_width - id_col_width
    status_col_width = all_equal_col_width * (2/3)
    status_col_neg_space = all_equal_col_width - status_col_width
    total_neg_space = id_col_neg_space + status_col_neg_space
    custom_col_width_count = 2;

    # Text column variables
    equal_col_count = num_cols - custom_col_width_count
    text_col_width = all_equal_col_width + total_neg_space/equal_col_count

    cols = [
        ["ID          ","1","2","3","4","5","6","7"],
        ["What the user has done                              ","12", "22", "32", "42", "52", "62", "72"],
        ["What negative (and positive) effect that has", "13", "23", "33", "43", "53", "63", "73"],
        ["How to resolve the issue                            ", "14", "24", "34", "44", "54", "64", "74"],
        ["Status                           ", "Passed", "Passed", "Passed", "Passed", "Failed", "Failed", "Failed"]
    ]

    i = 0;
    j = 0;
    saved_x_loc = freecad_report_pdf.x
    saved_y_loc = freecad_report_pdf.y
    x_loc_add = 0;
    for col in cols:
        col_new_width = text_col_width
        freecad_report_pdf.y = saved_y_loc

        for item in col:

            # Define Text font based on row number
            if(i == 0): # Header
                freecad_report_pdf.set_fill_color(0, 0, 200)
                freecad_report_pdf.set_text_color(0, 0, 0)
                freecad_report_pdf.set_font("Arial", style='B', size=12)
            else: # Main Table
                freecad_report_pdf.set_font("Arial", size=12, style='')
                freecad_report_pdf.set_text_color(0, 0, 0)

            col_new_width = text_col_width
            if(j == 0):
                col_new_width = id_col_width
            if(j == 4):
                col_new_width = status_col_width

            # Set cursor back to top of table
            freecad_report_pdf.x = freecad_report_pdf.x - x_loc_add

            freecad_report_pdf.multi_cell(col_new_width, row_height, item, border=1, align='L')

            x_loc_add = col_new_width
            i = i + 1

        freecad_report_pdf.x = freecad_report_pdf.x + col_new_width
        i = 0
        j = j + 1

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
