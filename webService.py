from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import urllib
import db_handler
import time
from urllib.parse import urlparse
import bokeh.plotting as pl
import bokeh.models as md
from bokeh.palettes import Dark2_5 as palettes
import itertools
import datetime as dt

def preparePlot():
    coinTypes = ["Maple", "Phil", "Kang", "Krueger"]
    colors = itertools.cycle(palettes)
    pl.output_file("graph.html", title="GoldWatch")

    p = pl.figure(title="Preisverlauf verschiedener Goldmünzen (basierend auf den Daten von https://www.exchange-ag.de/)",plot_width=1000, x_axis_type="datetime")
    datetime = md.DatetimeTickFormatter(days="%d/%m %H:%M", months="%d/%m %H:%M", hours="%d/%m %H:%M", minutes="%d/%m %H:%M")
    p.xaxis.formatter = datetime
    p.add_layout(md.Title(text="Zeitpunkt der Datenerfassung", align="center"), "below")
    p.add_layout(md.Title(text="Goldpreis in €", align="center"), "left")

    tooltip = [
        ("Münztyp", "$name"),
        ("Datum", "$x"),
        ("Wert in €", "$y{int}")
    ]
    formatters = { "@x": "datetime"}
    p.add_tools(md.HoverTool(tooltips=tooltip, formatters=formatters))
    for coin,color in zip(coinTypes,colors):
        data = db_handler.getData(coin)
        tmp = ()
        x = []
        yB = []
        yS = []
        for idx,elem in enumerate(data):
            nTime = time.ctime(elem[0])
            
            x.append(dt.datetime.fromtimestamp(elem[0]))
            yB.append(elem[1])
            yS.append(elem[2])
            # nTime = time.s
        print(x,yB)
        p.line(x, yB, legend_label=f"{coin} Buy", line_color=color, line_width=2, name=f"{coin} Buy")
        p.line(x, yS, legend_label=f"{coin} Sell", line_color=color, line_width=2, line_dash="dashed", name=f"{coin} Sell")

    pl.save(p)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        preparePlot()
        plot = open("graph.html", "rb")
        self.wfile.write(plot.read())

if __name__ == "__main__":
    httpd = HTTPServer(("192.168.178.67", 8000), SimpleHTTPRequestHandler)
    httpd.allow_reuse_address = True
    httpd.serve_forever()