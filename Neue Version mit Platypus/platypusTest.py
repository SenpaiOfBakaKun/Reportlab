from traceback import print_list
from reportlab.platypus import Paragraph, Frame,SimpleDocTemplate
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch,cm
from reportlab.lib.styles import getSampleStyleSheet

hoch, breit = (21*cm, 29.7*cm)
pdf = canvas.Canvas("platypusTest.pdf")

pdf.translate(cm,cm)

logo="logo.jpg"
pdf.drawImage(logo,breit-cm*3.5,hoch-cm*3,cm*2,cm*2)

pdf.setPageSize((breit, hoch))
flow_obj = []
graph1 = []
graph2 = []
graph3 = []
graph4 = []
tabelle1 = []
tabelle2 = []

styles = getSampleStyleSheet()

text = "this is text"

p_text= Paragraph(text,style=styles["Normal"])

text1 = Paragraph("Hier kommt ein Graph",style=styles["Normal"])

text2 = Paragraph("Hier kommt eine Legende",style=styles["Normal"])




frame1=Frame(0,cm*10,200,200,showBoundary=1)

frame2=Frame(300,cm*10,200,200,showBoundary=1)

frame3=Frame(600,cm*10,200,200,showBoundary=1)

frame4=Frame(0,cm*1,200,200,showBoundary=1)

frame5=Frame(300,cm,200,200,showBoundary=1)

frame6=Frame(600,cm,200,200,showBoundary=1)



def ueberschrift():
    pdf.setFont("Courier",16)
    pdf.drawCentredString(cm*13.85,hoch-cm*2,"Hier kommt die Überschrift")

ueberschrift()



flow_obj.append(p_text)
flow_obj.append(text1)
graph2.append(text1)
graph3.append(text1)
graph4.append(text1)
tabelle1.append(text2)
tabelle2.append(text2)


frame1.addFromList(flow_obj,pdf)
frame2.addFromList(graph2,pdf)
frame3.addFromList(graph3,pdf)
frame4.addFromList(graph4,pdf)
frame5.addFromList(tabelle1,pdf)
frame6.addFromList(tabelle2,pdf)




pdf.save()