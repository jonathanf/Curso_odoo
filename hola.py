#
# Este es mi segundo programa en python
# los comentarios van despues del simbolo #
# 

# Convierto la entrada de raw_input a float,
# raw_input siempre me da un str.
a = float( raw_input("Primero: ") )
b = float( raw_input("Segundo: ") )
resultado = 0.0

op = raw_input("Que operacion quieres realizar (\"+\", \"-\", \"*\", \"/\"): ")

if op == '+':
    resultado = a + b
elif op == '-':
    resultado = a - b
elif op == '*':
    resultado = a * b
elif op == '/':
    # Capturo el error ZeroDivisionError
    try:
        resultado = a / b
    except ZeroDivisionError:
        print "No puedo dividir para 0 (cero)"
else:
    print "No existe esa opcion!!!"

print "El resultado es: " + str(resultado)
raw_input("Presiona cualquier tecla para salir...")
