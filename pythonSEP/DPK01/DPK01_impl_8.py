def twist(str):
    return ''.join(reversed(str))
    # join the characters in the string in reverse order
    # using the built-in reversed function and join method
    # ''- separates the characters with no separator
    # reversed(str) returns an iterator that build characters in reverse order

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()