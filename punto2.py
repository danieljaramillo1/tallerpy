from time import altzone


def recibir():

    ancho=int(input(f'ingrese el ancho: '))
    alto=int(input(f'ingrese el alto: '))
    datos=[ancho,alto]
    return datos

datos=recibir()
print(datos)

def calcular(ancho,alto):
    area=ancho*alto
    print(f'el total es {area}')

calcular(datos[0],datos[1])   

def graficar(ancho,alto):
    for m in range (0,alto):
        print(ancho*'*')

graficar(datos[0],datos[1])
