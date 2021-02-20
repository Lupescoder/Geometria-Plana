# 5 => Losango

D = float(input("Digite um valor para a diagonal maior  "))
d = float(input("Digite um valor para a diagonal menor  "))
if D < d: 
    print("Diagonal Maior é menor que a Diagonal Menor --- error")
else:
    area = (D*d)/2
    print ("Área =%.2f"%area)
