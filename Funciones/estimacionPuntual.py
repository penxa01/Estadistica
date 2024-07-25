import numpy as np

def ecm(estimador, valor_exacto):
    return np.var(estimador) + (valor_exacto - np.mean(estimador))**2

def main(df_original):
    # Calculamos los estimadores para la media
    
    estimador_x_raya = sum(df_original['BodyFat']) / len(df_original['BodyFat'])
    valor_exacto_media = df_original['BodyFat'].mean()
    
    ecm_x_raya = ecm([estimador_x_raya], valor_exacto_media)
    
    print("\n----Estimación Puntual para la Media----\n")
    print('Estimación X raya: {:.2f}'.format(estimador_x_raya))
    print('ECM X raya: {:.2f}'.format(ecm_x_raya))
    print('Valor exacto de la media: {:.2f}'.format(valor_exacto_media))
    print("------------------------")
    
    estimador_s2 = sum((df_original['BodyFat'] - valor_exacto_media)**2) / (len(df_original['BodyFat']) - 1)  
    valor_exacto_varianza = np.var(df_original['BodyFat'])
    
    ecm_s2 = ecm([estimador_s2],valor_exacto_varianza)
  
    print("\n----Estimación Puntual para la Varianza----\n")
    print('Estimación S^2: {:.2f}'.format(estimador_s2))
    print('ECM S^2: {:.2f}'.format(ecm_s2))
    print('Valor exacto de la varianza: {:.2f}'.format(valor_exacto_varianza))
    print('------------------------\n')

