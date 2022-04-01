from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin, String
from reportlab.graphics.charts.lineplots import SimpleTimeSeriesPlot
from reportlab.lib.colors import PCMYKColor


class chart(_DrawingEditorMixin,Drawing):

    def __init__(self,width=400,height=200,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        self._add(self,SimpleTimeSeriesPlot(),name='chart',validate=None,desc=None)
        self.chart.x                = 30
        self.chart.y                = 30
        self.chart.height           = 90
        self.chart.yValueAxis.forceZero               = 0
        self._add(self,String(10,10,'text'),name='title',validate=None,desc=None)
        self.title.text       = 'Simple Time Series Plot'
        self.title.fontSize   = 16
        self.chart.lines[0].strokeColor = PCMYKColor(100,0,90,50,alpha=100)
        self.chart.lines.strokeWidth     = 2
        self.chart.lines[1].strokeColor = PCMYKColor(0,100,100,40,alpha=100)
        self.chart.xValueAxis.xLabelFormat            = '{dd}/{mm}/{YY}'
        self.chart.data = [[('20120101', 50), ('20121231', 114)]]

        self.chart.xValueAxis.niceMonth               = 1
        self.chart.width           = 335
        self.title.y          = 160
        self.title.x          = 115



if __name__=="__main__": #NORUNTESTS
    chart().save(formats=['pdf'],outDir='.',fnRoot=None)
