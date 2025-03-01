import PyPDF2

pdfiles = ['1sample.pdf', '2sample.pdf']
merger = PyPDF2.PdfMerger()
for file in pdfiles:
    pdfFile = open(file,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')    