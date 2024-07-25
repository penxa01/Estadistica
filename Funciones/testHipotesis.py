import os
import numpy as np
import scipy.stats as st

def test_hipotesis_media1(df_original):
    # Test de hipótesis para la media
    print("Test de hipótesis para la media:\n")
    print("H0: μ = 20 vs H1: μ < 20")
    # Extraemos los datos de la columna 'BodyFat'
    datos = df_original['BodyFat']
    # Calculamos la media, la desviación estándar y definimos la signifacion
    media_muestral = np.mean(datos)
    varianza_muestral = np.var(datos)
    desviacion_muestral = np.std(datos, ddof=1)  # ddof=1 para obtener la desviación estándar muestral
    n = len(datos)
    alpha = 0.05
    # Definimos la hipótesis nula y la hipótesis alternativa
    # H0: μ = 20
    # H1: μ < 20
    mu0 = 20
    # Calculamos el estadístico de prueba
    z = (media_muestral - mu0) / (desviacion_muestral / np.sqrt(n))
    # Calculamos el valor crítico
    z_critico = st.norm.ppf(alpha)
    # Calculamos el p-valor
    p_valor = st.norm.cdf(z)
    # Imprimimos los resultados
    print(f"Media muestral: {media_muestral:.2f}")
    print(f"Desviación estándar muestral: {desviacion_muestral:.2f}")
    print(f"Tamaño de la muestra: {n}")
    print(f"Valor crítico: {z_critico:.2f}")
    print(f"Estadístico de prueba: {z:.2f}")
    print(f"P-valor: {p_valor:.4f}")
    if p_valor < alpha:
        print("Rechazamos la H0")
    else:
        print("No rechazamos la H0")

    print("\n")

def test_hipotesis_media2(df_original):
    print("Test de hipótesis para la media:\n")
    print("H0: μ = 10 vs H1: μ > 10")
    # Extraemos los datos de la columna 'BodyFat'
    datos = df_original['BodyFat']
    # Calculamos la media, la desviación estándar y definimos la signifacion
    media_muestral = np.mean(datos)
    varianza_muestral = np.var(datos)
    desviacion_muestral = np.std(datos, ddof=1)  # ddof=1 para obtener la desviación estándar muestral
    n = len(datos)
    alpha = 0.05
    # Definimos la hipótesis nula y la hipótesis alternativa
    # H0: μ = 10
    # H1: μ > 10
    mu0 = 10
    # Calculamos el estadístico de prueba
    z = (media_muestral - mu0) / (desviacion_muestral / np.sqrt(n))
    # Calculamos el valor crítico
    z_critico = st.norm.ppf(1 - alpha)
    # Calculamos el p-valor
    p_valor = 1 - st.norm.cdf(z)
    # Imprimimos los resultados
    print(f"Media muestral: {media_muestral:.2f}")
    print(f"Desviación estándar muestral: {desviacion_muestral:.2f}")
    print(f"Tamaño de la muestra: {n}")
    print(f"Valor crítico: {z_critico:.2f}")
    print(f"Estadístico de prueba: {z:.2f}")
    print(f"P-valor: {p_valor:.4f}")
    if p_valor < alpha:
        print("Rechazamos la H0")
    else:
        print("No rechazamos la H0")

    print("\n")

def test_hipotesis_media3(df_original):
    print("Test de hipótesis para la media:\n")
    print("H0: μ = 15 vs H1: μ ≠ 15")
    # Extraemos los datos de la columna 'BodyFat'
    datos = df_original['BodyFat']
    # Calculamos la media, la desviación estándar y definimos la signifacion
    media_muestral = np.mean(datos)
    varianza_muestral = np.var(datos)
    desviacion_muestral = np.std(datos, ddof=1)  # ddof=1 para obtener la desviación estándar muestral
    n = len(datos)
    alpha = 0.05
    # Definimos la hipótesis nula y la hipótesis alternativa
    # H0: μ = 15
    # H1: μ ≠ 15
    mu0 = 15
    # Calculamos el estadístico de prueba
    z = (media_muestral - mu0) / (desviacion_muestral / np.sqrt(n))
    # Calculamos el valor crítico
    z_critico_inf = st.norm.ppf(alpha/2)
    z_critico_sup = st.norm.ppf(1 - alpha/2)
    # Calculamos el p-valor
    p_valor = 2 * (1 - st.norm.cdf(abs(z)))
    # Imprimimos los resultados
    print(f"Media muestral: {media_muestral:.2f}")
    print(f"Desviación estándar muestral: {desviacion_muestral:.2f}")
    print(f"Tamaño de la muestra: {n}")
    print(f"Valor crítico (inferior): {z_critico_inf:.2f}")
    print(f"Valor crítico (superior): {z_critico_sup:.2f}")
    print(f"Estadístico de prueba: {z:.2f}")
    print(f"P-valor: {p_valor:.4f}")
    if p_valor < alpha:
        print("Rechazamos la H0")
    else:
        print("No rechazamos la H0")
    
    print("\n")

def test_hipotesis_varianza(df_original):

    #Test de hipotesis para la varianza
    print("Test de hipótesis para la varianza:\n")
    print("H0: σ² = 20 vs H1: σ² > 20")
    # Extraemos los datos de la columna 'BodyFat'
    datos = df_original['BodyFat']
    # Calculamos la varianza muestral y definimos la signifacion
    varianza_muestral = np.var(datos)
    n = len(datos)
    alpha = 0.05
    # Definimos la hipótesis nula y la hipótesis alternativa
    # H0: σ² = 20
    # H1: σ² > 20
    sigma0 = 20
    # Calculamos el estadístico de prueba
    chi2 = (n-1) * varianza_muestral / sigma0
    # Calculamos el valor crítico
    chi2_critico = st.chi2.ppf(1 - alpha, n-1)
    # Calculamos el p-valor
    p_valor = 1 - st.chi2.cdf(chi2, n-1)
    # Imprimimos los resultados
    print(f"Varianza muestral: {varianza_muestral:.2f}")
    print(f"Valor crítico: {chi2_critico:.2f}")
    print(f"Estadístico de prueba: {chi2:.2f}")
    print(f"P-valor: {p_valor:.4f}")
    if p_valor < alpha:
        print("Rechazamos la H0")
    else:
        print("No rechazamos la H0")
    
    print("\n")

def menu():
    print("----Menu TH----")
    print("1. Test de hipótesis para la media (μ = 20)")
    print("2. Test de hipótesis para la media (μ = 10)")
    print("3. Test de hipótesis para la media (μ = 15)")
    print("4. Test de hipótesis para la varianza (σ² = 20)")
    print("5. Salir")
    print("---------------")
    op = int(input("Ingrese el numero de la hipótesis a analizar: "))
    return op
    
def main(df_original):
    opcion = 0
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            os.system('cls')
            test_hipotesis_media1(df_original)
        elif opcion == 2:
            os.system('cls')
            test_hipotesis_media2(df_original)
        elif opcion == 3:
            os.system('cls')
            test_hipotesis_media3(df_original)
        elif opcion == 4:
            os.system('cls')
            test_hipotesis_varianza(df_original)
        elif opcion == 5:
            os.system('cls')
            print("Saliendo...")
        else:
            os.system('cls')
            print("Opción incorrecta, intente nuevamente.")


