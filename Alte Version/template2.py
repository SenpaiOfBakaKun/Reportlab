from textwrap import fill
from tkinter import font
from reportlab.pdfgen import canvas 
from reportlab.lib.units import cm, inch 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import letter,A4
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, String
from reportlab.graphics.charts.lineplots import SimpleTimeSeriesPlot
from reportlab.lib.colors import PCMYKColor



#A8 5,2 cm x 7,4 cm
#A7 7,4 cm x 10,5 cm
#A6 10,5 cm x 14,8 cm
#A5 14,8 cm x 21,0 cm
#A4 21,0 cm * 29,7 cm
#A3 29,7 cm x 42,0 cm
#A2 42,0 cm x 59,4 cm
#A1 59,4 cm x 84,1 cm
#A0 84,1 cm x 118,9 cm


hoch, breit = (21*cm, 29.7*cm)

logo = 'logo.jpg'


pdf = canvas.Canvas("template2.pdf")

#color
red = PCMYKColor(0,100,100,0)
black = PCMYKColor(0,0,0,100)
blue = PCMYKColor(100,100,0,0)
green = PCMYKColor(100,0,90,50,100)

blueTransparent = PCMYKColor(0.507, 0.256, 0, 0.235,alpha=0.5)


pdf.translate(cm,cm)

pdf.setPageSize((breit,hoch))

def deko():
    pdf.setFillColorCMYK = blueTransparent
    pdf.rect(0-cm,hoch-cm*3,breit,hoch,stroke=0,fill=1)
    

def achse():
    pdf.line(0,0,0,600) #y-Achse
    pdf.line(0,0,1000,0)

def rand():
    pdf.line(0,0,0,hoch-cm*2)
    pdf.line(0,0,breit-cm*2,0)

    pdf.line(0,hoch-cm*2,breit-cm*2,hoch-cm*2)
    pdf.line(breit-cm*2,0,breit-cm*2,hoch-cm*2)

def fonts():
    for font in pdf.getAvailableFonts():
        print(font)
'''
Courier
Courier-Bold
Courier-BoldOblique
Courier-Oblique
Helvetica
Helvetica-Bold
Helvetica-BoldOblique
Helvetica-Oblique
Symbol
Times-Bold
Times-BoldItalic
Times-Italic
Times-Roman
ZapfDingbats
'''
def ueberschrift():
    pdf.setFont("Courier",16)
    pdf.drawCentredString(cm*13.85,hoch-cm*2,"Streckenvergleich")

def teil(teil):
    pdf.setFont("Courier-Bold",12)
    pdf.drawCentredString(cm*13.85,hoch-cm*2.5,teil)

def graphBorder1():
    pdf.rect(0,cm*10,200,200,fill=0)

def graphBorder2():
    pdf.rect(300,cm*10,200,200,fill=0)

def graphBorder3():
    pdf.rect(600,cm*10,200,200,fill=0)

def graphBorder4():
    pdf.rect(0,cm*1,200,200,fill=0)

def seitenZahl():
    pdf.setFont("Times-Roman",12)
    pdf.drawCentredString(14.85*cm,0,"1")

###########################################################


#fonts()
#rand()
#graphBorder1()
#graphBorder2()
#graphBorder3()
#graphBorder4()
deko()
ueberschrift()
teil("EZMLR1")
seitenZahl()
pdf.drawInlineImage(logo,breit-cm*3.5,hoch-cm*3,cm*2,cm*2)





class chart(_DrawingEditorMixin,Drawing):
    
    def __init__(self,width=200,height=200,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        self.add
        self._add(self,SimpleTimeSeriesPlot(),name='chart',validate=None,desc=None)
        self.chart.x = 30
        self.chart.y = 30
        self.chart.height = 150
        self.chart.yValueAxis.forceZero = 0
        self._add(self,String(10,10,'text'),name='title',validate=None,desc=None)
        self.title.text = 'Graph1'
        self.title.fontSize = 16
        self.chart.lines[0].strokeColor = red
        self.chart.lines.strokeWidth = 2
        self.chart.xValueAxis.xLabelFormat            = '{dd}/{mm}/{YY}'
        self.chart.data = [[('20220101', 0), ('20221231', 114)]]

        self.chart.xValueAxis.niceMonth = 1
        self.chart.width           = 200
        self.title.y          = 160
        self.title.x          = 115

class chart2(_DrawingEditorMixin,Drawing):
    
    def __init__(self,width=200,height=200,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        self.add
        self._add(self,SimpleTimeSeriesPlot(),name='chart',validate=None,desc=None)
        self.chart.x                = 30
        self.chart.y                = 30
        self.chart.height           = 150
        self.chart.yValueAxis.forceZero               = 0
        self._add(self,String(10,10,'text'),name='title',validate=None,desc=None)
        self.title.text       = 'Graph2'
        self.title.fontSize   = 16
        self.chart.lines[0].strokeColor = blue
        self.chart.lines.strokeWidth = 2
        self.chart.xValueAxis.xLabelFormat            = '{dd}/{mm}/{YY}'
        self.chart.data = [[('20220101', 0),('20220201',10),('20220301',10),('20220401',10),('20220501',10), ('20220601',10),('20220701',10),('20220801',10),('20220901',10),('20221001',10),('20221101',10),('20221201', 114)]]

        self.chart.xValueAxis.niceMonth               = 1
        self.chart.width           = 200
        self.title.y          = 160
        self.title.x          = 115


class chart3(_DrawingEditorMixin,Drawing):
    
    def __init__(self,width=200,height=200,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        self.add
        self._add(self,SimpleTimeSeriesPlot(),name='chart',validate=None,desc=None)
        self.chart.x                = 30
        self.chart.y                = 30
        self.chart.height           = 150
        self.chart.yValueAxis.forceZero               = 0
        self._add(self,String(10,10,'text'),name='title',validate=None,desc=None)
        self.title.text       = 'Graph3'
        self.title.fontSize   = 16
        self.chart.lines[0].strokeColor = green
        self.chart.lines.strokeWidth     = 2
        #self.chart.lines[1].strokeColor = PCMYKColor(0,100,100,40,alpha=100)
        self.chart.xValueAxis.xLabelFormat            = '{dd}/{mm}/{YY}'
        self.chart.data = [[('20220101', 0), ('20221231', 114)]]

        self.chart.xValueAxis.niceMonth               = 1
        self.chart.width           = 200
        self.title.y          = 160
        self.title.x          = 115

##############


class chart4(_DrawingEditorMixin,Drawing):
    
    def __init__(self,width=200,height=200,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        self.add
        self._add(self,SimpleTimeSeriesPlot(),name='chart',validate=None,desc=None)
        self.chart.x                = 30
        self.chart.y                = 30
        self.chart.height           = 150
        self.chart.yValueAxis.forceZero               = 0
        self._add(self,String(10,10,'text'),name='title',validate=None,desc=None)
        self.title.text       = 'Graph4'
        self.title.fontSize   = 16
        self.chart.lines[0].strokeColor = black
        self.chart.lines.strokeWidth = 2
        self.chart.xValueAxis.xLabelFormat            = '{dd}/{mm}/{YY}'
        self.chart.data = [[('20120101', 100), ('20120102', 100), ('20120103', 101), ('20120104', 101), ('20120105', 102), ('20120106', 101), ('20120107', 101), ('20120108', 101), ('20120109', 102), ('20120110', 103), ('20120111', 103), ('20120112', 104), ('20120113', 103), ('20120114', 103), ('20120115', 103), ('20120116', 103), ('20120117', 103), ('20120118', 105), ('20120119', 106), ('20120120', 106), ('20120121', 106), ('20120122', 106), ('20120123', 106), ('20120124', 107), ('20120125', 108), ('20120126', 107), ('20120127', 107), ('20120128', 107), ('20120129', 107), ('20120130', 107), ('20120131', 107), ('20120201', 109), ('20120202', 109), ('20120203', 111), ('20120204', 111), ('20120205', 111), ('20120206', 111), ('20120207', 111), ('20120208', 111), ('20120209', 110), ('20120210', 109), ('20120211', 109), ('20120212', 109), ('20120213', 110), ('20120214', 110), ('20120215', 109), ('20120216', 111), ('20120217', 111), ('20120218', 111), ('20120219', 111), ('20120220', 111), ('20120221', 111), ('20120222', 111), ('20120223', 112), ('20120224', 111), ('20120225', 111), ('20120226', 111), ('20120227', 111), ('20120228', 111), ('20120229', 110), ('20120301', 111), ('20120302', 109), ('20120303', 109), ('20120304', 109), ('20120305', 109), ('20120306', 106), ('20120307', 108), ('20120308', 109), ('20120309', 111), ('20120310', 111), ('20120311', 111), ('20120312', 110), ('20120313', 113), ('20120314', 112), ('20120315', 113), ('20120316', 112), ('20120317', 112), ('20120318', 112), ('20120319', 113), ('20120320', 112), ('20120321', 112), ('20120322', 110), ('20120323', 111), ('20120324', 111), ('20120325', 111), ('20120326', 113), ('20120327', 113), ('20120328', 112), ('20120329', 112), ('20120330', 112), ('20120331', 112), ('20120401', 112), ('20120402', 113), ('20120403', 112), ('20120404', 110), ('20120405', 110), ('20120406', 110), ('20120407', 110), ('20120408', 110), ('20120409', 108), ('20120410', 106), ('20120411', 107), ('20120412', 109), ('20120413', 107), ('20120414', 107), ('20120415', 107), ('20120416', 107), ('20120417', 109), ('20120418', 108), ('20120419', 108), ('20120420', 108), ('20120421', 108), ('20120422', 108), ('20120423', 106), ('20120424', 107), ('20120425', 109), ('20120426', 110), ('20120427', 111), ('20120428', 111), ('20120429', 111), ('20120430', 110), ('20120501', 110), ('20120502', 110), ('20120503', 108), ('20120504', 106), ('20120505', 106), ('20120506', 106), ('20120507', 106), ('20120508', 106), ('20120509', 105), ('20120510', 106), ('20120511', 105), ('20120512', 105), ('20120513', 105), ('20120514', 104), ('20120515', 103), ('20120516', 103), ('20120517', 101), ('20120518', 100), ('20120519', 100), ('20120520', 100), ('20120521', 102), ('20120522', 102), ('20120523', 102), ('20120524', 102), ('20120525', 102), ('20120526', 102), ('20120527', 102), ('20120528', 102), ('20120529', 104), ('20120530', 102), ('20120531', 101), ('20120601', 98), ('20120602', 98), ('20120603', 98), ('20120604', 98), ('20120605', 99), ('20120606', 102), ('20120607', 101), ('20120608', 102), ('20120609', 102), ('20120610', 102), ('20120611', 100), ('20120612', 101), ('20120613', 99), ('20120614', 100), ('20120615', 101), ('20120616', 101), ('20120617', 101), ('20120618', 102), ('20120619', 103), ('20120620', 103), ('20120621', 100), ('20120622', 101), ('20120623', 101), ('20120624', 101), ('20120625', 99), ('20120626', 99), ('20120627', 100), ('20120628', 100), ('20120629', 103), ('20120630', 103), ('20120701', 103), ('20120702', 104), ('20120703', 106), ('20120704', 106), ('20120705', 106), ('20120706', 104), ('20120707', 104), ('20120708', 104), ('20120709', 104), ('20120710', 102), ('20120711', 102), ('20120712', 102), ('20120713', 103), ('20120714', 103), ('20120715', 103), ('20120716', 102), ('20120717', 103), ('20120718', 104), ('20120719', 104), ('20120720', 102), ('20120721', 102), ('20120722', 102), ('20120723', 101), ('20120724', 99), ('20120725', 100), ('20120726', 101), ('20120727', 104), ('20120728', 104), ('20120729', 104), ('20120730', 103), ('20120731', 103), ('20120801', 101), ('20120802', 101), ('20120803', 103), ('20120804', 103), ('20120805', 103), ('20120806', 104), ('20120807', 105), ('20120808', 105), ('20120809', 106), ('20120810', 106), ('20120811', 106), ('20120812', 106), ('20120813', 105), ('20120814', 105), ('20120815', 106), ('20120816', 107), ('20120817', 108), ('20120818', 108), ('20120819', 108), ('20120820', 107), ('20120821', 107), ('20120822', 107), ('20120823', 106), ('20120824', 106), ('20120825', 106), ('20120826', 106), ('20120827', 106), ('20120828', 107), ('20120829', 107), ('20120830', 106), ('20120831', 106), ('20120901', 106), ('20120902', 106), ('20120903', 106), ('20120904', 107), ('20120905', 107), ('20120906', 110), ('20120907', 110), ('20120908', 110), ('20120909', 110), ('20120910', 110), ('20120911', 110), ('20120912', 111), ('20120913', 112), ('20120914', 114), ('20120915', 114), ('20120916', 114), ('20120917', 113), ('20120918', 112), ('20120919', 112), ('20120920', 111), ('20120921', 111), ('20120922', 111), ('20120923', 111), ('20120924', 111), ('20120925', 109), ('20120926', 108), ('20120927', 110), ('20120928', 109), ('20120929', 109), ('20120930', 109), ('20121001', 109), ('20121002', 109), ('20121003', 109), ('20121004', 110), ('20121005', 110), ('20121006', 110), ('20121007', 110), ('20121008', 109), ('20121009', 108), ('20121010', 108), ('20121011', 108), ('20121012', 107), ('20121013', 107), ('20121014', 107), ('20121015', 108), ('20121016', 109), ('20121017', 110), ('20121018', 110), ('20121019', 108), ('20121020', 108), ('20121021', 108), ('20121022', 108), ('20121023', 107), ('20121024', 107), ('20121025', 107), ('20121026', 107), ('20121027', 107), ('20121028', 107), ('20121029', 107), ('20121030', 107), ('20121031', 109), ('20121101', 111), ('20121102', 109), ('20121103', 109), ('20121104', 109), ('20121105', 110), ('20121106', 111), ('20121107', 108), ('20121108', 107), ('20121109', 107), ('20121110', 107), ('20121111', 107), ('20121112', 107), ('20121113', 106), ('20121114', 104), ('20121115', 104), ('20121116', 105), ('20121117', 105), ('20121118', 105), ('20121119', 107), ('20121120', 107), ('20121121', 108), ('20121122', 108), ('20121123', 109), ('20121124', 109), ('20121125', 109), ('20121126', 109), ('20121127', 109), ('20121128', 109), ('20121129', 110), ('20121130', 110), ('20121201', 110), ('20121202', 110), ('20121203', 110), ('20121204', 110), ('20121205', 110), ('20121206', 110), ('20121207', 110), ('20121208', 110), ('20121209', 110), ('20121210', 111), ('20121211', 112), ('20121212', 112), ('20121213', 111), ('20121214', 111), ('20121215', 111), ('20121216', 111), ('20121217', 112), ('20121218', 114), ('20121219', 114), ('20121220', 114), ('20121221', 113), ('20121222', 113), ('20121223', 113), ('20121224', 113), ('20121225', 113), ('20121226', 112), ('20121227', 112), ('20121228', 112), ('20121229', 112), ('20121230', 112), ('20121231', 114)], [('20120101', 100), ('20120102', 100), ('20120103', 101), ('20120104', 100), ('20120105', 101), ('20120106', 101), ('20120107', 101), ('20120108', 101), ('20120109', 101), ('20120110', 103), ('20120111', 103), ('20120112', 104), ('20120113', 103), ('20120114', 103), ('20120115', 103), ('20120116', 103), ('20120117', 103), ('20120118', 105), ('20120119', 105), ('20120120', 105), ('20120121', 105), ('20120122', 105), ('20120123', 105), ('20120124', 106), ('20120125', 107), ('20120126', 107), ('20120127', 107), ('20120128', 107), ('20120129', 107), ('20120130', 107), ('20120131', 107), ('20120201', 109), ('20120202', 109), ('20120203', 112), ('20120204', 112), ('20120205', 112), ('20120206', 111), ('20120207', 111), ('20120208', 111), ('20120209', 111), ('20120210', 109), ('20120211', 109), ('20120212', 109), ('20120213', 111), ('20120214', 110), ('20120215', 109), ('20120216', 112), ('20120217', 111), ('20120218', 111), ('20120219', 111), ('20120220', 111), ('20120221', 111), ('20120222', 110), ('20120223', 112), ('20120224', 111), ('20120225', 111), ('20120226', 111), ('20120227', 111), ('20120228', 111), ('20120229', 109), ('20120301', 110), ('20120302', 108), ('20120303', 108), ('20120304', 108), ('20120305', 108), ('20120306', 106), ('20120307', 107), ('20120308', 109), ('20120309', 110), ('20120310', 110), ('20120311', 110), ('20120312', 110), ('20120313', 112), ('20120314', 111), ('20120315', 112), ('20120316', 112), ('20120317', 112), ('20120318', 112), ('20120319', 113), ('20120320', 112), ('20120321', 112), ('20120322', 111), ('20120323', 112), ('20120324', 112), ('20120325', 112), ('20120326', 114), ('20120327', 113), ('20120328', 112), ('20120329', 112), ('20120330', 112), ('20120331', 112), ('20120401', 112), ('20120402', 113), ('20120403', 113), ('20120404', 111), ('20120405', 110), ('20120406', 110), ('20120407', 110), ('20120408', 110), ('20120409', 108), ('20120410', 106), ('20120411', 107), ('20120412', 109), ('20120413', 107), ('20120414', 107), ('20120415', 107), ('20120416', 108), ('20120417', 109), ('20120418', 108), ('20120419', 108), ('20120420', 108), ('20120421', 108), ('20120422', 108), ('20120423', 107), ('20120424', 108), ('20120425', 110), ('20120426', 110), ('20120427', 111), ('20120428', 111), ('20120429', 111), ('20120430', 110), ('20120501', 110), ('20120502', 110), ('20120503', 109), ('20120504', 107), ('20120505', 107), ('20120506', 107), ('20120507', 107), ('20120508', 107), ('20120509', 106), ('20120510', 107), ('20120511', 107), ('20120512', 107), ('20120513', 107), ('20120514', 105), ('20120515', 105), ('20120516', 104), ('20120517', 102), ('20120518', 101), ('20120519', 101), ('20120520', 101), ('20120521', 103), ('20120522', 103), ('20120523', 103), ('20120524', 103), ('20120525', 103), ('20120526', 103), ('20120527', 103), ('20120528', 103), ('20120529', 105), ('20120530', 103), ('20120531', 103), ('20120601', 100), ('20120602', 100), ('20120603', 100), ('20120604', 100), ('20120605', 101), ('20120606', 103), ('20120607', 103), ('20120608', 104), ('20120609', 104), ('20120610', 104), ('20120611', 101), ('20120612', 103), ('20120613', 102), ('20120614', 103), ('20120615', 104), ('20120616', 104), ('20120617', 104), ('20120618', 104), ('20120619', 106), ('20120620', 106), ('20120621', 103), ('20120622', 105), ('20120623', 105), ('20120624', 105), ('20120625', 103), ('20120626', 103), ('20120627', 105), ('20120628', 105), ('20120629', 108), ('20120630', 108), ('20120701', 108), ('20120702', 109), ('20120703', 111), ('20120704', 111), ('20120705', 111), ('20120706', 109), ('20120707', 109), ('20120708', 109), ('20120709', 109), ('20120710', 108), ('20120711', 107), ('20120712', 107), ('20120713', 108), ('20120714', 108), ('20120715', 108), ('20120716', 108), ('20120717', 108), ('20120718', 109), ('20120719', 109), ('20120720', 107), ('20120721', 107), ('20120722', 107), ('20120723', 105), ('20120724', 104), ('20120725', 104), ('20120726', 105), ('20120727', 108), ('20120728', 108), ('20120729', 108), ('20120730', 107), ('20120731', 107), ('20120801', 104), ('20120802', 104), ('20120803', 107), ('20120804', 107), ('20120805', 107), ('20120806', 108), ('20120807', 109), ('20120808', 108), ('20120809', 109), ('20120810', 109), ('20120811', 109), ('20120812', 109), ('20120813', 108), ('20120814', 108), ('20120815', 109), ('20120816', 110), ('20120817', 111), ('20120818', 111), ('20120819', 111), ('20120820', 111), ('20120821', 110), ('20120822', 110), ('20120823', 109), ('20120824', 110), ('20120825', 110), ('20120826', 110), ('20120827', 110), ('20120828', 110), ('20120829', 111), ('20120830', 110), ('20120831', 110), ('20120901', 110), ('20120902', 110), ('20120903', 110), ('20120904', 111), ('20120905', 111), ('20120906', 114), ('20120907', 114), ('20120908', 114), ('20120909', 114), ('20120910', 114), ('20120911', 114), ('20120912', 115), ('20120913', 116), ('20120914', 117), ('20120915', 117), ('20120916', 117), ('20120917', 117), ('20120918', 116), ('20120919', 116), ('20120920', 116), ('20120921', 116), ('20120922', 116), ('20120923', 116), ('20120924', 116), ('20120925', 114), ('20120926', 113), ('20120927', 115), ('20120928', 114), ('20120929', 114), ('20120930', 114), ('20121001', 114), ('20121002', 114), ('20121003', 114), ('20121004', 115), ('20121005', 114), ('20121006', 114), ('20121007', 114), ('20121008', 114), ('20121009', 112), ('20121010', 112), ('20121011', 113), ('20121012', 112), ('20121013', 112), ('20121014', 112), ('20121015', 113), ('20121016', 113), ('20121017', 114), ('20121018', 114), ('20121019', 112), ('20121020', 112), ('20121021', 112), ('20121022', 111), ('20121023', 111), ('20121024', 111), ('20121025', 111), ('20121026', 110), ('20121027', 110), ('20121028', 110), ('20121029', 110), ('20121030', 110), ('20121031', 111), ('20121101', 113), ('20121102', 111), ('20121103', 111), ('20121104', 111), ('20121105', 111), ('20121106', 112), ('20121107', 109), ('20121108', 108), ('20121109', 108), ('20121110', 108), ('20121111', 108), ('20121112', 108), ('20121113', 107), ('20121114', 105), ('20121115', 105), ('20121116', 106), ('20121117', 106), ('20121118', 106), ('20121119', 108), ('20121120', 108), ('20121121', 109), ('20121122', 109), ('20121123', 110), ('20121124', 110), ('20121125', 110), ('20121126', 110), ('20121127', 110), ('20121128', 111), ('20121129', 112), ('20121130', 112), ('20121201', 112), ('20121202', 112), ('20121203', 112), ('20121204', 112), ('20121205', 112), ('20121206', 112), ('20121207', 112), ('20121208', 112), ('20121209', 112), ('20121210', 112), ('20121211', 114), ('20121212', 113), ('20121213', 112), ('20121214', 112), ('20121215', 112), ('20121216', 112), ('20121217', 114), ('20121218', 115), ('20121219', 116), ('20121220', 116), ('20121221', 116), ('20121222', 116), ('20121223', 116), ('20121224', 115), ('20121225', 115), ('20121226', 114), ('20121227', 114), ('20121228', 113), ('20121229', 113), ('20121230', 113), ('20121231', 116)]]

        self.chart.xValueAxis.niceMonth               = 1
        self.chart.width           = 200
        self.title.y          = 160
        self.title.x          = 115




    
    

chart().drawOn(pdf,0-cm*1.11,cm*10)
chart2().drawOn(pdf,270,cm*10)
chart3().drawOn(pdf,570,cm*10)
chart4().drawOn(pdf,0-cm*1.11,0)




pdf.save()
