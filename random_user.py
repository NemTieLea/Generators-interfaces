import requests


def get_random_user_name():
    url = "https://randomuser.me/api/?ersults=1"
    u = requests.get(url).json()['results'][0]['name']['last']
    return u['first'], u['last']


def generate_random_users():
    while True:
        yield get_random_user_name()


generator = get_random_user_name()
for user in generator:
    print(user)
    akcja = input("Czy przerwac (y/n: ")
    if akcja == 'y':
        print("Przerywam petle")
        break
