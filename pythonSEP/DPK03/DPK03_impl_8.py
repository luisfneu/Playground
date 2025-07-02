lookup = [
    {"id": 1, "name": "John", "email": "john@john.jhon.com"},
    {"id": 2, "name": "lneu", "email": "lneu@google.com"},
    {"id": 3, "name": "Bina", "email": "bina@teste.com"}
]
look = {}

for lookups in lookup:
    look[lookups["id"]] = lookups["name"]
    look[lookups["name"]] = lookups["email"]
    look[lookups["email"]] = lookups["name"]

def lookup(key):
    return look.get(key, "n/a")

print(lookup(3))