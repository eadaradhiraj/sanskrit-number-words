# Execute with
# $ python -m sanskrit_number_words   (3.10+)

import argparse

from sanskrit_number_words import ConvertNumbers


def main() -> None:
    """Main function to be exposed as a cli script"""
    parser = argparse.ArgumentParser(
        description="""Convert Sanskrit number words to numbers.
        Can convert to integers or hindu numerals"""
    )
    parser.add_argument("-i", "--inputtext", type=str, required=True)
    parser.add_argument(
        "-o", "--outputformat", type=str, required=False, default="integer"
    )

    args = parser.parse_args()
    print(
        ConvertNumbers.convert(
            inp_str=args.inputtext,
            output_format=args.outputformat,
        )
    )


if __name__ == "__main__":
    main()
