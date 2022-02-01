import PyPDF2
pdffileobj=open('1.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()
file1=open(r"C:\\wunschordner\\pdf_zeug\\1.txt","a")
file1.writelines(text)
file1.close()

# ort an dem der textinhalt des pdf gespeichert werden soll. 