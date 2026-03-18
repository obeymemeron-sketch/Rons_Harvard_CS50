while True:
    try:
        x, y = input("Fraction: ").split('/')
        answer = round(float(x) / float(y) * 100)
        if answer < 0 or answer > 100 or "." in x or "." in y :
            pass
        else :
            if answer >= 99 :
                print("F")
            elif answer <= 1 :
                print("E")
            else :
                print(f"{answer}%")
            break
    except (ValueError, ZeroDivisionError):
        pass
