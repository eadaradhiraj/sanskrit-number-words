import unittest
from sanskrit_number_words.break_words import BreakWords

class TestCases(unittest.TestCase):
    def test_breaks(self):
        self.assertEqual(
            BreakWords.get_words(
                "navanavatyuttaranavazatottaranavasahasra"
            ),
            ['navanavati', '+', 'nava', '100', '+', 'nava', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "navanavatyadhikanavazatottaranavasahasra"
            ),
            ['navanavati', '+', 'nava', '100', '+', 'nava', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "navanavatyadhikanavazataadhikanavasahasra"
            ),
            ['navanavati', '+', 'nava', '100', '+', 'nava', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "navanavatyadhikanavazatottaranavasahasra"
            ),
            ['navanavati', '+', 'nava', '100', '+', 'nava', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptaaziityadhikanavazataadhikanavasahasra"
            ),
            ['saptaaziiti', '+', 'nava', '100', '+', 'nava', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "navanavatyadhikaikazataadhikaikasahasra"
            ),
            ['navanavati', '+', 'eka', '100', '+', 'eka', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptottarazatam"
            ),
            ['sapta', '+', '100', 'm']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptazata"
            ),
            ['sapta', '100']
        )
        self.assertEqual(
            BreakWords.get_words(
                "SoDaza"
            ),
            ['16']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptottarazata"
            ),
            ['sapta', '+','100']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptasaptatizata"
            ),
            ['saptasaptati','100']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptasaptatizatakoTi"
            ),
            ['saptasaptati','100', '10000000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptasaptatyuttarazatakoTi"
            ),
            ['saptasaptati', '+', '100', '10000000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "saptaaziityadhikanavazataadhikanavasahasra"
            ),
            ['saptaaziiti', '+', 'nava', '100', '+', 'nava', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "ekaannasahasra"
            ),
            ['eka', 'minus', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "ekonasahasra"
            ),
            ['eka', 'minus', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "ekonaayuta"
            ),
            ['eka', 'minus', '10000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "ekaannaayuta"
            ),
            ['eka', 'minus', '10000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "ekonaarbuda"
            ),
            ['eka', 'minus', '1000000000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "Unasahasra"
            ),
            ['minus', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "paJcaannasahasra"
            ),
            ['paJca', 'minus', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "paJconasahasra"
            ),
            ['paJca', 'minus', '1000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "caturayuta"
            ),
            ['catur', '10000']
        )
        self.assertEqual(
            BreakWords.get_words(
                "caturUnaayuta"
            ),
            ['catur', 'minus', '10000']
        )
