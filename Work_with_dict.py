
users = {
    "Alex": "BMW",
    "Victor": "Audi",
    "Olga": "Posche",
}

users["Oleg"] = "Nissan"

print(users)

print(users.get("Victor"))
print(users.get("Anna"))
print(users.get("Anna", "Client isn't in Dict"))
print(users.keys())

for user in users:
    print(user)

for user in users.keys():
    print(user)

print(users.values())

for user in users.values():
    print(user)

print(users.items())

for user in users.items():
    print(user)

for k, v in users.items():
    print(f'{k} - {v}')

del users["Victor"]
print(users)

users_copy = users.copy()
print(users_copy)

print(users.pop("Olga"))
print(users)

users.clear()
print(users)

fruits = ['Banana', 'Apple', 'Kiwi', 'Mango']
prices = [1.08, 2.32, 3.03, 1.97]

Fruit_dictionary = dict(zip(fruits, prices))
print(Fruit_dictionary)
