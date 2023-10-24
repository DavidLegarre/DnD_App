from pdfquery import PDFQuery


def parse_pdf(filepath: str):
    # read the PDF
    pdf = PDFQuery(filepath)
    pdf.load()

    # convert the pdf to XML
    pdf.tree.write('customers.xml', pretty_print=True)

