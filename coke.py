amount = 50
change = -50


while True :
    if amount > 0 :
        coin = int(input(f'Amount Due: {amount}\nInsert Coin: '))
        if coin == 25 or coin == 10 or coin == 5 :
            amount -= coin
            change += coin

        else :
            pass

    elif change > 0 :
        print(f'Change Owed: {change}')
        change = 0

    else :
        print(f'Change Owed: {change}')
        break



