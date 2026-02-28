answer = input('Expression: ')
x, y, z = answer.split(' ')

x = int(x)
z = int(z)

if '+' in y :
    final = x + z
elif '-' in y :
    final = x - z
elif '/' in y :
    final = x / z
elif '*' in y :
    final = x * z

print(float(final))
