from .break_words import BreakWords
from .convert_devanagari_to_roman import FromSkt
from typing import Tuple


class ConvertNumbers:
    """Convert number words to actual numbers

    Returns:
        str or int: returns string or integer output
    """

    __hindu_nums = {
        "0": "०",
        "1": "१",
        "2": "२",
        "3": "३",
        "4": "४",
        "5": "५",
        "6": "६",
        "7": "७",
        "8": "८",
        "9": "९",
    }

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
        "zUnya": "0",
    }

    @staticmethod
    def __get_digit(wd: str, digits: dict) -> Tuple[str, str] | None:
        """Takes a number word and finds its equivalent from a dictionary

        Args:
            wd (str): string input of a number word
            digits (dict): takes a dict input to map equivalents

        Returns:
            tuple or none: returns the equivalent digit and its equivalent or Nothing
        """
        for dig in digits:
            if dig in wd:
                return dig, digits[dig]
        return None

    @staticmethod
    def __get_ten(wd: str) -> Tuple[str, str] | None:
        """Convert double-digit numbers to equivalent

        Args:
            wd (str): number word preferable representing a double-digit number

        Returns:
            tuple or none: returns the equivalent digit
                and its equivalent double-digit number or Nothing
        """
        return ConvertNumbers.__get_digit(wd, ConvertNumbers.__tens)

    @staticmethod
    def __get_one(wd: str) -> Tuple[str, str] | None:
        """Convert single-digit numbers to equivalent

        Args:
            wd (str): number word preferable representing a single-digit number

        Returns:
            tuple or none: returns the equivalent digit
                and its equivalent single-digit number or Nothing
        """
        return ConvertNumbers.__get_digit(wd, ConvertNumbers.__ones)

    @staticmethod
    def convert(inp_str: str, output_format: str = "integer") -> int | str:
        """Convert number words into integer or string

        Args:
            inp_str (str): Number words should be in devanagari format
            output_format (str, optional): Output format if in devanagari will
                return devangari numerals,
                if integer then will return integer type.
                Defaults to "integer".

        Returns:
            int | str: Return either integer type or
                devangari string of the converted output
        """
        return ConvertNumbers.convert_from_roman(
            inp_str=FromSkt.transliterate_from_skt(inp_str), output_format=output_format
        )

    @staticmethod
    def convert_from_roman(inp_str: str, output_format: str = "integer") -> int | str:
        """Convert number words into integer or string

        Args:
            inp_str (str): Number words should be in roman format
            output_format (str, optional): Output format
                if in devanagari will return devangari numerals,
                if integer then will return integer type.
                Defaults to "integer".

        Returns:
            int | str: Return either integer type or
                devangari string of the converted output
        """
        sep_wds = BreakWords.get_words(inp_str)
        res_eq = []
        for idx, wd in enumerate(sep_wds):
            ten_in_wd = ConvertNumbers.__get_ten(wd)
            curr_eq = ""
            if wd.isdigit() or wd == "+":
                res_eq.append(wd)
                continue
            elif wd == "minus":
                if res_eq and res_eq[-1] == "+":
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
        integer_result = eval("".join(final_res_eq))
        if output_format == "devanagari":
            return "".join(
                [ConvertNumbers.__hindu_nums[ch] for ch in str(integer_result)]
            )
        elif output_format == "integer":
            return integer_result
        else:
            return "Invalid output format!!"
