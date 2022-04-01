from reportlab.pdfgen import canvas 

from reportlab.lib.units import cm 
from reportlab.lib import colors 

breit = 1024
hoch= 700


pdf = canvas.Canvas("template1.pdf")
pdf.translate(cm,cm)
pdf.setPageSize((1024,700))

def achse():
    pdf.line(0,0,0,600) #y-Achse
    pdf.line(0,0,1000,0)









pdf.save()

