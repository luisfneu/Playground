def revList (lst): 
    new_lst = []
    for item in lst:
        new_lst.insert(0, item)
    return new_lst

def main():
    listIn = input("* Type a list separete by , (comma) : ")
    listIn = listIn.split(',') # split string in , to a list
    listOut = revList(listIn)
    print("* Reversed List :",listOut)

main()