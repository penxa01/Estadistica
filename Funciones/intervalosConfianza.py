import numpy as np
import scipy.stats as st 
import matplotlib.pyplot as plt

def intervalos_confianza(df_original):
    # Extraemos los datos de la columna 'BodyFat'
    datos = df_original['BodyFat']
    # Calculamos la media, la desviación estándar y definimos la signifacion 
    alpha = 0.05
    media_muestral = np.mean(datos)
    varianza_muestral = np.var(datos)
    desviacion_muestral = np.std(datos, ddof=1)  # ddof=1 para obtener la desviación estándar muestral
    
    # Tamaño de la muestra
    n = len(datos)

    # Valor crítico de Z
    z_critico = st.norm.ppf(1 - alpha/2)
    
    # Error estándar
    error_estandar = desviacion_muestral / np.sqrt(n)
    
    # Intervalo de confianza
    margen_error = z_critico * error_estandar
    intervalo = (media_muestral - margen_error, media_muestral + margen_error)
    
    print(f"Intervalo de confianza para la media con un nivel de confianza del {(1-alpha)*100}%:")
    print(f"Media muestral: {media_muestral:.2f}")
    print(f"Desviación estándar muestral: {desviacion_muestral:.2f}")
    print(f"Tamaño de la muestra: {n}")
    print(f"Valor crítico de Z: {z_critico:.2f}")
    print(f"Margen de error: {margen_error:.2f}")
    print(f"Intervalo de confianza para la media:({intervalo[0]:.2f} <μ< {intervalo[1]:.2f})")
    print('-------------------------------')

    #Gráfico intervalo de confianza para la media muestral    
    plt.figure(figsize=(10,6))
    
    mu, sigma = st.norm.fit(datos)
    x = np.linspace(datos.min(), datos.max(), 100)
    p = st.norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'k', linewidth=2, label='Curva de Normalidad')

    plt.axvline(media_muestral, color='b', linestyle='dashed', linewidth=2, label=f'Media(μ): {media_muestral:.2f}')
    plt.axvline(intervalo[0], color='r', linestyle='dashed', linewidth=2, label=f'Limite Inferior: {intervalo[0]:.2f}')
    plt.axvline(intervalo[1], color='r', linestyle='dashed', linewidth=2, label=f'Limite Superior: {intervalo[1]:.2f}')

    plt.title('Intervalo de Confianza para la Media Muestral')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()
    

    # Valor crítico de Chi-cuadrado
    chi2_critico_inf = st.chi2.ppf(alpha/2, n-1)
    chi2_critico_sup = st.chi2.ppf(1 - alpha/2, n-1)
    
    # Intervalo de confianza
    limite_inf = ((n-1) * varianza_muestral)/ chi2_critico_sup
    limite_sup = ((n-1) * varianza_muestral)/ chi2_critico_inf
    intervalo_varianza = (limite_inf, limite_sup)

    print(f"Intervalo de confianza para la varianza con un nivel de confianza del {(1-alpha)*100}%:")
    print(f"Varianza muestral: {varianza_muestral:.2f}")
    print(f"Valor crítico de Chi-cuadrado (inferior): {chi2_critico_inf:.2f}")
    print(f"Valor crítico de Chi-cuadrado (superior): {chi2_critico_sup:.2f}")
    print(f"Margen de error (inferior): {limite_inf:.2f}")
    print(f"Margen de error (superior): {limite_sup:.2f}")
    print(f"Intervalo de confianza para la varianza:({intervalo_varianza[0]:.2f} <σ²< {intervalo_varianza[1]:.2f})")
    print('-------------------------------')

    #Gráfico intervalo de confianza para la varianza muestral
    plt.figure(figsize=(10,6))

    # Valores de la chi-cuadrado para graficar
    x = np.linspace(0, chi2_critico_sup * 1.1, 1000)
    y = st.chi2.pdf(x, n - 1)
    

    plt.plot(x, y, label=f'Chi-cuadrado (df={n-1})')
    plt.axvline(varianza_muestral, color='b', linestyle='dashed', linewidth=2, label=f'Varianza(σ²): {varianza_muestral:.2f}') #type: ignore
    plt.axvline(intervalo_varianza[0], color='r', linestyle='dashed', linewidth=2, label=f'Limite Inferior: {intervalo_varianza[0]:.2f}') #type: ignore
    plt.axvline(intervalo_varianza[1], color='r', linestyle='dashed', linewidth=2, label=f'Limite superior: {intervalo_varianza[1]:.2f}') #type: ignore

    plt.title('Curva Chi-cuadrado y Intervalo de Confianza para la Varianza')
    plt.xlabel('Valor Chi-cuadrado')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()
    plt.show()

def main(df_original):
    print("\n----Intervalos de Confianza----\n")
    intervalos_confianza(df_original)
    print("\n")