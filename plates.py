def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:1].isalpha() and 2 <= len(s) <= 6 and s.isalnum() :
        for char in s :
            if char.isdecimal() :
                before = int(s.index(char)) - 1
                if s[before].isalpha() and char == '0' :
                    return False
                elif not char == s[-1] :
                    after = int(s.index(char)) + 1
                    if s[after].isalpha() :
                        return False
                    else :
                        continue
                else :
                    return True
            elif s.isalpha() and 2 <= len(s) <= 6 :
                return True
            else :
                continue
    else :
        return False

main()
