class LookupService:
    def __init__(self):
        self.id_to_name = {}
        self.name_to_email = {}
        self.email_to_name = {}
    
    def add_entry(self, id_, name, email):
        self.id_to_name[id_] = name
        self.name_to_email[name] = email
        self.email_to_name[email] = name

    def lookup(self, key):
        if isinstance(key, int):
            return self.id_to_name.get(key, "Not found")
        elif isinstance(key, str):
            if key in self.name_to_email:
                return self.name_to_email[key]
            elif key in self.email_to_name:
                return self.email_to_name[key]
            else:
                return "Not found"
        else:
            return "Invalid"
if __name__ == "__main__":
    service = LookupService() 
    service.add_entry(1, "John", "john@john.jhon.com")
    service.add_entry(2, "luis", "luis@fernando.neu.com")
    service.add_entry(3, "sabrina", "sabrina@123.com")
    
    print(service.lookup("john@john.jhon.com")) 
    print(service.lookup(2))
    print(service.lookup("sabrina"))
 