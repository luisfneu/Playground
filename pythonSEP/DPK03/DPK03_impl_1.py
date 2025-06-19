lookup = [
    {"id": 1, "name": "John", "email": "john@john.jhon.com"},
    {"id": 2, "name": "lneu", "email": "lneu@google.com"},
    {"id": 3, "name": "Bina", "email": "bina@teste.com"}
]
id_to_name = {person["id"]: person["name"] for person in lookup}
name_to_email = {person["name"]: person["email"] for person in lookup}
email_to_name = {person["email"]: person["name"] for person in lookup}

def lookup(key):
    if isinstance(key, int):
        return id_to_name.get(key, "ID not found")
    elif isinstance(key, str):
        if key in name_to_email:
            return name_to_email[key]
        elif key in email_to_name:
            return email_to_name[key]
        else:
            return "Name or email not found"
    else:
        return "Invalid key type"

print(lookup(3))
print(lookup("lneu"))
print(lookup("john@john.jhon.com"))