from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Отчет по оборудованию', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Страница {self.page_no()}', 0, 0, 'C')

def generate_pdf_report(equipment_data):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    for equipment in equipment_data:
        pdf.cell(0, 10, f"{equipment['name']} - {equipment['type']} - {equipment['location']}", 0, 1)

    pdf.output('equipment_report.pdf')
