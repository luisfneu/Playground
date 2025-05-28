def twist(st):
    revst = ""
    idx = len(st) - 1 # define last char index
    while idx >= 0:   # while until index less or equal to 0 
        revst = revst + st[idx]    # build reversed string
        idx = idx -1  # decrement index to use next char
    return revst

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()