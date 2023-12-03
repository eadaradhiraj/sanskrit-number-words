import unittest
from sanskrit_number_words import ConvertNumbers


class TestCases(unittest.TestCase):
    def test_convert_numbers(self):
        self.assertEqual(ConvertNumbers.convert(inp_str="षट्शतम्"), 600)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकान्नशत"), 99)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकान्नायुत"), 9999)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोनायुत"), 9999)
        self.assertEqual(ConvertNumbers.convert(inp_str="ऊनायुत"), 9999)
        self.assertEqual(
            ConvertNumbers.convert(inp_str="नवनवत्यधिकनवशताधिकनवसहस्र"), 9999
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="नवनवत्युत्तरनवशतोत्तरनवसहस्र"), 9999
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="अष्टाशीत्यधिकाष्टशताधिकाष्टसहस्र"), 8888
        )
        self.assertEqual(ConvertNumbers.convert(inp_str="षडुत्तरशतम्"), 106)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडधिकशतम्"), 106)
        self.assertEqual(
            ConvertNumbers.convert(inp_str="सप्ताशीत्यधिकनवशताधिकनवसहस्र"), 9987
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="सप्ताशीत्युत्तरनवशतोत्तरनवसहस्र"), 9987
        )
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चान्नशत"), 95)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चोनशत"), 95)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्यधिकशतम्"), 103)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्यूनशतम्"), 97)
        self.assertEqual(ConvertNumbers.convert(inp_str="तिस्रः"), 3)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रीणि"), 3)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रयः"), 3)
        self.assertEqual(ConvertNumbers.convert(inp_str="ऊनविंशत्"), 19)
        self.assertEqual(ConvertNumbers.convert(inp_str="शतोनशतम्"), 0)
        self.assertEqual(ConvertNumbers.convert(inp_str="षोडश"), 16)
        self.assertEqual(ConvertNumbers.convert(inp_str="ऊनत्रिंशत्"), 29)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रिशतकम्"), 300)
        self.assertEqual(ConvertNumbers.convert(inp_str="शतत्रयम्"), 300)
        self.assertEqual(ConvertNumbers.convert(inp_str="शतशतकम्"), 10000)
        self.assertEqual(ConvertNumbers.convert(inp_str="शतचतुष्कम्"), 400)
        self.assertEqual(ConvertNumbers.convert(inp_str="शतपञ्चकम्"), 500)
        self.assertEqual(ConvertNumbers.convert(inp_str="शतद्वयम्"), 200)
        self.assertEqual(
            ConvertNumbers.convert(
                inp_str="पञ्चत्रिंशदधिकचतुःशताधिकपञ्चषष्टिसहस्राधिकसप्तलक्षाधिकपञ्चाशत्प्रयुत"
            ),
            50765435,
        )
        self.assertEqual(
            ConvertNumbers.convert(
                inp_str="एकनवत्यधिकद्विशताधिकाष्टाचत्वारिंशत्सहस्राधिकसप्तलक्षाधिकप्रयुत"
            ),
            1748291,
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="अष्टासप्तत्यधिकत्रिशताधिकपञ्चदशसहस्र"),
            15_378,
        )
        self.assertEqual(ConvertNumbers.convert(inp_str="एकाधिकायुत"), 10_001)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोत्तरायुत"), 10_001)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवशतमहापद्म"), 900000000000000)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्यधिकशत"), 102)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्युत्तरशत"), 102)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोत्तरशत"), 101)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकाधिकशत"), 101)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्यधिकशत"), 103)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्युत्तरशत"), 103)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरधिकशत"), 104)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरुत्तरशत"), 104)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चाधिकशत"), 105)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चोत्तरशत"), 105)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडधिकशत"), 106)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडुत्तरशत"), 106)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्ताधिकशत"), 107)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तोत्तरशत"), 107)
        self.assertEqual(ConvertNumbers.convert(inp_str="अष्टाधिकशत"), 108)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवाधिकशत"), 109)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवोत्तरशत"), 109)
        self.assertEqual(ConvertNumbers.convert(inp_str="दशाधिकशत"), 110)
        self.assertEqual(ConvertNumbers.convert(inp_str="दशोत्तरशत"), 110)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकादशाधिकशत"), 111)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकादशोत्तरशत"), 111)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वादशाधिकशत"), 112)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वादशोत्तरशत"), 112)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रयोदशाधिकशत"), 113)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रयोदशोत्तरशत"), 113)
        self.assertEqual(ConvertNumbers.convert(inp_str="विंशत्यधिकशत"), 120)
        self.assertEqual(ConvertNumbers.convert(inp_str="विंशत्युत्तरशत"), 120)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकविंशत्यधिकशत"), 121)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकविंशत्युत्तरशत"), 121)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वाविंशत्यधिकशत"), 122)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वाविंशत्युत्तरशत"), 122)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रिंशदधिकशत"), 130)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकत्रिंशदधिकशत"), 131)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकत्रिंशदुत्तरशत"), 131)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वात्रिंशदधिकशत"), 132)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वात्रिंशदधिकशत"), 132)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवनवत्यधिकशत"), 199)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोनद्विशत"), 199)
        self.assertEqual(ConvertNumbers.convert(inp_str="ऊनद्विशत"), 199)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकान्नद्विशत"), 199)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवनवत्युत्तरशत"), 199)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरयुत"), 40000)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोत्तरद्विशत"), 201)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकाधिकद्विशत"), 201)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्यधिकद्विशत"), 202)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्युत्तरद्विशत"), 202)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्यधिकद्विशत"), 203)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्युत्तरद्विशत"), 203)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरधिकद्विशत"), 204)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरुत्तरद्विशत"), 204)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चाधिकद्विशत"), 205)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चोत्तरद्विशत"), 205)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडधिकद्विशत"), 206)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडुत्तरद्विशत"), 206)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्ताधिकद्विशत"), 207)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तोत्तरद्विशत"), 207)
        self.assertEqual(ConvertNumbers.convert(inp_str="अष्टाधिकद्विशत"), 208)
        self.assertEqual(ConvertNumbers.convert(inp_str="अष्टोत्तरद्विशत"), 208)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवाधिकद्विशत"), 209)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवोत्तरद्विशत"), 209)
        self.assertEqual(ConvertNumbers.convert(inp_str="दशाधिकद्विशत"), 210)
        self.assertEqual(ConvertNumbers.convert(inp_str="दशोत्तरद्विशत"), 210)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकादशाधिकद्विशत"), 211)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकादशोत्तरद्विशत"), 211)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वादशाधिकद्विशत"), 212)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्वादशोत्तरद्विशत"), 212)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रिंशदधिकद्विशत"), 230)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रिंशदुत्तरद्विशत"), 230)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्रयस्त्रिंशदधिकद्विशत"), 233)
        self.assertEqual(
            ConvertNumbers.convert(inp_str="त्रयस्त्रिंशदुत्तरद्विशत"), 233
        )
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुस्त्रिंशदधिकद्विशत"), 234)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुस्त्रिंशदुत्तरद्विशत"), 234)
        self.assertEqual(ConvertNumbers.convert(inp_str="चत्वारिंशदधिकद्विशत"), 240)
        self.assertEqual(ConvertNumbers.convert(inp_str="चत्वारिंशदुत्तरद्विशत"), 240)
        self.assertEqual(
            ConvertNumbers.convert(inp_str="त्रयश्चत्वारिंशदधिकद्विशत"), 243
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="त्रयश्चत्वारिंशदुत्तरद्विशत"), 243
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="चतुश्चत्वारिंशदधिकद्विशत"), 244
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="चतुश्चत्वारिंशदुत्तरद्विशत"), 244
        )
        self.assertEqual(ConvertNumbers.convert(inp_str="नवनवत्यधिकद्विशत"), 299)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोनत्रिशत"), 299)
        self.assertEqual(ConvertNumbers.convert(inp_str="ऊनत्रिशत"), 299)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकान्नत्रिशत"), 299)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवनवत्युत्तरद्विशत"), 299)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकाधिकत्रिशत"), 301)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोत्तरत्रिशत"), 301)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्यधिकचतुःशत"), 402)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्युत्तरचतुःशत"), 402)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्यधिकपञ्चशत"), 503)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्युत्तरपञ्चशत"), 503)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरधिकषट्शत"), 604)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरुत्तरषट्शत"), 604)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चाधिकसप्तशत"), 705)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चोत्तरसप्तशत"), 705)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडधिकाष्टशत"), 806)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडुत्तराष्टशत"), 806)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्ताधिकनवशत"), 907)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तोत्तरनवशत"), 907)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चाशदधिकनवशत"), 950)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चाशदुत्तरनवशत"), 950)
        self.assertEqual(ConvertNumbers.convert(inp_str="षष्ट्यधिकनवशत"), 960)
        self.assertEqual(ConvertNumbers.convert(inp_str="षष्ट्युत्तरनवशत"), 960)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तत्यधिकनवशत"), 970)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तत्युत्तरनवशत"), 970)
        self.assertEqual(ConvertNumbers.convert(inp_str="अशीत्यधिकनवशत"), 980)
        self.assertEqual(ConvertNumbers.convert(inp_str="अशीत्युत्तरनवशत"), 980)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवत्यधिकनवशत"), 990)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवत्युत्तरनवशत"), 990)

        self.assertEqual(ConvertNumbers.convert(inp_str="नवनवत्यधिकनवशत"), 999)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोनसहस्र"), 999)
        self.assertEqual(ConvertNumbers.convert(inp_str="ऊनसहस्र"), 999)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकान्नसहस्र"), 999)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवनवत्युत्तरनवशत"), 999)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकाधिकसहस्र"), 1001)
        self.assertEqual(ConvertNumbers.convert(inp_str="एकोत्तरसहस्र"), 1001)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्यधिकद्विसहस्र"), 2002)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्युत्तरद्विसहस्र"), 2002)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्युत्तरत्रिसहस्र"), 3003)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्यधिकचतुस्सहस्र"), 4002)
        self.assertEqual(ConvertNumbers.convert(inp_str="द्व्युत्तरचतुस्सहस्र"), 4002)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्यधिकपञ्चसहस्र"), 5003)
        self.assertEqual(ConvertNumbers.convert(inp_str="त्र्युत्तरपञ्चसहस्र"), 5003)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरधिकषट्सहस्र"), 6004)
        self.assertEqual(ConvertNumbers.convert(inp_str="चतुरुत्तरषट्सहस्र"), 6004)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चाधिकसप्तसहस्र"), 7005)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चोत्तरसप्तसहस्र"), 7005)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडधिकाष्टसहस्र"), 8006)
        self.assertEqual(ConvertNumbers.convert(inp_str="षडुत्तराष्टसहस्र"), 8006)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्ताधिकनवसहस्र"), 9007)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तोत्तरनवसहस्र"), 9007)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चशताधिकनवसहस्र"), 9500)
        self.assertEqual(ConvertNumbers.convert(inp_str="पञ्चशतोत्तरनवसहस्र"), 9500)
        self.assertEqual(ConvertNumbers.convert(inp_str="षट्शताधिकनवसहस्र"), 9600)
        self.assertEqual(ConvertNumbers.convert(inp_str="षट्शतोत्तरनवसहस्र"), 9600)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तशतोत्तरनवसहस्र"), 9700)
        self.assertEqual(ConvertNumbers.convert(inp_str="सप्तशताधिकनवसहस्र"), 9700)
        self.assertEqual(ConvertNumbers.convert(inp_str="अष्टशताधिकनवसहस्र"), 9800)
        self.assertEqual(ConvertNumbers.convert(inp_str="अष्टशतोत्तरनवसहस्र"), 9800)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवशताधिकनवसहस्र"), 9900)
        self.assertEqual(ConvertNumbers.convert(inp_str="नवशतोत्तरनवसहस्र"), 9900)
        self.assertEqual(
            ConvertNumbers.convert(inp_str="षट्त्रिंशदधिकनवशताधिकनवसहस्र"), 9936
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="षट्त्रिंशदुत्तरनवशतोत्तरनवसहस्र"), 9936
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="शून्यः"), 0
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="द्विसप्तानि सहस्राणि"), 14000
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="द्विपञ्च"), 10
        )
        self.assertEqual(
            ConvertNumbers.convert(inp_str="विंशतिविंशतिः"), 40
        )
