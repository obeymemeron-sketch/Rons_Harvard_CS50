answer = input('Greeting : ').title()

if 'Hello' in answer :
    print('$0')

elif answer.startswith('H') :
    print('$20')

else :
    print('$100')
