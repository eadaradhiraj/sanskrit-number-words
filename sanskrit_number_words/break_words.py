class BreakWords:
    __summations = {
        "radhika": "r + ",
        "aadhika": "a + ",
        "yadhika": "i + ",
        "dadhika": "t + ",
        "Dadhika": "T + ",

        "ruttara": "r + ",
        "yuttara": "i + ",
        "ottara": "a + ",
        "duttara": "t + ",
        "Duttara": "T + ",

        "rUna": "r minus ",
        "yUna": "i minus ",
        "ona": "a minus ",
        "dUna": "t minus ",
        "DUna": "T minus ",

        "dayuta": "t 10000 ",
        "Dayuta": "T 10000 ",
        "yayuta": "i 10000 ",
        "aayuta": "a 10000 ",

        "danna": "t minus ",
        "Danna": "T minus ",
        "yanna": "i minus ",
        "aanna": "a minus ",

        "darbuda": "t 1000000000 ",
        "Darbuda": "T 1000000000 ",
        "yarbuda": "i 1000000000 ",
        "aarbuda": "a 1000000000 ",
    }
    __non_tens = {
        "prayuta": " 1000000 ",
        "mahaapadma": "1000000000000",
        "zata": " 100 ",
        "sahasra": " 1000 ",
        "koTi": " 10000000 ",
        "Una": " minus ",
        "anna": " minus ",
        "ayuta": " 10000 ",
        "arbuda": " 1000000000 ",
        "lakSa": " 100000 ",
        "SoDaza": " 16 "
    }
    def __break_words(inp_string, _dict):
        res = inp_string
        _dict_keys = list(_dict.keys())
        key_idx = 0
        while key_idx < len(_dict_keys):
            _key = _dict_keys[key_idx]
            index = res.find(_key)
            if index > -1:
                key_idx = -1
                curr_dict_val = _dict[_key]
                res = res[:index]+curr_dict_val+res[index+len(_key):]
            key_idx += 1
        return res

    def get_words(inp_string):
        strings_without_summations = BreakWords.__break_words(
            inp_string, BreakWords.__summations
        )
        eka_corrections = []
        for _st in strings_without_summations.split(" "):
            if _st.startswith("ika"):
                eka_corrections.append("e"+_st[1:])
                continue
            eka_corrections.append(_st)
        res_strings = BreakWords.__break_words(
            " ".join(eka_corrections), BreakWords.__non_tens
        )
        return (
            [
                _split for _split in "".join(res_strings).split(" ") if len(_split) > 0
            ]
        )
