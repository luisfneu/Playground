# pilha com stack e pop()
# https://www.geeksforgeeks.org/stack-in-python/
# Uma pilha (stack) segue o princípio LIFO: Last In, First Out. Ou seja, o último elemento que entra é o primeiro que sai.

def twist(str):
    stack = list(str)
    rstr = ""
    while stack:
        rstr = rstr + stack.pop() # .pop() remove o último elemento da lista e o retorna.
    return rstr

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()