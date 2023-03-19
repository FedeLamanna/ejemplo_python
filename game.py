from random import choice, randrange
from datetime import datetime

operators = ["+","-","*","/"]
times = 5
init_time = datetime.now()
print(f"Veremos cuanto tardas en responder estas {times} operaciones!")
correctos = 0
incorrectos = 0
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Tenemos en cuenta si el divisor es cero
    if ((operator == "/") and (number_2 == 0)):
        print("No se puede dividir por cero. Elegimos otros numeros")
    else:
        result = float(input("resultado: "))
        if (operator == "+"):
            if number_1 + number_2 == result:
                print("Correcto!!")
                correctos += 1 
            else:
                print("Incorrecto!!")
                incorrectos += 1
        elif (operator == "-"):
            if (number_1 - number_2 == result):
                print("Correcto!!")
                correctos += 1 
            else:
                print("Incorrecto!!")
                incorrectos += 1
        elif (operator == "*"):
            if (number_1 * number_2 == result):
                print("Correcto!!")
                correctos += 1 
            else:
                print("Incorrecto!!")
                incorrectos += 1
        elif (operator == "/"):
            if (number_1 / number_2 == result):
                print("Correcto!!")
                correctos += 1 
            else:
                print("Incorrecto!!")
                incorrectos += 1
    
        end_time = datetime.now()
total_time = end_time - init_time
print(f"\nTardaste {total_time.seconds} segundos.")
print(f"Resultados correctos: {correctos}")
print(f"Resultados incorrectos: {incorrectos}")
