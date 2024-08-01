#lista(list)
frutas=["Tunas","Guanabana","Marucuya"]
numeroPrimos=[3,5,7,11]
print(type(frutas))
print(type(numeroPrimos))
print(frutas[0])
print(numeroPrimos[2])

frutas[0]="Mango"
print(frutas)

frutas.append("Lichi")
print(frutas)

numeroPrimos.append(13)
print(numeroPrimos)

#tupla
dimensiones = (1920,1080)
coordenadas = (10,20)
print(type(dimensiones))
print(type(coordenadas))
puntos=(10,20)
puntos[1]=30
#puntos[1]=30 #no se puede asignar a tupla un nuevo valor
#conjunto
colores={"rojo","azul","amarillo"}
numerosUnicos={"1,2,3"}
print(type(colores))
print(colores)
print(type(numerosUnicos))