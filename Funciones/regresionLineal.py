import os
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as st
import matplotlib.pyplot as plt

def regresion_lineal_simple(df_original):
    # Aplicamos regresión lineal simple a las variables 'BodyFat' y 'Weight'
    x = df_original['Weight']
    y = df_original['BodyFat']
    
    pendiente, ordenada, r_value, p_value, std_err = st.linregress(x, y)
    r_squared = r_value**2 #type: ignore
    print('Regresión Lineal Simple:')
    print("------------------------")
    print(f"Pendiente: {pendiente:.2f}")
    print(f"Ordenada: {ordenada:.2f}")
    print(f"Coeficiente de correlación: {r_value:.2f}")
    print(f"Coeficiente de determinación: {r_squared:.2f}")
    print(f"Error estándar: {std_err:.2f}")
    print(f"y= {pendiente:.2f}x + ({ordenada:.2f}) ± {std_err:.2f}")
    print("------------------------\n")

    # Graficamos la regresión lineal simple junto con el r_value y el std_err
    plt.scatter(x, y, color='blue', label='Datos')
    plt.plot(x, pendiente*x + ordenada, color='red', label='Regresión Lineal')
    plt.xlabel('Peso (lbs)')
    plt.ylabel('Porcentaje de grasa corporal')
    plt.legend()
    plt.annotate(f"r_value: {r_value:.2f}", (0.05, 0.05), xycoords='axes fraction')
    plt.annotate(f"std_err: {std_err:.2f}", (0.05, 0.85), xycoords='axes fraction')
    plt.show()
    plt.close()
    return pendiente, ordenada

def analizar_residuos(df_original):
    x = df_original['Weight']
    y = df_original['BodyFat']
    pendiente, ordenada = st.linregress(x, y)[:2]
    residuos = y - (pendiente * x + ordenada)

    plt.figure(figsize=(10, 5))
    plt.scatter(x, residuos)
    plt.hlines(y=0, xmin=x.min(), xmax=x.max(), colors='red', linestyles='dashed')
    plt.xlabel('Peso (lbs)')
    plt.ylabel('Residuos')
    plt.title('Análisis de Residuos')
    plt.show()
    plt.close()


def menu():
    print("------Menú de RL------")
    print("1: Regresión Lineal Simple")
    print("2: Análisis de Residuos")
    print("3: Salir")
    print("----------------------")
    op = int(input("Ingrese la opción deseada: "))
    return op

def main(df_original):
    os.system('cls')
    opcion = 0
    while opcion != 3:
        opcion = menu()
        if opcion == 1:
            os.system('cls')
            regresion_lineal_simple(df_original)
        elif opcion == 2:
            os.system('cls')
            analizar_residuos(df_original)
        elif opcion == 3:
            os.system('cls')
            print("Saliendo...")
        else:
            os.system('cls')
            print("Opción no válida")