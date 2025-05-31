def twist(s):
    if len(s) == 0:
        return s
    return twist(s[1:]) + s[0]

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()