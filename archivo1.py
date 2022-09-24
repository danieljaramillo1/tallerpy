numeros=[]

def llenar():
    for n in range (0, 20):
        numero = int(input("Digita un numero entero: "))
        numeros.append(numero)
        
        
llenar()

def recorrer(numeros):
    total=0
    for n in range (0, 20):
        total = total + numeros[n]
    return total

recorrer(numeros)
print(recorrer(numeros))



def calcular(total):
    prom = total / 20
    print(prom)
    
calcular(recorrer(numeros))
    
    


   