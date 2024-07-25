import os
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as st
import matplotlib.pyplot as plt

def test_normalidad(df_original):
    variables_normales = []
    for i in df_original.columns:
        if i in'State':
            continue
        if i == 'BodyFat' or i == 'Height' or i == 'Weight':
            result = st.normaltest(df_original[i])
            if result.pvalue > 0.001:
                variables_normales.append(i)
    print('Variables normales:')
    print("------------------------")
    for var in variables_normales:
        print(f"{var}: p-value = {result.pvalue}")
    print("------------------------\n")

    #grafico de normalidad con la curva de normalidad
    for i in variables_normales:
        plt.figure(figsize=(10,6))
        sns.histplot(df_original[i], kde=True, color='skyblue')
        mu, sigma = st.norm.fit(df_original[i])
        x = np.linspace(df_original[i].min(), df_original[i].max(), 100)
        p = st.norm.pdf(x, mu, sigma)
        plt.plot(x, p, 'k', linewidth=2)
        plt.title(f'Distribución de {i} con curva de normalidad')
        plt.xlabel(i)
        plt.ylabel('Frecuencia')
        plt.show()
        plt.close()
    
    
def test_independencia(df_original):
    variables_independientes = []
    for i in df_original.columns:
        if i == 'State':
            continue
        if i == 'BodyFat' or i == 'Height' or i == 'Weight':
            for j in df_original.columns:
                if j == 'State':
                    continue
                if i == j:
                    continue
                if j == 'BodyFat' or j == 'Height' or j == 'Weight':
                    result = st.pearsonr(df_original[i], df_original[j])
                    if result.pvalue > 0.001:   # type: ignore
                        variables_independientes.append((i, j, "%.3f" % result.pvalue)) # type: ignore
    print('Variables independientes:')
    print("------------------------")
    for var in variables_independientes:
        print(f"{var[0]} vs {var[1]}: p-value = {var[2]}")
    print("------------------------\n")

    
def test_homogeneidad(df_original):
    variables_homogeneas = []
    for i in df_original.columns:
        if i == 'State':
            continue
        if i == 'BodyFat' or i == 'Height' or i == 'Weight':
            for j in df_original.columns:
                if j == 'State':
                    continue
                if i == j:
                    continue
                if j == 'BodyFat' or j == 'Height' or j == 'Weight':
                    result = st.levene(df_original[i], df_original[j])
                    if result.pvalue > 0.001:
                        variables_homogeneas.append((i, j, "%.3f" % result.pvalue))
    print('Variables homogeneas:')
    print("------------------------")
    for var in variables_homogeneas:
        print(f"{var[0]} vs {var[1]}: p-value = {var[2]}")
    print("------------------------\n")

def menu ():
    print("----Menu PNP----")
    print("1. Test de normalidad")
    print("2. Test de independencia")
    print("3. Test de homogeneidad")
    print("4. Salir")
    print("----------------")
    op = int(input("Ingrese el numero de la prueba a realizar: "))
    return op

def main(df_original):
    opcion = 0
    while opcion != 4:
        opcion = menu()
        if opcion == 1:
            os.system('cls')
            test_normalidad(df_original)
        elif opcion == 2:
            os.system('cls')
            test_independencia(df_original)
        elif opcion == 3:
            os.system('cls')
            test_homogeneidad(df_original)
        elif opcion == 4:
            os.system('cls')
            print("Saliendo...")
        else:
            os.system('cls')
            print("Opción no válida")
