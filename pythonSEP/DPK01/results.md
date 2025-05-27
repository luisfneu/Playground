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


1. entrada da funcao main
2. variavel sin = 123456
3. chama funcao twist com palavra digitada no sin
4. executa a funcao inverter a string [::-1] - busca string indice(inicial) e final decrementando 1, este efeito do slicing inverte a string
5. sout = "654321"
6. saida do print com sout