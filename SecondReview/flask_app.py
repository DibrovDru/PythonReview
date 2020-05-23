from flask import Flask
from flask import render_template
from lxml import etree
import requests


def parseStatisticsXML(xml_file):
    data_list = []
    with open(xml_file) as file:
        root = etree.parse(file)

    for valute in root.getroot().getchildren():
        temp_nominal = valute[4].text.replace(',', '.')
        data_list.append(valute[3].text + ' ' + str(float(''.join(temp_nominal)) / float(valute[2].text)))

    return data_list

app = Flask(__name__)
ufr = requests.get("http://www.cbr.ru/scripts/XML_daily_eng.asp")
with open('valute_xml', 'wb') as file:
    file.write(ufr.content)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='tempCourse', valute_list=parseStatisticsXML('valute_xml'))