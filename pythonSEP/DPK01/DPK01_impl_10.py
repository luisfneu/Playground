def stwist(str):
    reversed = ""
    for char in str:
        reversed = char + reversed
    return reversed

def main():
    sin = input("# chose a word: ")
    sout = stwist(sin)
    print("# word twisted:", sout)

main ()