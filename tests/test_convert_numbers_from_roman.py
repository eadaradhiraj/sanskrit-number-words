import unittest
from sanskrit_number_words import ConvertNumbers


class TestCases(unittest.TestCase):
    def test_convert_numbers(self):
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="ekaannazata"), 99)
        self.assertEqual(
            ConvertNumbers.convert_from_roman(inp_str="ekaannaayuta"), 9999
        )
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="ekonaayuta"), 9999)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="Unaayuta"), 9999)
        self.assertEqual(
            ConvertNumbers.convert_from_roman(
                inp_str="navanavatyadhikanavazataadhikanavasahasra"
            ),
            9999,
        )
        self.assertEqual(
            ConvertNumbers.convert_from_roman(
                inp_str="navanavatyuttaranavazatottaranavasahasra"
            ),
            9999,
        )
        self.assertEqual(
            ConvertNumbers.convert_from_roman(
                inp_str="aSTaaziityadhikaaSTazataadhikaaSTasahasra"
            ),
            8888,
        )
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="SaTzatam"), 600)
        self.assertEqual(
            ConvertNumbers.convert_from_roman(inp_str="SaDuttarazatam"), 106
        )
        self.assertEqual(
            ConvertNumbers.convert_from_roman(inp_str="SaDadhikazatam"), 106
        )
        self.assertEqual(
            ConvertNumbers.convert_from_roman(
                inp_str="saptaaziityadhikanavazataadhikanavasahasra"
            ),
            9987,
        )
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="paJcaannazata"), 95)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="paJconazata"), 95)
        self.assertEqual(
            ConvertNumbers.convert_from_roman(inp_str="tryadhikazatam"), 103
        )
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="tryUnazatam"), 97)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="tryUnazatam"), 97)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="tisraH"), 3)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="trINi"), 3)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="trayaH"), 3)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="UnaviMzat"), 19)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="zatonazata"), 0)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="SoDaza"), 16)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="UnatriMzat"), 29)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="trizatakam"), 300)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="zatatrayam"), 300)
        self.assertEqual(
            ConvertNumbers.convert_from_roman(inp_str="zatazatakam"), 10000
        )
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="zatacatuSkam"), 400)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="zatapaJcakam"), 500)
        self.assertEqual(ConvertNumbers.convert_from_roman(inp_str="zatadvayam"), 200)
