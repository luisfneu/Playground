def revList (lst): 
    return lst[::-1]

def main():
    listIn = input("* Type a list separete by , (comma) : ")
    listIn = listIn.split(',')
    listOut = revList(listIn)
    print("* Reversed List :",listOut)

main()