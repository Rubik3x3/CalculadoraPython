
#<<<------------------------->>>#
#<<<       Calculadora       >>>#
#<<<------------------------->>>#


#-----------------------#                        
#     Instrucciones:    #
#-----------------------#


#SUMA: Para sumar hay que ingresar el numero 1 o escribir la palabra "suma".

#RESTA: Para restar hay que ingresar el numero 2 o escribir la palabra "resta".

#MULTIPLICACION: Para multiplicar hay que ingresar el numero 3 o escribir la palabra "multiplicacion".

#DIVICION: Para dividir hay que ingresar el numero 4 o escribir la palabra "divicion".

#POTENCIACION: Para la potenciacion hay que ingresar el numero 5 o escribir la palabra "potenciacion".

#FACTORIAL: Para el factorial hay que ingresar el numero 6 o escribir la palabra "factorial". 


#NUMEROS_IGUALES_O_DIFERENTES: Para averiguar si un numero es igual o diferente hay que ingresar el numero 7 o escribir la palabra "iguales".


#-------------#
#  Variables  #
#-------------#


suma = 1

resta = 2

multiplicacion = 3

divicion = 4

potenciacion = 5

factorial = 6

iguales = 7


#-----------------#
#      Suma       #
#-----------------#


if input() == suma:

    print("Ingrese numero 1 de la suma:")
    num1_suma = input()

    print("Ingrese numero 2 de la suma:")
    num2_suma = input()

    resultado_suma = num1_suma + num2_suma

    print("El resultado de la suma es:", resultado_suma)


#-----------------#
#      Resta      #
#-----------------#


if input() == resta:

    print("Ingrese numero 1 de la resta")
    num1_resta = input()

    print("Ingrese numero 2 de la resta")
    num2_resta = input()

    resultado_resta = num1_resta - num2_resta

    print("El resultado de la resta es:", resultado_resta)


#--------------------------#
#      Multiplicacion      #
#--------------------------#


if input() == multiplicacion:
    print("Ingrese factor 1 de la multiplicacion")
    factor1_multiplicacion = input()

    print("Ingrese factor 2 de la multiplicacion")
    factor2_multiplicacion = input()

    producto_multiplicacion = factor1_multiplicacion * factor2_multiplicacion

    print("El producto de la multiplicacion es:", producto_multiplicacion)


#--------------------------#
#         Divicion         #
#--------------------------#

if input() == divicion:

    print("Ingrese dividendo de la divicion")
    dividendo_divicion = input()

    print("Ingrese divisor de la divicion")
    divisor_divicion = input()

    cociente_divicion = dividendo_divicion / divisor_divicion

    print("El cociente de la divicion es:", cociente_divicion)
    


#------------------------------#
#          Potenciacion        #
#------------------------------#

if input() == potenciacion:

    print("Ingrese la base de la potenciacion")
    base_potenciacion = input()

    print("Ingrese el exponente de la potenciacion")
    exponente_potenciacion = input()
    

    potencia_potenciacion = base_potenciacion ** exponente_potenciacion

    print("El resultado de la potenciacion es:", potencia_potenciacion)
    


#------------------------------#
#          Factorial           #
#------------------------------#

if input() == factorial:
    print("Ingrese numero:")
    numero_factorial = input()
    factorial = 1
    if int(numero_factorial) >= 1:
        for i in range (1,int(numero_factorial)+1):
            factorial = factorial * i
    print("El factorial es:")
    print(factorial)

#--------------------------------#
#  Numeros Iguales o Diferentes  #
#--------------------------------#

if input() == iguales:

    print("Ingrese numero 1:")
    num1_iguales = input()

    print("Ingrese numero 2:")
    num2_iguales = input()

    if num1_iguales == num2_iguales:
        
        print("Los numeros son Iguales")

    else:

        print("Los numeros son Diferentes")