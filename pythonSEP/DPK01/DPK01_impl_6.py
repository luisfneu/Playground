def twist(str):
    chars = list(str)
    left =0 
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left] # swap characters
        left = left + 1 
        right = right - 1
    return ''.join(chars) # join list back into a string

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()