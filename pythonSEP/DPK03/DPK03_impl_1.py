lookup = [
    {"id": 1, "name": "John", "email": "john@john.jhon.com"},
    {"id": 2, "name": "lneu", "email": "lneu@google.com"},
    {"id": 3, "name": "Bina", "email": "bina@teste.com"}
]
lookup_map = {}
for user in lookup:
    lookup_map[user["id"]] = user["name"]
    lookup_map[user["name"]] = user["email"]
    lookup_map[user["email"]] = user["name"]

def lookup(key):
    return lookup_map.get(key, "Not found")

print(lookup(2))
print(lookup("John"))
print(lookup("john@john.jhon.com"))
print(lookup("lneu@google.com"))
print(lookup("Bina"))
print(lookup("xxx"))