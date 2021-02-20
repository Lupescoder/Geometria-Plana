# 4 => Trapézio

b = float(input("Digite um valor para a base menor  "))
B = float(input("Digite um valor para a base maior  "))
h = float(input("Digite um valor para a altura  "))

if B < b:
    print("Base maior é menor que a Base menor --- error")
else:
    area = ((B + b)*h)/2
    print ("Área =%.2f"%area)
