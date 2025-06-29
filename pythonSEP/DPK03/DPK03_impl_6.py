lookup = {"id": 1, "name": "John", "email": "john@john.jhon.com"}
lookup_map = {
    lookup["id"]: lookup["name"],
    lookup["name"]: lookup["email"],
    lookup["email"]: lookup["name"]
}

def lookup(key):
    return lookup_map.get(key)

print(lookup(1))
print (lookup("email"))