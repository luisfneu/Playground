lookup = [
    {"id": 1, "name": "John", "email": "john@john.jhon.com"},
    {"id": 2, "name": "lneu", "email": "lneu@google.com"},
    {"id": 3, "name": "Bina", "email": "bina@teste.com"}
]

def lookups(key):
    for u in lookup:
        for field in ["id", "name", "email"]:
            if u[field] == key:
                if field == "id":
                    return u["name"]
                elif field == "name":
                    return u["email"]
                elif field == "email":
                    return u["name"]
    return "Not found"

print(lookups(2))
print(lookups("John"))
print(lookups("john@john.jhon.com"))
print(lookups("lneu@google.com"))
print(lookups("Bina"))
print(lookups("xxx"))