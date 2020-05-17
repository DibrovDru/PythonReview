from flask import Flask
from flask import render_template
from lxml import etree
import requests


def parseBookXML(xml_file):
    ffw = []
    f = open(xml_file, 'r')
    root = etree.parse(f)

    for valute in root.getroot().getchildren():
        temp_nominal = []
        for symbols in valute[4].text:
            if symbols == ',':
                temp_nominal.append('.')
            else:
                temp_nominal.append(symbols)

        ffw.append(valute[3].text + ' ' + str(float(''.join(temp_nominal)) / float(valute[2].text)))

    return ffw

app = Flask(__name__)
f = open('valute_xml', 'wb')
ufr = requests.get("http://www.cbr.ru/scripts/XML_daily_eng.asp")
f.write(ufr.content)
f.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='tempCourse', valute_list=parseBookXML('valute_xml'))