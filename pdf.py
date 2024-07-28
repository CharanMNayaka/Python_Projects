import PyPDF2

pdf_file = ["1.pdf", "2.pdf"]

merge = PyPDF2.PdfMerger()

for pdf in pdf_file:
    pdfs = open(pdf, 'rb')
    pdfreader = PyPDF2.PdfReader(pdfs)
    merge.append(pdfreader)

merge.write('output.pdf')