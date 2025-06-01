def twist(str):
    barray = bytearray(str, "utf-8")
    barray.reverse() # metodo reverse do bytearray 
    # barray.reverse() in-place, so no need to assign it back
    rstr = barray.decode("utf-8")
    return rstr

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()