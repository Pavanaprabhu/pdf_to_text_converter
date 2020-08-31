"""open pdf file
generate interpreter
for each page->interpret it to text n save it
create  a txt file with saved data"""

from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

pdfpath='Downloads\\1pe17cs032_finalresume.pdf'
pdf=open(pdfpath,'rb')

mem=io.StringIO()


rm=PDFResourceManager()
lp=LAParams()
cnv=TextConverter(rm,mem,laparams=lp)
ip=PDFPageInterpreter(rm,cnv)

for i in PDFPage.get_pages(pdf):
	ip.process_page(i)
	text=mem.getvalue()

file=open("Downloads\\1pe17cs032_finalresume.txt",'wb')
file.write(text.encode('utf-8'))
print("done")