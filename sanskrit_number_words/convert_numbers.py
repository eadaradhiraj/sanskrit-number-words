from .break_words import BreakWords
from .convert_devanagari_to_roman import FromSkt

class ConvertNumbers:

    __ones = {
        "nava": "9",
        "aSTa": "8",
        "sapta": "7",
        "SaT": "6",
        "paJca": "5",
        "cat": "4",
        "tr": "3",
        "ti": "3",
        "dv": "2",
        "eka": "1",
    }
    __tens = {
        "navati": "90",
        "aziiti": "80",
        "saptati": "70",
        "SaSTi": "60",
        "paJcaazat": "50",
        "catvaariMzat": "40",
        "triMzat": "30",
        "viMzat": "20",
        "daza": "10",
    }

    def __get_digit(wd, digits):
        for dig in digits:
            if dig in wd:
                return dig, digits[dig]
        return None


    def __get_ten(wd):
        return ConvertNumbers.__get_digit(wd, ConvertNumbers.__tens)


    def __get_one(wd):
        return ConvertNumbers.__get_digit(wd, ConvertNumbers.__ones)

    def convert(inp_str):
        return ConvertNumbers.convert_from_roman(
            FromSkt.transliterate_from_skt(inp_str)
        )

    def convert_from_roman(inp_str):
        sep_wds = BreakWords.get_words(inp_str)
        res_eq = []
        for idx, wd in enumerate(sep_wds):
            ten_in_wd = ConvertNumbers.__get_ten(wd)
            curr_eq = ""
            if wd.isdigit() or wd == "+":
                res_eq.append(wd)
                continue
            elif wd == "minus":
                if res_eq and res_eq[-1] == '+':
                    res_eq.append("1")
                if res_eq:
                    res_eq[-1] = f"-{res_eq[-1]}"
                elif not res_eq:
                    res_eq.append("-1")
                res_eq.append("+")
                continue
            if ten_in_wd:
                wd = wd.replace(ten_in_wd[0], "")
                curr_eq += ten_in_wd[1]
            one_in_wd = ConvertNumbers.__get_one(wd)
            if one_in_wd:
                curr_eq = curr_eq + "+" + one_in_wd[1]
            if curr_eq:
                res_eq.append(str(eval(curr_eq)))
        final_res_eq = []
        for idx, op in enumerate(res_eq):
            if op.isdigit() and res_eq[idx - 1].isdigit() and idx > 0:
                final_res_eq.append("*")
            final_res_eq.append(op)
        return eval("".join(final_res_eq))
