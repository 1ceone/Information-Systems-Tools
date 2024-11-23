X = int(input("Введите количество коллег в клинике:"))
Y = int(input("Введите количество коллег в поликлинике:"))

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd = find_gcd(X, Y)

print(f"Необходимое количетсво кусочков пиццы: {gcd}")