def revertList (l): 
    return l[::-1]
def main():
    In = input("separa por - ")
    In = In.split(',')
    Out = revertList(In)
    print(Out)

main()