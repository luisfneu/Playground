def twist(str):
    rstr = ""
    for char in str:
        rstr = char + rstr
    return rstr

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()