from report_generator_lib import add
from report_generator_lib import freecad_assistant_pdf_report

def main():
    num1 = 5
    num2 = 7
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

    # Create FreeCAD assistant PDF report
    freecad_assistant_pdf_report()

if __name__ == "__main__":
    main()
