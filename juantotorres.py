from os import system

print("Hola soy juan torres")

while True:
    system("C:/Program Files/Google/Chorme/Application/chorme.exe")
    producto = 1
    
    
while True:
    num = input("Ingrese un número para multiplicar (o presione 'q' para salir): ")
    if num == 'q':
        break
    producto *= float(num)
print("El producto de los números ingresados es:", producto)