class User:
    def __init__(self, name, age, email, height):
        self.name = name
        self.age = age
        self.email = email
        self.height = height
        self.accounts = {}

    def __str__(self):
        return f"<{self.name}, {self.age} [{self.email}]>"

    def __int__(self):
        return self.age

    def __float__(self):
        return self.height / 100

    def __bool__(self):
        return self.age > 18

    def __len__(self):
        return len(self.name) - 1

    def __setitem__(self, key, value):
        print(f"Zapisuje: {value} do [{key}]")
        if key in self.accounts:
            print("Nie moge zapisac, konto juz zajete")
        else:
            self.accounts[key] = value

    def __getitem__(self, item):
        print(f"Odczytuje wartosc dla: {item}")
        return self.accounts[item]

    def __rshift__(self, other):
        print("Robie rshift")
        other.accounts = self.accounts.copy()
        self.accounts = {}


# dunder -> double underscore


new_user = User("Adam Kowalski", 21, "a.kow@email.com", 170)

s = str(new_user)
print(f"{s}")

print("Wiek usera:", int(new_user))
print("Wzrost usera:", float(new_user), "metra")
print("Liter w imieniu i nazwisku:", new_user.__len__())

# new_user.__setitem__("super bank", 20)
# new_user.__setitem__("bliski bank", 30)

new_user["super bank"] = 20
new_user["bliski bank"] = 30

print(new_user["bliski bank"])


for n, v in [("a bank", 100), ("b bank", 50), ("c bank", 20), ("d bank", 30)]:
    new_user[n] = v


new_user_2 = User("aaa", 121, "a@b.com", 172)

new_user >> new_user_2

print("2:", new_user_2.accounts)
print("1:", new_user.accounts)
