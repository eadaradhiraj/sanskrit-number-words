# Sanskrit Number Words

A module to convert Sanskrit Number words into actual numbers.

See also
 - https://www.sanskrit-trikashaivism.com/en/appendixes-numbers-appen-numbers-1-english-1/ for a basic understanding of how sanskrit number words are work
 - https://en.wikipedia.org/wiki/Devanagari_numerals to understand how numbers are represented in devanagari

## How to Use?

### To run from CLI
    python -m sanskrit_number_words -i <inputstring> -o <outputformat>

### To import as a package
    from sanskrit_number_words import ConvertNumbers
    print(
        ConvertNumbers.convert(
            inp_str="पञ्चत्रिंशदधिकचतुःशताधिकपञ्चषष्टिसहस्राधिकसप्तलक्षाधिकपञ्चाशत्प्रयुत"
            output_format="integer" ## is by default
        )
    )
    # will print 50765435
    print(
        ConvertNumbers.convert(
            inp_str="पञ्चत्रिंशदधिकचतुःशताधिकपञ्चषष्टिसहस्राधिकसप्तलक्षाधिकपञ्चाशत्प्रयुत",
            output_format="devanagari"  ## is not default
        ),
    )
    # will print "५०७६५४३५"


## How to install?
    pip install git+https://github.com/eadaradhiraj/sanskrit-number-words.git#egg=sanskrit-number-words