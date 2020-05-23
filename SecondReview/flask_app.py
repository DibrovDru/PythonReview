from flask import Flask
from flask import render_template
from lxml import etree
import requests


def parseStatisticsXML(xml_file):
    data_list = []
    file = open(xml_file, 'r')
    root = etree.parse(file)

    for valute in root.getroot().getchildren():
        temp_nominal = []
        for symbols in valute[4].text:
            if symbols == ',':
                temp_nominal.append('.')
            else:
                temp_nominal.append(symbols)

        data_list.append(valute[3].text + ' ' + str(float(''.join(temp_nominal)) / float(valute[2].text)))

    return data_list

app = Flask(__name__)
file = open('valute_xml', 'wb')
ufr = requests.get("http://www.cbr.ru/scripts/XML_daily_eng.asp")
file.write(ufr.content)
file.close()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='tempCourse', valute_list=parseStatisticsXML('valute_xml'))