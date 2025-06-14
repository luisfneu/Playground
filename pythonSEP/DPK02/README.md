# Resultados

## [DPK02_impl_1.py](DPK02_impl_1.py)

    python3 DPK02_impl_1.py
    * Type a list separete by , (comma) : 123,456,789,0
    * Reversed List : ['0', '789', '456', '123']

### teste de mesa: 
1. entrada da funcao main
2. digitar * Type a list separete by , (comma) : 
3. input = "132,456,789,0"
4. listIn faz split por ,
5. listIn = ['123', '456', '789', '0']
6. listOut = função revList(['123', '456', '789', '0']) # utiliza slicing do python
6. listOut = ['0', '789', '456', '123']
7. * Reversed List :['0', '789', '456', '123']

## [DPK02_impl_2.py](DPK02_impl_2.py)

    python3 DPK02_impl_2.py
    * Type a list separete by , (comma) : 123,456,789,0
    * Reversed List : ['0', '789', '456', '123']

### teste de mesa: 
1. entrada da funcao main
2. digitar * Type a list separete by , (comma) : 
3. input = "132,456,789,0"
4. listIn faz split por ,
5. listIn = ['123', '456', '789', '0']
6. listOut = função revList(['123', '456', '789', '0']) # utiliza slicing do python
6. listOut = ['0', '789', '456', '123']
7. * Reversed List :['0', '789', '456', '123']

## [DPK02_impl_3.py](DPK02_impl_3.py)

    python3 DPK02_impl_3.py
    * Type a list separete by , (comma) : 132,456,789,0
    * Reversed List : ['0', '789', '456', '132']

### teste de mesa: 
1. entrada da função main
2. exibe: * Type a list separete by , (comma) :
3. input = "132,456,789,0"
4. listIn = input.split(',') ⟶ transforma em lista
5. listIn = ['132', '456', '789', '0']
6. chamada revList(['132', '456', '789', '0'])
7. início: new_lst = []
- iteração 1: item = '132' → new_lst = ['132']
- iteração 2: item = '456' → new_lst = ['456', '132']
- iteração 3: item = '789' → new_lst = ['789', '456', '132']
- iteração 4: item = '0' → new_lst = ['0', '789', '456', '132']
8. listOut = ['0', '789', '456', '132']
9. exibe: * Reversed List : ['0', '789', '456', '132']

## [DPK02_impl_4.py](DPK02_impl_4.py)

    python3 DPK02_impl_4.py
    * Type a list separete by , (comma) : 12,34,56
    * Reversed List : ['56', '34', '12']

1. entrada da função main
2. exibe: * Type a list separete by , (comma) :
3. input = "12,34,56"
4. listIn = input.split(',') → transforma em lista
5. listIn = ['12', '34', '56']
6. chamada revList(['12', '34', '56'])
7. início: new_lst = []
8. range(len(lst) - 1, -1, -1) → range(2, -1, -1) → percorre índices 2, 1, 0
- iteração 1: i = 2 → lst[2] = '56' → new_lst = ['56']
- iteração 2: i = 1 → lst[1] = '34' → new_lst = ['56', '34']
- iteração 3: i = 0 → lst[0] = '12' → new_lst = ['56', '34', '12']
9. listOut = ['56', '34', '12']
10. exibe: * Reversed List : ['56', '34', '12']

## [DPK02_impl_5.py](DPK02_impl_5.py)

    python3 DPK02_impl_5.py
    * Type a list separete by , (comma) : LUIS,FERNANDO,NEU
    * Reversed List : ['NEU', 'FERNANDO', 'LUIS']

1. entrada da função main
2. exibe: * Type a list separete by , (comma) :
3. input = "LUIS,FERNANDO,NEU"
4. listIn = input.split(',') → transforma em lista
5. listIn = ['LUIS', 'FERNANDO', 'NEU']
6. chamada revList(['LUIS', 'FERNANDO', 'NEU'])
7. início: new_lst = []
8. temp = lst[:] → cópia de lst: temp = ['LUIS', 'FERNANDO', 'NEU']
9. loop while temp: enquanto temp não estiver vazia:
- iteração 1: temp.pop() → 'NEU' → new_lst = ['NEU'] | temp = ['LUIS', 'FERNANDO']
- iteração 2: temp.pop() → 'FERNANDO' → new_lst = ['NEU', 'FERNANDO'] | temp = ['LUIS']
- iteração 3: temp.pop() → 'LUIS' → new_lst = ['NEU', 'FERNANDO', 'LUIS'] | temp = []
10. listOut = ['NEU', 'FERNANDO', 'LUIS']
11. exibe: * Reversed List : ['NEU', 'FERNANDO', 'LUIS']