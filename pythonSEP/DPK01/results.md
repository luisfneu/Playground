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
- pop() → '1' → rstr = "5" → stack = ['1', '2', '3', '4']
- pop() → '2' → rstr = "54" → stack = ['1', '2', '3']
- pop() → '3' → rstr = "543" → stack = ['1', '2']
- pop() → '4' → rstr = "5321" → stack = ['1']
- pop() → '5' → rstr = "54321" → stack = []
7. sout = "54321" retornado da função twist
6. saida do print com sout

## [DPK01_impl_6.py](DPK01_impl_6.py)  

    python3 DPK01_impl_6.PY
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