import os
import pandas as pd

import Funciones.analisisExploratorio as ae
import Funciones.probabilidad as prob
import Funciones.estimacionPuntual as ep
import Funciones.intervalosConfianza as ic
import Funciones.testHipotesis as th
import Funciones.pruebasNoParametricas as pnp
import Funciones.regresionLineal as rl

def CargarDataSet():
    data = pd.read_csv('CSV/BodyFat.csv')
    return data

def menu():
    print("----------Menú de opciones----------")
    print("1: Análisis Exploratorio de Datos")
    print("2: Probabilidad")
    print("3: Estimación Puntual")
    print("4: Intervalos de Confianza")
    print("5: Test de Hipótesis parametricos")
    print("6: Pruebas no paramétricas")
    print("7: Regresión Lineal Simple")
    print("8: Salir")
    print("------------------------------------")
    op = int(input("Ingrese la opción deseada: "))
    return op

if __name__ == "__main__":
    os.system('cls')
    op = 0

    df_original = CargarDataSet()

    while op != 8:
        op = menu()
        
        if op == 1:
            os.system('cls')
            ae.main(df_original)

        elif op == 2:
            os.system('cls')
            prob.main(df_original)

        elif op == 3:
            os.system('cls')
            ep.main(df_original)
        
        elif op == 4:
            os.system('cls')
            ic.main(df_original)
        
        elif op == 5:
            os.system('cls')
            th.main(df_original)

        elif op == 6:
            os.system('cls')
            pnp.main(df_original)
        
        elif op == 7:
            os.system('cls')
            rl.main(df_original)
        
        elif op == 8:
            os.system('cls')
            print("\n\nGracias por todo Profes :)\n\n")