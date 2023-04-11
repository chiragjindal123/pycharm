a = 'amaama'

mid = int(len(a) // 2)

c = a[:mid]
b = a[mid:]

if a == a[::-1]:
    print("hai")
else:
    print("nahi")


if c==b:
    print('hai')
else:
    print('nahi')