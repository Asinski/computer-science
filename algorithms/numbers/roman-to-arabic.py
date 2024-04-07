dct_rom_num = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

dct_diff = {('I', 'V'): 3,
            ('I', 'X'): 8,
            ('X', 'L'): 30,
            ('X', 'C'): 80,
            ('C', 'D'): 300,
            ('C', 'M'): 800}


def roman_to_arabic(roman_number: str) -> int:
    number = 0
    prev_literal = None
    for literal in roman_number:
        if prev_literal and dct_rom_num[prev_literal] < dct_rom_num[literal]:
            number += dct_diff[(prev_literal, literal)]
        else:
            number += dct_rom_num[literal]
        prev_literal = literal

    return number


roman_number = input()
print(roman_to_arabic(roman_number))
