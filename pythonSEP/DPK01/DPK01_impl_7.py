def twist(str):
    barray = bytearray(str, "utf-8")
    barray.reverse()
    rstr = barray.decode("utf-8")
    return rstr

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()