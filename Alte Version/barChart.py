"Comparison chart"
from reportlab.lib.colors import purple, PCMYKColor, red, Color, CMYKColor, yellow
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, String
from reportlab.lib.validators import Auto
from reportlab.pdfbase.pdfmetrics import stringWidth, EmbeddedType1Face, registerTypeFace, Font, registerFont
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label

class BarChart02(_DrawingEditorMixin,Drawing):
   
    def __init__(self,width=298,height=164,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        # font
        fontName = 'Helvetica'
        # chart
        self._add(self,VerticalBarChart(),name='chart',validate=None,desc=None)
        self.chart.width = 280
        self.chart.height = 106
        # chart bars
        self.chart.bars.strokeColor = None
        self.chart.bars.strokeWidth = 0
        self.chart.barSpacing = 4
        self.chart.barWidth = 14
        self.chart.barLabelFormat   = '%s'
        self.chart.barLabels.nudge           = 5
        self.chart.barLabels.fontName        = fontName
        self.chart.barLabels.fontSize        = 5
        # categoy axis
        self.chart.categoryAxis.labelAxisMode='low'
        self.chart.categoryAxis.labels.angle = 0
        self.chart.categoryAxis.labels.boxAnchor = 'n'
        self.chart.categoryAxis.labels.dy = -6
        self.chart.categoryAxis.labels.fillColor = PCMYKColor(0,0,0,100)
        self.chart.categoryAxis.labels.fontName = fontName
        self.chart.categoryAxis.labels.fontSize = 8
        self.chart.categoryAxis.labels.textAnchor='middle'
        self.chart.categoryAxis.tickShift=1
        self.chart.categoryAxis.visibleTicks = 0
        self.chart.categoryAxis.strokeWidth     = 0
        self.chart.categoryAxis.strokeColor         = None
        self.chart.groupSpacing = 15
        # value axis
        self.chart.valueAxis.avoidBoundFrac     = None
        self.chart.valueAxis.labels.fontName    = fontName
        self.chart.valueAxis.labels.fontSize    = 8
        self.chart.valueAxis.rangeRound         = 'both'
        self.chart.valueAxis.strokeWidth        = 0
        self.chart.valueAxis.visibleGrid        = 1
        self.chart.valueAxis.visibleTicks       = 0
        self.chart.valueAxis.visibleAxis        = 0
        self.chart.valueAxis.gridStrokeColor    = PCMYKColor(100,0,46,46)
        self.chart.valueAxis.gridStrokeWidth    = 0.25
        self.chart.valueAxis.valueStep          = None#3
        self.chart.valueAxis.labels.dx          = -3
        # legend
        self._add(self,Legend(),name='legend',validate=None,desc=None)
        self.legend.alignment = 'right'
        self.legend.boxAnchor = 'sw'
        self.legend.columnMaximum = 3
        self.legend.dx = 8
        self.legend.dxTextSpace = 4
        self.legend.dy = 6
        self.legend.fontSize = 8
        self.legend.fontName = fontName
        self.legend.strokeColor = None
        self.legend.strokeWidth = 0
        self.legend.subCols.minWidth = 55
        self.legend.variColumn = 1
        self.legend.y = 1
        self.legend.deltay = 10
        self.legend.colorNamePairs   =  Auto(obj=self.chart)
        self.legend.autoXPadding     = 65
        # x label
        self._add(self,Label(),name ='XLabel',validate=None,desc="The label on the horizontal axis")
        self.XLabel._text = ""
        self.XLabel.fontSize = 6
        self.XLabel.height = 0
        self.XLabel.maxWidth = 100
        self.XLabel.textAnchor ='middle'
        self.XLabel.x = 140
        self.XLabel.y = 10
        # y label
        self._add(self,Label(),name='YLabel',validate=None,desc="The label on the vertical axis")
        self.YLabel._text = ""
        self.YLabel.angle = 90
        self.YLabel.fontSize = 6
        self.YLabel.height = 0
        self.YLabel.maxWidth = 100
        self.YLabel.textAnchor ='middle'
        self.YLabel.x = 12
        self.YLabel.y = 80
        #sample data
        self.chart.data = [[-2.6000000000000001, -0.80000000000000004, 9.8000000000000007, None, None, None, None], [-1.8999999999999999, 1.3999999999999999, 13.1, None, None, None, None], [-1.8999999999999999, 1.3, 12.199999999999999, 4.9000000000000004, 2.2000000000000002, 5.4000000000000004, 10.6], [-1.7, 2.0, 13.300000000000001, 5.9000000000000004, 3.2000000000000002, 6.4000000000000004, 11.6], [-1.8999999999999999, 1.5, 13.9, 4.0999999999999996, -1.3, 3.8999999999999999, 11.1]]
        self.chart.categoryAxis.categoryNames=['Q3', 'YTD', '1 Year', '3 Year', '5 Year', '7 Year', '10 Year']
        for i in range(len(self.chart.data)): self.chart.bars[i].name = ('BP', 'Shell Transport & Trading', 'Liberty International', 'Persimmon', 'Royal Bank of Scotland',)[i]
        self.width       = 400
        self.height      = 200
        self.chart.x               = 30
        self.chart.y               = 65
        self.legend.x              = 30
        self.chart.bars[0].fillColor   = PCMYKColor(0,100,100,40,alpha=85)
        self.chart.bars[1].fillColor   = PCMYKColor(23,51,0,4,alpha=85)
        self.chart.bars[2].fillColor   = PCMYKColor(100,60,0,50,alpha=85)
        self.chart.bars[3].fillColor   = PCMYKColor(66,13,0,22,alpha=85)
        self.chart.bars.fillColor       = PCMYKColor(100,0,90,50,alpha=85)

if __name__=="__main__": #NORUNTESTS
    BarChart02().save(formats=['pdf'],outDir='.',fnRoot=None)