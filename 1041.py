entrada = input().split()
x = float(entrada[0])
y = float(entrada[1])
quadrante = ""
if x == 0 and y == 0:
    quadrante = "Origem"
else:
    if y > 0 and x > 0:
        quadrante = "Q1"
    elif y > 0 and x < 0:
        quadrante = "Q2"
    elif y < 0 and x < 0:
        quadrante = "Q3"
    elif y < 0 and x > 0:
        quadrante = "Q4"
    elif y == 0 and x != 0:
        quadrante = "Eixo X"
    elif y != 0 and x == 0:
        quadrante = "Eixo Y"
print(quadrante)
