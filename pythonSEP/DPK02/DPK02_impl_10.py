def revL (l): 
    return l[::-1]

def main():
    stIn = input("")
    stIn = stIn.split(',')
    stOut = revL(stIn)
    print(stOut)

main()