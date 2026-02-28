def convert(n) :
    joined = '_'.join(f'{n}')
    splitted = joined.split('_')

    for word in splitted :

        if word.isupper() :
            index = splitted.index(f'{word}')
            lowered = splitted[index].lower()
            splitted.remove(word)
            splitted.insert(index, '_' + f'{lowered}')

        else :
           pass

    return ''.join(splitted)



def main() :
    snake = convert(input('camelCase :'))
    print(snake)

main()
