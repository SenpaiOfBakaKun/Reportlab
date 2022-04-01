from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas


styleSheet = getSampleStyleSheet()
style = styleSheet['BodyText']
P=Paragraph('This is a very silly example',style)
canv = Canvas('doc.pdf')
aW = 460 # available width and height
aH = 800
w,h = P.wrap(aW, aH) # find required space
if w<=aW and h<=aH:
    P.drawOn(canv,0,aH)
    aH = aH-h
    canv.save()
else:
    raise ValueError
