from fpdf import FPDF

def main():
    year = 2016

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_top_margin(15)
    # Page 1
    pdf.add_page()
    pdf.set_font("times", size=40, style='B')
    pdf.set_y(60)
    pdf.multi_cell(200, 10, txt=f"Maven Pizzas\n\nReport {year}", align="C")
    pdf.set_font("times", size=20, style='B')
    pdf.set_y(115)
    pdf.cell(200, 10, txt="Author: Alejandro Martínez de Guinea", ln=1, align="C")
    pdf.image('IMAGES/pizza.jpg', x=10, y=150, w=190, h=105)

    # Page 2
    pdf.add_page()
    pdf.set_font("times", size=15)
    pdf.cell(200, 10, txt="Ingredients predicted", ln=1)
    pdf.image(f'IMAGES/ingredients_{year}.png', x=10, y=30, w=190, h=125)

    pdf.output(f"data_report_{year}.pdf")
