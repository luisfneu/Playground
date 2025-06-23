lookup = {1: "John", "John": "john@john.jhon.com", "john@john.jhon.com" :"John" }

def lookups(value):
    return lookup.get(value)

print(lookups(1))
print(lookups("John"))
print(lookups("john@john.jhon.com"))
print(lookups("xxx"))