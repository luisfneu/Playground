lookup = [
    {"id": 1, "name": "John", "email": "john@john.jhon.com"},
    {"id": 2, "name": "lneu", "email": "lneu@google.com"},
    {"id": 3, "name": "Bina", "email": "bina@teste.com"}
]

lookupped = {}

for lookups in lookup:
    lookupped[lookups["id"]] = lookups["name"]
    lookupped[lookups["name"]] = lookups["email"]
    lookupped[lookups["email"]] = lookups["name"]

def lookup(key):
    return lookupped.get(key, "Not found")

print(lookup(2))
print(lookup("John"))
print(lookup("john@john.jhon.com"))
print(lookup("lneu@google.com"))
print(lookup("Bina"))
print(lookup("xxx"))