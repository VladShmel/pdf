from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for i in range(210):
    pdf.add_page()

pdf.output("output.pdf")