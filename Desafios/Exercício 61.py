pt = int (input('Digite o priemiro termo da PA: '))
rz = int (input('Digite a razão da PA: '))
while True:
    for pa in range (pt, pt * 10, rz):
        print(pa)
    break