def main():
    converted = float(convert(input('What time is it? ')))

    if 7 <= converted <= 8 :
        time = 'breakfast'

    elif 12 <= converted <= 13 :
        time = 'lunch'

    elif 18 <= converted <= 19 :
        time = 'dinner'

    print(f'{time} time')


def convert(input):

    if input.endswith('a.m.') :
        if input.startswith('12') :
            h, m = input.split(':')
            h = 0
            m, am = m.split(' ')
            m = float(m)
            m /= 60
            input = float(h) + float(m)
            input = float(input)
            return input

        else :
            h, m = input.split(':')
            h = float(h)
            m, am = m.split(' ')
            m = float(m)
            m /= 60
            input = float(h) + float(m)
            input = float(input)
            return input

    elif input.endswith('p.m.') :
        if input.startswith('12') :
            h, m = input.split(':')
            h = 12
            m, am = m.split(' ')
            m = float(m)
            m /= 60
            input = float(h) + float(m)
            input = float(input)
            return input

        else :
            h, m = input.split(':')
            h = float(h) + 12
            m, am = m.split(' ')
            m = float(m)
            m /= 60
            input = float(h) + float(m)
            input = float(input)
            return input

    else :
        h, m = input.split(':')
        m = float(m)
        m /= 60
        input = float(h) + float(m)
        input = float(input)
        return input

if __name__ == "__main__":
    main()
