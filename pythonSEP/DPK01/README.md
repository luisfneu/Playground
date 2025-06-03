# Resultados

## [DPK01_impl_1.py](DPK01_impl_1.py)

    python3 DPK01_impl_1.py
    # chose a word: NEU
    # word twisted: UEN

### teste de mesa: 
1. entrada da funcao main
2. variavel sin = NEU
3. chama funcao twist com palavra digitada no sin
4. lopp com For com cada char de sin ( NEU)
- 1 item do for:
    tmp = "N" + "" = "N"
- 2 item do for: 
    tmp = "E" + "N" = "EN"
- 3 item do for: 
    tmp = "U" + "EN" = "UEN"
5. sout = "UEN" retornado da função twist
6. saida do print com sout


## [DPK01_impl_2.py](DPK01_impl_2.py)  

    python3 DPK01_impl_2.PY
    # chose a word: 123456
    # word twisted: 654321

### teste de mesa: 
1. entrada da funcao main
2. variavel sin = 123456
3. chama funcao twist com palavra digitada no sin
4. executa a funcao inverter a string [::-1] - busca string indice(inicial) e final decrementando 1, este efeito do slicing inverte a string
5. sout = "654321" retornado da função twist
6. saida do print com sout

## [DPK01_impl_3.py](DPK01_impl_3.py)  

    python3 DPK01_impl_3.PY
    # chose a word: LUIS
    # word twisted: SIUL

### teste de mesa: 
1. entrada da funcao main
2. variavel sin = LUIS
3. chama funcao twist com palavra digitada no sin
4. loop com for com cada char de sin ( LUIS)
- 1 item do for:
    tmp = "L" + "" = "L"
- 2 item do for: 
    tmp = "U" + "L" = "UL"
- 3 item do for: 
    tmp = "I" + "UL" = "IUL"
- 4 item do for: 
    tmp = "S" + "IUL" = "SIUL"
5. sout = "SIUL" retornado da função twist
6. saida do print com sout


## [DPK01_impl_4.py](DPK01_impl_4.py)  

    python3 DPK01_impl_4.PY
    # chose a word: 13245
    # word twisted: 54321

### teste de mesa: 
1. entrada da funcao main.
2. variavel sin = 12345.
3. chama funcao twist com palavra digitada no sin.
4. variavel revst = "" (em branco).
5. define o tamanho do indice com base no tamanho da palavra decrementando um ( pois indice tem count inicial em zero).
6. laço com while com cada char desde que idx maior ou igual a zero.
- 1 item do for:
    trevstmp = "1" + "" = "1"
- 2 item do for: 
    trevstmp = "2" + "L" = "21"
- 3 item do for: 
    revst = "3" + "21" = "321"
- 4 item do for: 
    trevstmp = "4" + "321" = "4321"
- 5 item do for: 
    revst = "5" + "4321" = "54321"
5. sout = "5421" retornado da função twist
6. saida do print com sout

## [DPK01_impl_5.py](DPK01_impl_5.py)  

    python3 DPK01_impl_5.PY
    # chose a word: 13245
    # word twisted: 54321

### teste de mesa: 
1. entrada da funcao main.
2. variavel sin = 12345.
3. chama funcao twist com palavra digitada no sin.
3. cria lista(pilha) stack com valores ['1', '2', '3', '4', '5']
4. variavel revst = "" (em branco).
6. laço com while com valores do stack até pilha stack ficar vazia
- pop() - '1' → rstr = "5" → stack = ['1', '2', '3', '4']
- pop() - '2' → rstr = "54" → stack = ['1', '2', '3']
- pop() - '3' → rstr = "543" → stack = ['1', '2']
- pop() - '4' → rstr = "5321" → stack = ['1']
- pop() - '5' → rstr = "54321" → stack = []
7. sout = "54321" retornado da função twist
6. saida do print com sout

## [DPK01_impl_6.py](DPK01_impl_6.py)  

    python3 DPK01_impl_6.PY
    # chose a word: LUIS NEU
    # word twisted: UEN SIUL

### teste de mesa: 
1. entrada da funcao main.
2. variavel sin = NEU.
3. chama funcao twist com palavra digitada no sin.
4. str = LUIS NEU
5. chars = ['L','U','I','S',' ','N','E','U']
6. left =0 e right = 7 - tamanho da string -1 (para poder usar indice correto que começa em 0)
7. While
    - iteração 1 - While de 0 < 7 = true
        - chars[0], chars[7] = chars[7], chars[0]
            -  chars = ['U','U','I','S',' ','N','E','L']
        - left = 0+1 =1
        - right = 7-1 = 6
    - iteração 2 - While de 1 < 6 = true
        - chars[1], chars[6] = chars[6], chars[1]
            -  chars = ['U','E','I','S',' ','N','U','L']
        - left = 1+1 =2
        - right = 6-1 = 5
    - iteração 3 - While de 2 < 5 = true
        - chars[2], chars[5] = chars[5], chars[2]
            -  chars = ['U','E','N','S',' ','I','U','L']
        -left = 2+1 =3
        -right = 5-1 = 4
    - iteração 4 - While de 3 < 4 = true
        -chars[3], chars[4] = chars[4], chars[3]
            -  chars = ['U','E','N',' ','S','I','U','L']
        - left = 3+1 =4
        - right = 4-1 = 3
    - iteração 5 - While de 4 < 3 = false
8. chars = ['U','E','N',' ','S','I','U','L']
9. return com join ['U','E','N',' ','S','I','U','L'] com separador '', remotando string
10. sout = "UEN SIUL" retornado da função twist
11. saida do print com sout

## [DPK01_impl_7.py](DPK01_impl_7.py)  

    python3 DPK01_impl_7.PY
    # chose a word: FERNANDO
    # word twisted: ODNANREF

### teste de mesa: 
1. entrada da funcao main.
2. variavel sin = FERNANDO.
3. chama funcao twist com palavra digitada no sin.
4. barray transformando sin em bytearray UTF-8.
5. barray usnado metodo reverse() - que inverte os bytes do proprio array.
6. rstr convertido bytearray para string novamente com metodo decode() em UTF-8
7. sout = "ODNANREF" retornado da função twist
8. saida do print com sout

## [DPK01_impl_8.py](DPK01_impl_8.py)  

    python3 DPK01_impl_8.PY
    # chose a word: NEU
    # word twisted: UEN

### teste de mesa: 
1. entrada da funcao main.
2. variavel sin = NEU.
3. chama funcao twist com palavra digitada no sin.
4. retorna com metodo join
    - '' - separador
    - resersed(str) - inverte a string
    - retorna string invertida com separador '' ( string em branco)
7. sout = "UEN" retornado da função twist
8. saida do print com sout

## [DPK01_impl_9.py](DPK01_impl_9.py)  

    python3 DPK01_impl_9.PY
    # chose a word: LUIS F
    # word twisted: F SIUL

### teste de mesa: 
1. entrada da funcao main
2. variavel sin = "LUIS F"
3. chama funcao twist com palavra digitada no sin
4. executa a função inverter a string
5. sout = "F SIUL" retornado da função twist
6. saida do print com sout

## [DPK01_impl_10.py](DPK01_impl_10.py)

    python3 DPK01_impl_10.PY
    # chose a word: 123
    # word twisted: 321

1. Solução ja utilizada anteriormente, apenas para treinamento
2. Mesmo que: [DPK01_impl_1.py](DPK01_impl_1.py)