class FromSkt:
    """
    Class FromSkt
    This class is used for transliterating from devanagari
    """
    __vowels = {
        "अ": "a",
        "आ": "aa",
        "इ": "i",
        "ई": "ii",
        "उ": "u",
        "ऊ": "U",
        "ए": "e",
        "ऐ": "ai",
        "ओ": "o",
        "औ": "au",
        "ऋ": "R",
        "ॠ": "RR",
        "ऌ": "lR",
        "ॡ": "lRR",
    }

    __vowel_markers = {
        "ा": "aa",
        "ि": "i",
        "ी": "ii",
        "ु": "u",
        "ू": "U",
        "े": "e",
        "ै": "ai",
        "ो": "o",
        "ौ": "au",
        "ृ": "R",
        "ॄ": "RR",
        "ॢ": "lR",
        "ॣ": "lRR",
    }

    __anusvara = {
        "ः": "H",
        "ं": "M",
    }

    __misc = {
        "।": "|",
        "ऽ": "'",
    }

    __consonants = {
        'क': 'ka', 
        'ख': 'kha',
        'ग': 'ga', 
        'घ': 'gha',
        'ङ': 'Ga', 
        'च': 'ca', 
        'छ': 'cha',
        'ज': 'ja', 
        'झ': 'jha',
        'ञ': 'Ja', 
        'ट': 'Ta', 
        'ठ': 'Tha',
        'ड': 'Da', 
        'ढ': 'Dha',
        'ण': 'Na', 
        'त': 'ta', 
        'थ': 'tha',
        'द': 'da', 
        'ध': 'dha',
        'न': 'na', 
        'प': 'pa', 
        'फ': 'pha',
        'ब': 'ba', 
        'भ': 'bha',
        'म': 'ma', 
        'य': 'ya', 
        'र': 'ra', 
        'ल': 'la', 
        'व': 'va', 
        'श': 'za', 
        'ष': 'Sa', 
        'स': 'sa', 
        'ह': 'ha', 
    }

    @staticmethod
    def transliterate_from_skt(text: str) -> str:
        """
        convert DEVANAGARI to custom roman format
        :param text: the input text
        :return: output text in roman text
        """
        res = []
        for ch in text:
            if ch in FromSkt.__consonants:
                res.append(FromSkt.__consonants[ch])
            elif ch in FromSkt.__vowel_markers:
                res[-1] = res[-1][:-1] + FromSkt.__vowel_markers[ch]
            elif ch in FromSkt.__vowels:
                res.append(FromSkt.__vowels[ch])
            elif ch in FromSkt.__misc:
                res.append(FromSkt.__misc[ch])
            elif ch in FromSkt.__anusvara:
                res[-1] = res[-1] + FromSkt.__anusvara[ch]
            elif ch == "्":
                res[-1] = res[-1][:-1]
            else:
                res.append(ch)
        return ''.join(res)
