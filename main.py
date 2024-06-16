# Generatory

def generuj_liczby():
    yield 1
    yield 2
    yield 3


generator = generuj_liczby()

# for liczba in generator:
#     print(liczba)
#     break
#
# print("Po pętli")
#
# for liczba in generator:
#     print(liczba)


def read_file_number():
    with open("plik.txt") as f:
        while True:
            linia = f.readline().strip()
            if not linia:
                return
            yield linia


suma = 0
for num in read_file_number():
    suma += int(num)

print(suma)
