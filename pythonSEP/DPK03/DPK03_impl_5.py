id_to_name = {1: "John"}
name_to_email = {"John": "john@john.jhon.com"}
email_to_name = {"john@john.jhon.com": "John"}

def lookup(key):
    if isinstance(key, int):
        return id_to_name.get(key)
    elif key in name_to_email:
        return name_to_email[key]
    elif key in email_to_name:
        return email_to_name[key]
    else:
        return "not found"
    
print(lookup("blabla"))
print(lookup("John"))
print(lookup("john@john.jhon.com"))
