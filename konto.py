class Account:
    def __init__(self):
        self.account_value = 0
        self.auth_owners = {}
        self.current_iter = 0

    def add_money(self, value):
        self.account_value += value

    def __setitem__(self, owner, status):
        self.auth_owners[owner] = status

    def __getitem__(self, owner):
        return self.auth_owners[owner]

    def __add__(self, other):
        return self.account_value + other.account_value

    def __iter__(self):
        return iter(self.auth_owners)

    def items(self):
        for k, v in self.auth_owners.items():
            yield k, v


new_account = Account()
new_account.add_money(200)

new_account["Adam"] = "wszystko"
new_account["Kasia"] = "podglad"
new_account["Basia"] = "wszystko"

print("User")
for owner in new_account:
    print(owner)

print("user, status")
for o, s in new_account.items():
    print(o, s)
