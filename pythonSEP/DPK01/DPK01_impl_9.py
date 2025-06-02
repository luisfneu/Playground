def twist(str): 
    return str[::-1]

def main():
    imput_str = input("Enter a string: ")
    string_out = twist(imput_str)
    print(f"Twisted string: {string_out}")

main ()