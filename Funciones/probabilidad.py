import os 

def probabilidad_simple(df_original):
    print("#Prob. Simple:\n")
    personas_obesas = 0
    personas_altura = 0
    total_personas = len(df_original)
    for i in range(total_personas):
        #Consultar si esta bien, la probabilidad de que una persona sea Obesa se resuelve con probabilidad total
        if df_original['BodyFat'][i] > 25:
            personas_obesas += 1
        if df_original['Height'][i] > 70:
            personas_altura += 1
    print (f'Personas obesas: {personas_obesas}')
    print (f'Personas con una altura mayor a 70: {personas_altura}')
    prob_A = personas_obesas/total_personas
    prob_B = personas_altura/total_personas
    print('P(A) = %{}'.format(round(prob_A*100,2)))
    print('P(B) = %{}'.format(round(prob_B*100,2)))
    print("------------------------\n")
    return prob_A,prob_B

def probabilidad_interseccion(df_original):
    print("#Prob. Interseccion:\n")
    personas_obesas_altura = 0
    total_personas = len(df_original)

    for i in range(total_personas):
        if df_original['BodyFat'][i] > 25 and df_original['Height'][i] > 70:
            personas_obesas_altura += 1
    
    print (f'Personas obesas con una altura mayor a 70: {personas_obesas_altura}')
    prob_AnB = personas_obesas_altura/total_personas
    print('P(AnB) = %{}'.format(round(prob_AnB*100,2)))
    print("------------------------\n")
    return prob_AnB

def probabilidad_condicionada(df_original):
    personas_obesas = 0
    personas_altura = 0
    personas_obesas_altura = 0
    total_personas = len(df_original)

    for i in range(total_personas):
        #Consultar si esta bien, la probabilidad de que una persona sea Obesa se resuelve con probabilidad total
        if df_original['BodyFat'][i] > 25:
            personas_obesas += 1
        if df_original['Height'][i] > 70:
            personas_altura += 1
    
    for i in range(total_personas):
        if df_original['BodyFat'][i] > 25 and df_original['Height'][i] > 70:
            personas_obesas_altura += 1

    pA = personas_obesas/total_personas
    pB = personas_altura/total_personas
    pAnB = personas_obesas_altura/total_personas

    print("#Prob. Condicionada:\n")
    print('La probabilidad de que una persona sea obesa dado que tiene una altura superior a 70 es de %{:.2f}'.format((pAnB/pB)*100))
    print('La probabilidad de que una persona tenga una altura superior a 70 in dado que es obeso es de %{:.2f}'.format((pAnB/pA)*100))
    print("------------------------\n")
    
def probabilidad_total(df_original):
    total_personas = len(df_original)
    #Calculo de probabilidades simples
    personas_california = 0
    personas_idaho = 0
    personas_oregon = 0
    personas_nevada = 0
    personas_washington = 0
    for i in range(total_personas):
        if df_original['State'][i] == 'California':
            personas_california += 1
        elif df_original['State'][i] == 'Idaho':
            personas_idaho += 1
        elif df_original['State'][i] == 'Oregon':
            personas_oregon += 1
        elif df_original['State'][i] == 'Nevada':
            personas_nevada += 1
        elif df_original['State'][i] == 'Washington':
            personas_washington += 1
    prob_california = personas_california/total_personas
    prob_idaho = personas_idaho/total_personas
    prob_oregon = personas_oregon/total_personas
    prob_nevada = personas_nevada/total_personas
    prob_washington = personas_washington/total_personas
    #Calculo de probabilidades conjunta
    personas_obesas_california = 0
    personas_obesas_idaho = 0
    personas_obesas_oregon = 0
    personas_obesas_nevada = 0
    personas_obesas_washington = 0
    for i in range(total_personas):
        if df_original['State'][i] == 'California' and df_original['BodyFat'][i] > 25:
            personas_obesas_california += 1
        elif df_original['State'][i] == 'Idaho' and df_original['BodyFat'][i] > 25:
            personas_obesas_idaho += 1
        elif df_original['State'][i] == 'Oregon' and df_original['BodyFat'][i] > 25:
            personas_obesas_oregon += 1
        elif df_original['State'][i] == 'Nevada' and df_original['BodyFat'][i] > 25:
            personas_obesas_nevada += 1
        elif df_original['State'][i] == 'Washington' and df_original['BodyFat'][i] > 25:
            personas_obesas_washington += 1
    prob_OnC = personas_obesas_california/total_personas
    prob_OnI = personas_obesas_idaho/total_personas
    prob_OnO = personas_obesas_oregon/total_personas
    prob_OnN = personas_obesas_nevada/total_personas
    prob_OnW = personas_obesas_washington/total_personas
    #Calculo de probabilidad condicionada
    prob_OC = prob_OnC/prob_california
    prob_OI = prob_OnI/prob_idaho
    prob_OO = prob_OnO/prob_oregon
    prob_ON = prob_OnN/prob_nevada
    prob_OW = prob_OnW/prob_washington
    prob_total_A = (prob_OC*prob_california) + (prob_OI*prob_idaho) + (prob_OO*prob_oregon) + (prob_ON*prob_nevada) + (prob_OW*prob_washington)
    print("#Prob. Total:\n")
    print('La probabilidad total de que las personas sean obesas es de %{:.2f}'.format(round(prob_total_A*100,2)))
    print("------------------------\n")

def menu():
    print("----------Menú de Probabilidad----------")
    print("1: Probabilidad Simple")
    print("2: Probabilidad Interseccion")
    print("3: Probabilidad Condicionada")
    print("4: Probabilidad Total")
    print("5: Salir")
    print("------------------------------------")
    op = int(input("Ingrese la opción deseada: "))
    return op

def main(df_original):
    os.system('cls')

    opcion = 0
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            os.system('cls')
            probabilidad_simple(df_original)
        elif opcion == 2:
            os.system('cls')
            probabilidad_interseccion(df_original)
        elif opcion == 3:
            os.system('cls')
            probabilidad_condicionada(df_original)
        elif opcion == 4:
            os.system('cls')
            probabilidad_total(df_original)
        elif opcion == 5:
            os.system('cls')
            print("Saliendo...")
        else:
            os.system('cls')
            print("Opción no válida")