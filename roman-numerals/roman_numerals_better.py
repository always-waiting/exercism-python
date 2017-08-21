import sys
def numeral(number):
    number = int(number)
    # thousands
    roman = ("M" * (number / 1000))

    # hundreds
    roman += form_numeral(((number % 1000) / 100), "M", "D", "C")

    #tens
    roman += form_numeral((((number % 1000) % 100) / 10), "C", "L", "X")

    #ones
    roman += form_numeral((((number % 1000) % 100) % 10), "X", "V", "I")

    return roman

def form_numeral(number, highest, middle, single):
    if number == 5:
        # middle numeral
        return middle
    elif number == 4:
        # middle numeral less one
        return single + middle
    elif number == 9:
        # highest numeral less one
        return single + highest
    elif number <= 3:
        # single numeral times count
        return single * number
    elif number >= 6:
        # middle number times single count less 5
        return middle + (single * (number - 5))

if __name__ == "__main__":
    print numeral(sys.argv[1])
