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
5. sout = "UEN"
6. saida do print com sout


## [DPK01_impl_2.py](DPK01_impl_2.py)  

    python3 DPK01_impl_2.PY
    # chose a word: 123456
    # word twisted: 54321

### teste de mesa: 
1. entrada da funcao main
2. variavel sin = 123456
3. chama funcao twist com palavra digitada no sin
4. executa a funcao inverter a string [::-1] - busca string indice(inicial) e final decrementando 1, este efeito do slicing inverte a string
5. sout = "654321"
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
5. sout = "SIUL"
6. saida do print com sout


## [DPK01_impl_4.py](DPK01_impl_4.py)  

    python3 DPK01_impl_4.PY
    # chose a word: 13245
    # word twisted: 54321

### teste de mesa: 
1. entrada da funcao main
2. variavel sin = 12345
3. chama funcao twist com palavra digitada no sin
4. variavel revst = "" (em branco) 
5. define o  indice 
6. laço com while com cada char 
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
5. sout = "5421"
6. saida do print com sout
