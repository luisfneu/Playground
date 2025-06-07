def revList (lst): 
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

def main():
    listIn = input("* Type a list separete by , (comma) : ")
    listIn = listIn.split(',')
    listOut = revList(listIn)
    print("* Reversed List :",listOut)

main()