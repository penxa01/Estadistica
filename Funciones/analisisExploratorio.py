import os
import math 
import numpy as np
import matplotlib.pyplot as plt

def describirDataSet(df_original):
    # Describimos el dataset
    print("\n\n------------------------")
    print("#Descripción del dataset:")
    print(df_original.describe())
    print("------------------------")
    print("#Información del dataset:")
    print(df_original.info())
    print("------------------------")
    print("#Traducido:")
    print("(1) Densidad corporal (Density) - cuantitativa continua")
    print("(2) Porcentaje de grasa corporal (Bodyfat) - cuantitativa continua")
    print("(3) Edad (age) - cuantitativa discreta")
    print("(4) Peso (weight) en libras - cuantitativa continua")
    print("(5) Altura (Height) en pulgadas - cuantitativa continua")
    print("(6) Circunferencia del cuello (neck) - cuantitativa continua")
    print("(7) Circunferencia del pecho (chest) - cuantitativa continua")
    print("(8) Circunferencia del abdomen (abdomen) - cuantitativa continua")
    print("(9) Circunferencia de la cadera (hip) - cuantitativa continua")
    print("(10) Circunferencia del muslo (thigh) - cuantitativa continua")
    print("(11) Circunferencia de la rodilla (knee) - cuantitativa continua")
    print("(12) Circunferencia del tobillo (ankle) - cuantitativa continua")
    print("(13) Circunferencia del bíceps extendido (bicep) - cuantitativa continua")
    print("(14) Circunferencia del antebrazo (forearm) - cuantitativa continua")
    print("(15) Circunferencia de la muñeca (wrist) - cuantitativa continua")
    print("(16) Estado donde vive la persona (State) - cualitativa nominal")
    print("------------------------\n\n")

def menuVariables():
    print("----Variables----")
    print("1. Bodyfat")
    print("2. Weight")
    print("3. Height")
    print("-----------------")
    var = int(input("Ingrese el numero de la variable a analizar: "))

    if var == 1:
        return "BodyFat"
    elif var == 2:
        return "Weight"
    elif var == 3:
        return "Height"

def descripcionVariable(df_original):
    # Describimos la variable
    variable = menuVariables()
    print(variable)
    print('Media:                ', df_original[variable].mean())
    print('Mediana:              ', df_original[variable].median())
    #sin salto de linea
    print('Moda/s:                 ', df_original[variable].mode().values.tolist())
    print('Varianza:             ', df_original[variable].var())
    print('Desviacion estandar:  ', df_original[variable].std())
    print('Coef. de variacion:   ', df_original[variable].std() / df_original[variable].mean())
    print('Maximo:               ', df_original[variable].max())
    print('Minimo:               ', df_original[variable].min())
    print('Rango:                ', df_original[variable].max() - df_original[variable].min())
    print('Coef. de asimetria:   ', df_original[variable].skew())
    print('Coef. de curtosis:    ', df_original[variable].kurtosis())
    print('P - 0.25:             ', df_original[variable].quantile(0.25))
    print('P - 0.50:             ', df_original[variable].quantile(0.5))
    print('P - 0.75:             ', df_original[variable].quantile(0.75))
    print()
    print('Frecuencia de valores:')
    print(df_original[variable].value_counts())
    print("------------------------")

def VisualizarVariables(df):
    plt.figure()
    plt.subplots_adjust(wspace=0.7)
    N = int(np.ceil(1 + 3.3 * math.log10(len(df))))
    
    #Histograma para el peso
    plt.subplot(131) 
    mediaW= df["Weight"].mean()
    A1 = round((df["Weight"].max() - df["Weight"].min())/N,1)
    binsW = np.arange(df["Weight"].min(),df["Weight"].max()+A1,A1)
    cuantilesW = np.percentile(df["Weight"],[25,75])
    plt.hist(df["Weight"],bins=binsW,edgecolor='black',color='lightgreen',linewidth=1.2)
    plt.axvline(mediaW,color= "red",linestyle="dashed",linewidth=2,label=f"μ={mediaW:.2f}") #Representa la media
    plt.axvline(df["Weight"].median(),color= "blue",linestyle="dashed",linewidth=2,label=f"Med={df["Weight"].median():.2f}") #Representa la mediana
    plt.axvline(mediaW + df["Weight"].std(),color= "yellow",linestyle="dashed",linewidth=2,label=f"μ+σ={mediaW + df["Weight"].std():.2f}") #Representa la desviación
    plt.axvline(mediaW - df["Weight"].std(),color= "yellow",linestyle="dashed",linewidth=2,label=f"μ-σ={mediaW - df["Weight"].std():.2f}")
    plt.axvline(cuantilesW[0],color="#6C6C6C",linestyle="dashed",linewidth=2,label=f"q1={cuantilesW[0]:.2f}")
    plt.axvline(cuantilesW[1],color="#6C6C6C",linestyle="dashed",linewidth=2,label=f"q3={cuantilesW[1]:.2f}")
    plt.xlabel("Peso (lbs)")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.legend()
    
    #Histograma para la altura
    plt.subplot(132)
    mediaH= df["Height"].mean()
    A2 = round((df["Height"].max() - df["Height"].min())/N,1)
    binsH = np.arange(df["Height"].min(),df["Height"].max()+A2,A2)
    cuantilesH = np.percentile(df["Height"],[25,75])
    plt.hist(df["Height"],bins=binsH,edgecolor='black',color='#ff1493',linewidth=1.2)
    plt.axvline(mediaH,color= "red",linestyle="dashed",linewidth=2,label=f"μ={mediaH:.2f}")
    plt.axvline(df["Height"].median(),color= "blue",linestyle="dashed",linewidth=2,label=f"Med={df["Height"].median():.2f}")
    plt.axvline(mediaH + df["Height"].std(),color= "yellow",linestyle="dashed",linewidth=2,label=f"μ+σ={mediaH + df["Height"].std():.2f}")
    plt.axvline(mediaH - df["Height"].std(),color= "yellow",linestyle="dashed",linewidth=2,label=f"μ-σ={mediaH - df["Height"].std():.2f}")
    plt.axvline(cuantilesH[0],color="#6C6C6C",linestyle="dashed",linewidth=2,label=f"q1={cuantilesH[0]:.2f}")
    plt.axvline(cuantilesH[1],color="#6C6C6C",linestyle="dashed",linewidth=2,label=f"q3={cuantilesH[1]:.2f}")
    plt.xlabel("Altura (in)")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.legend()
    
    #Histograma para la grasa corporal
    plt.subplot(133)
    mediaBF= df["BodyFat"].mean()
    A3 = round((df["BodyFat"].max() - df["BodyFat"].min())/N,1)
    binsBF = np.arange(df["BodyFat"].min(),df["BodyFat"].max()+A3,A3)
    cuantilesBF = np.percentile(df["BodyFat"],[25,75])
    plt.hist(df["BodyFat"],bins=binsBF,edgecolor='black',color='skyblue',linewidth=1.2)
    plt.axvline(mediaBF,color= "red",linestyle="dashed",linewidth=2,label=f"μ={mediaBF:.2f}")
    plt.axvline(df["BodyFat"].median(),color= "blue",linestyle="dashed",linewidth=2,label=f"Med={df["BodyFat"].median():.2f}")
    plt.axvline(mediaBF + df["BodyFat"].std(),color= "yellow",linestyle="dashed",linewidth=2,label=f"μ+σ={mediaBF + df["BodyFat"].std():.2f}")
    plt.axvline(mediaBF - df["BodyFat"].std(),color= "yellow",linestyle="dashed",linewidth=2,label=f"μ-σ={mediaBF - df["BodyFat"].std():.2f}")
    plt.axvline(cuantilesBF[0],color="#6C6C6C",linestyle="dashed",linewidth=2,label=f"q1={cuantilesBF[0]:.2f}")
    plt.axvline(cuantilesBF[1],color="#6C6C6C",linestyle="dashed",linewidth=2,label=f"q3={cuantilesBF[1]:.2f}")
    plt.xlabel("Porcentaje de grasa corporal")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.legend()
    
    #histograma de torta para el estado
    plt.figure(134)
    plt.pie(df["State"].value_counts(),labels=df["State"].value_counts().index,autopct="%1.1f%%",startangle=90)
    plt.axis("equal")
    plt.title("Distribución de estados")
    
    plt.show()
    plt.close()

def coef_Correlacion(df_original):
    print("------------------------")
    print("Coeficiente de correlación de las variables Bodyfat y Weight")
    # Coeficiente de correlación
    print('Coeficiente de correlacion: ', df_original.BodyFat.corr(df_original.Weight))
    print("------------------------")

def menu():
    print("----Menu de A.E.----")
    print("1. Descripción del dataset")
    print("2. Descripción de variable")
    print("3. Coeficiente de correlación a eleccion nuestra")
    print("4. Visualizar variables")
    print("5. Salir")
    print("--------------------")
    opcion = int(input("Ingrese el numero de la opción: "))
    return opcion

def main(df_original):
    os.system('cls')
    opcion = 0
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            os.system('cls')
            describirDataSet(df_original)
        elif opcion == 2:
            os.system('cls')
            descripcionVariable(df_original)
        elif opcion == 3:
            os.system('cls')
            coef_Correlacion(df_original)
        elif opcion == 4:
            os.system('cls')
            VisualizarVariables(df_original)
        elif opcion == 5:
            os.system('cls')
            print("Saliendo...")
        else:
            os.system('cls')
            print("Opción incorrecta, intente nuevamente")

