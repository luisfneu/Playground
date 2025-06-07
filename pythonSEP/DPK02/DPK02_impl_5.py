def revList (lst): 
    new_lst = []
    temp = lst[:]
    while temp:
        new_lst.append(temp.pop())
    return new_lst

def main():
    listIn = input("* Type a list separete by , (comma) : ")
    listIn = listIn.split(',') # split string in , to a list
    listOut = revList(listIn)
    print("* Reversed List :",listOut)

main()