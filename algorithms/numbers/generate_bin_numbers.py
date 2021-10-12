

def gen_bin(m, prefix=""):
    if m == 0:
        print(prefix)
        return
    # gen_bin(m - 1, prefix + "0")
    # gen_bin(m - 1, prefix + "1")
    for digit in "0", "1":
        gen_bin(m - 1, prefix + digit)


length_number = int(input())
gen_bin(length_number)
