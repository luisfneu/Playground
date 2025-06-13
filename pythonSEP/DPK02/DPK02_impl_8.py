def reverseL(l): 
    return list(reversed(l))

def main():
    listI = input("valor entrada sep por : ")
    listI = listI.split(':')
    listO = reverseL(listI)
    print(listO)
    
main()