# Peograma crado para exibição dos dez primeiros termos de uma progressão aritmética.


pt = int (input('Digite o priemiro termo da PA: '))
rz = int (input('Digite a razão da PA: '))
for pa in range (pt, pt * 10, rz):
    print(pa)
