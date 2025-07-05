map = {1: "John", "John": "john@john.jhon.com", "john@john.jhon.com" :"John" }
map = {2: "Bina", "Bina": "bina@gata.com", "bina@gata.com" :"Bina" }

def lup(value):
    return map.get(value)

print(lup(1))
print(lup("John"))
print(lup("john@john.jhon.com"))
print(lup("xxx"))