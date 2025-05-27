def twist (string): 
    return string[4::-1]
    # trabalhar com slicing em python
    # <object_name>[<start_index>, <stop_index>, <step>]
    # [::-1] busca o indice do final para o inicio
    # O <start_index> ou <stop_index> nunca é incluso se especificado
    # [4::-1] entrada 123456789 saida 54321 começa na posicao 4 (5o char) e vai até o inicio 

def main():
    sin = input("# chose a word: ")
    sout = twist(sin)
    print("# word twisted:",sout)

main()