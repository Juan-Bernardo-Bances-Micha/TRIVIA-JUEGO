print("Bienvenido a mi trivia para ver cuanto sabes de cultura general")

nombre = input("Ingresa tu nombre: ")

puntaje = 0

print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
)

print("tienes", puntaje, "puntos")


# Pregunta 1
print("\n 1) ¿Cuántos litros de sangre tiene una persona adulta?")
print("      a) Tiene entre 2 y 4 litros ")
print("      b) Tiene entre 4 y 6 litros ")
print("      c) Tiene 10 litros")
print("      d) Tiene 7 litros")
print("      e) Tiene 0,5 litros")

respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1 == "a":
  print("Incorrecto!", nombre, "Una persona adulta tiene entre 4 y 6 litros de sangre 😪😞😭")
elif respuesta_1 == "c":
  print("Incorrecto!", nombre, "Una persona adulta no tiene entre 4 y 6 litros de sangre 😪😞😭")
elif respuesta_1 == "d":
  print("Incorrecto!", nombre, "Una persona adulta no tiene entre 4 y 6 litros de sangre 😪😞😭")
elif respuesta_1 == "e":
  print("Incorrecto!", nombre, "Una persona adulta no tiene entre 4 y 6 litros de sangre 😪😞😭")
else:
  puntaje += 10
  
  print("Muy bien", nombre, "!","😁👍😜")


#pregunta 2
print("\n 2) ¿Quién es el autor de la frase Pienso, luego existo?")
print("      a)  Platón")
print("      b)  Galileo Galilei")
print("      c)  Descartes")
print("      d)  Sócrates")
print("      e)  Francis Bacon")

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_2 == "a":
  print("Incorrecto!", nombre, "Platón dijo: La mayor declaración de amor es la que no se hace; el hombre que siente mucho, habla poco. 😪😞😭")
elif respuesta_2 == "b":
  print("Incorrecto!", nombre, "Galileo Galilei dijo: No puedes enseñar nada a un hombre, pero puedes ayudarle a descubrirlo por sí mismo. 😪😞😭")
elif respuesta_2 == "d":
  print("Incorrecto!", nombre, "Sócrates dijo: Solo sé que no sé nada 😪😞😭")
elif respuesta_2 == "e":
  print("Incorrecto!", nombre, "Francis Bacon dijo: Vengándose, uno se iguala a su enemigo; perdonándolo, se muestra superior a él. 😪😞😭")
else:
  print("Muy bien", nombre, "!","😁👍😜")
 

#pregunta 3
print("\n 3) ¿Cuál es el país más grande y el más pequeño del mundo?")
print("      a)  Rusia y Vaticano")
print("      b)  China y Nauru")
print("      c)  Canadá y Mónaco")
print("      d)  Estados Unidos y Malta")
print("      e)  India y San Marino")

respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "b":
  print("Incorrecto!", nombre, "Rusia es el país mas grande del mundo con un área de 17 millones de km2, mientras el Vaticano tiene apenas 0,44 km2. 😪😞😭")
elif respuesta_3 == "c":
  print("Incorrecto!", nombre, "Rusia es el país mas grande del mundo con un área de 17 millones de km2, mientras el Vaticano tiene apenas 0,44 km2. 😪😞😭")
elif respuesta_3 == "d":
  print("Incorrecto!", nombre, "Rusia es el país mas grande del mundo con un área de 17 millones de km2, mientras el Vaticano tiene apenas 0,44 km2. 😪😞😭")
elif respuesta_3 == "e":
  print("Incorrecto!", nombre, "Rusia es el país mas grande del mundo con un área de 17 millones de km2, mientras el Vaticano tiene apenas 0,44 km2. 😪😞😭")
else:
  print("Muy bien", nombre, "!","😁👍😜")


#pregunta 4

print("\n  4) ¿Cuántos decimales tiene el número pi π?")

print("        a) Dos")
print("        b) Cien")
print("        c) Infinitos")
print("        d) Mil")
print("        e) Veinte")

respuesta_4 = input("\nTu respuesta: ")

while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input(
        "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_4 == "a":
  print("Incorrecto!", nombre, "A lo largo del tiempo, varios estudiosos se han dedicado a calcular el número π y aún no han llegado al final. Para el 2019 se habían calculado más de 31 billones de decimales. 😪😞😭")
elif respuesta_4 == "b":
  print("Incorrecto!", nombre, "A lo largo del tiempo, varios estudiosos se han dedicado a calcular el número π y aún no han llegado al final. Para el 2019 se habían calculado más de 31 billones de decimales. 😪😞😭")
elif respuesta_4 == "d":
  print("Incorrecto!", nombre, "A lo largo del tiempo, varios estudiosos se han dedicado a calcular el número π y aún no han llegado al final. Para el 2019 se habían calculado más de 31 billones de decimales. 😪😞😭")
elif respuesta_4 == "e":
  print("Incorrecto!", nombre, "A lo largo del tiempo, varios estudiosos se han dedicado a calcular el número π y aún no han llegado al final. Para el 2019 se habían calculado más de 31 billones de decimales. 😪😞😭")
else:
  print("Muy bien", nombre, "!","😁👍😜")