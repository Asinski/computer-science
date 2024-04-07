def arabic_to_roman(arabic_number: int) -> str:
    lst_rom_num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    str_arab_num = str(arabic_number)[::-1]
    number = ''
    rom_pointer = 0

    for place in range(len(str_arab_num)):
        if str_arab_num[place] in ['0', '1', '2', '3']:
            number = lst_rom_num[rom_pointer] * int(str_arab_num[place]) + number
        elif str_arab_num[place] is '4':
            number = lst_rom_num[rom_pointer] + lst_rom_num[rom_pointer + 1] + number
        elif str_arab_num[place] in ['5', '6', '7', '8']:
            number = lst_rom_num[rom_pointer + 1] + lst_rom_num[rom_pointer] * (int(str_arab_num[place]) - 5) + number
        elif str_arab_num[place] is '9':
            number = lst_rom_num[rom_pointer] + lst_rom_num[rom_pointer + 2] + number
        rom_pointer += 2

    return number


arabic_number = int(input())
print(arabic_to_roman(arabic_number))
