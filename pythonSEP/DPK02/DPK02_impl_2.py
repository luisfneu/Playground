def revList (lst): 
    return list(reversed(lst))

def main():
    listIn = input("* Type a list separete by , (comma) : ")
    listIn = listIn.split(',') # split string in , to a list
    listOut = revList(listIn)
    print("* Reversed List :",listOut)

main()