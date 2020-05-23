import unittest
import requests
from flask_app import parseStatisticsXML

class DataTest(unittest.TestCase):
    def test_data_first(self):
        real_data = ['Australian Dollar 20.9568', 'British Pound Sterling 52.3656',
                'Belarussian Ruble ' + str(12.3701 / 1000), 'Danish Krone ' + str(46.1908 / 10)]

        f = open('valute_xml_first', 'wb')
        ufr = requests.get("http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=22/01/2007")
        f.write(ufr.content)
        f.close()
        our_data_all = parseStatisticsXML('valute_xml_first')
        our_data_for_test = [our_data_all[0], our_data_all[1], our_data_all[2], our_data_all[3]]
        self.assertEqual(real_data, our_data_for_test)

    def test_data_second(self):
        real_data = ['Armenia Dram ' + str(17.2034 / 100), 'Belarussian Ruble ' + str(38.3446 / 10000), 'Bulgarian lev 46.5612']

        f = open('valute_xml_first', 'wb')
        ufr = requests.get("http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=22/01/2016")
        f.write(ufr.content)
        f.close()
        our_data_all = parseStatisticsXML('valute_xml_first')
        our_data_for_test = [our_data_all[3], our_data_all[4], our_data_all[5]]
        self.assertEqual(real_data, our_data_for_test)


if __name__ == '__main__':
    unittest.main()