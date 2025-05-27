def twist (word): 
    wordtmp = ""
    for char in word:
        wordtmp = char + wordtmp
    return wordtmp

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()