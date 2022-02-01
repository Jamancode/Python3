import sys
import os
import comtypes.client

def word_to_pfd(_in, _out):
	pdf_format_key = 17
	file_in = os.path.abspath(_in)
	file_out = os.path.abspath(_out)
	worddoc = comtypes.client.CreateObject( 'Word.Application')
	doc = worddoc.Documents.Open(flie_in)
	doc.SaveAs(file_out, FlieForat = pdf_format_key)
	doc.close()
	worddoc.Quit()

	wunsch = sys.argv[1]
	for file in os.listdir(wunsch):
		word_to_pdf(wunsch + "\\" + file, wunsch + "\\" + file + ".pdf")


# zum ausführen cmd öffnen und befehl eingeben.
#>>> C:\Users\Dein_PC\Desktop\Word>python word_to_pdf.py "C:\Users\MeinPC\Desktop\Word"
#hier ist "word_to_pdf.py" die datei und der zu suchende ordner um die zu finden. Leerzeichen und der Phat wo das erzeugte PDF abgelegt werden soll.