import time

def math_functions():
    print ("a ver, amos a hacer algo más interesante...")
    time.sleep(1)
    print ("""Esta es una sección matemática con operaciones básicas,
       escoge alguna de las opciones mostradas a continuación
       seleccionando el número correspondiente a la operación
       que deseas calcular""")
    time.sleep(1)
    
    print("""estas son tus opciones:
                    0 = Suma                     X = A + B

                    1 = Resta                    X = A - B

                    2 = Multiplicación           X = A * B

                    3 = División                 X = A / B

                    4 = Exponente                X = A ^ B""")
    menu_operaciones = int (input("opcion: "))


    #SUMA
    if menu_operaciones == 0:
        print("escogiste SUMA")
        print ("introduce el valor de A, mijo ")
        A = int ( input("A: "))
        print ( A , "arre")
        time.sleep(1)

        print ("ahora el valor de B, mijo")
        B = int ( input("B: "))
        print ( B , "arre")
        time.sleep(1)

        print ("bueno, según las matemáticas el resultado de X es :")
        time.sleep(1)       
        X = A + B
        print (X)
        print ("porque X =",A, "+", B)
        print ("por lo tanto X = ",X)
        time.sleep(1)


    #RESTA
    elif menu_operaciones == 1:
        
        print("escogiste RESTA")
        print ("introduce el valor de A, mijo ")
        A = int ( input("A: "))
        print ( A , "arre")
        time.sleep(1)

        print ("ahora el valor de B, mijo")
        B = int ( input("B: "))
        print ( B , "arre")
        time.sleep(1)

        print ("bueno, según las matemáticas el resultado de X es :")
        time.sleep(1)       
        X = A - B
        print (X)
        print ("porque X =",A, "-", B)
        print ("por lo tanto X = ",X)
        time.sleep(1)

    #MULTIPLICACION
    elif menu_operaciones == 2:
        
        print("escogiste MULTIPLICACIÓN")
        print ("introduce el valor de A, mijo ")
        A = int ( input("A: "))
        print ( A , "arre")
        time.sleep(1)

        print ("ahora el valor de B, mijo")
        B = int ( input("B: "))
        print ( B , "arre")
        time.sleep(1)

        print ("bueno, según las matemáticas el resultado de X es :")
        time.sleep(1)       
        X = A * B
        print (X)
        print ("porque X =",A, "*", B)
        print ("por lo tanto X = ",X)
        time.sleep(1)

    #DIVISIÓN
    elif menu_operaciones == 3:
        
        print("escogiste DIVISIÓN")
        print ("introduce el valor de A, mijo ")
        A = int ( input("A: "))
        print ( A , "arre")
        time.sleep(1)

        print ("ahora el valor de B, mijo")
        B = int ( input("B: "))
        print ( B , "arre")
        time.sleep(1)

        print ("bueno, según las matemáticas el resultado de X es :")
        time.sleep(1)       
        X = A / B
        print (X)
        print ("porque X =",A, "/", B)
        print ("por lo tanto X = ",X)
        time.sleep(1)


    #EXPONENTE
    elif menu_operaciones == 4:
        
        print("escogiste EXPONENTE")
        print ("introduce el valor de A, mijo ")
        A = int ( input("A: "))
        print ( A , "arre")
        time.sleep(1)

        print ("ahora el valor de B, mijo")
        B = int ( input("B: "))
        print ( B , "arre")
        time.sleep(1)

        print ("bueno, según las matemáticas el resultado de X es :")
        time.sleep(1)       
        X = A ** B
        print (X)
        print ("porque X =",A, "^", B)
        print ("por lo tanto X = ",X)
        time.sleep(1)
    print ("tas de acuerdo?")

#INTRODUCCIÓN

nombre = input(" Hola, introduce tu nombre, carnal: ")
time.sleep(1)
print ("tu nombre es:", nombre, " vedaaa?")
time.sleep(1)

confirmacion_1 = int (input("YES = 1     NEL = 0: "))
if confirmacion_1 == 1 :
    print("1=YES, arre")
    time.sleep(1)
else:
    print("cómo jijos no, we...? tas chavo a webo que sí te llamas ", nombre)
    time.sleep(1)
    print("seguimos")
    time.sleep(2)

                  
    
print ("ahora tu edad, brody")
time.sleep(1)
print ("cámara...")
time.sleep(1)
print ("ora sí,")


edad = int ( input ( "aquí tu age, vato: "))
if edad >90 :
    print("no manche, cómo vas a tener", edad, "años, we")
    edad = int ( input ( "aquí tu age, WE, SIN MENTIRAS YA: "))
    if edad <90 :
        print ("eso mirrey!")

time.sleep(0.2)
print ("wacha...")
time.sleep(2)
print ("tienes ",  edad, "primaveras,  sí o no?")
time.sleep(1)

confirmacion_2 = int (input("YES = 1     NEL = 0: "))
if confirmacion_2 == 1:
    print("1=YES, eso campeón")
    time.sleep(1)
else: 
    print("cómo jijos no, we...? CÓMO JIJOS NOOO", nombre, "???")
    time.sleep(2)
    print(" PSHH! seguimos...")
    time.sleep(1)


print ("bueno...")
time.sleep(1)


math_functions()


confirmacion_3 = int (input("YES = 1   CONTINUAR EN SECCIÓN MATEMÁTICA = 2    SALIR DE SECCIÓN MATEMÁTICA = 0 "))
if confirmacion_3 == 1:
    print ("awebo que sí, mi nene")

elif confirmacion_3 == 2:
    print ("regresar a cálculo matemático")
    time.sleep(2)
    while confirmacion_3 == 2:
        math_functions()
        confirmacion_3 = int (input("YES = 1   CONTINUAR EN SECCIÓN MATEMÁTICA = 2    SALIR DE SECCIÓN MATEMÁTICA = 0 "))

    
    
elif confirmacion_3 == 0:
    print ("saliendo")
    
time.sleep(2)
print ("bueno ahí tamos, mi chavo. Sigue practicando, bye!")
time.sleep(1)
print ("cambio y fuera")
exit()       
    
       
       
