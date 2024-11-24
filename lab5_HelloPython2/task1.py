a = str(input('Введите слово:'))
x = len(a)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if a[x - i] == a[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")