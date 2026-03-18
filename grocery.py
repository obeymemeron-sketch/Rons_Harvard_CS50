list = {}

while True:
    try:
        new_item = input("").upper()
        if not new_item in list :
            list[new_item] = 1
        else :
            list[new_item] += 1
    except (KeyError):
        pass
    except (EOFError):
        for item, number in sorted(list.items()) :
            print(f"{number} {item}", end="\n")
        break
