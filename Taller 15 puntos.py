# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:10:00 2021

@author: LUIS AGUILAR
"""
import pandas as pd
import numpy as np
url = "Casos_positivos_de_COVID-19_en_Colombia.csv"
df = pd.read_csv(url)
df.loc[df['Tipo de contagio'] == 'Comunitario', 'Tipo de contagio'] = 'Comunitaria'
df.loc[df['Tipo de contagio'] == 'En Estudio', 'Tipo de contagio'] = 'En estudio'
df.loc[df['Recuperado'] == 'fallecido', 'Recuperado'] = 'Fallecido'
df.loc[df['Ubicación del caso'] == 'CASA', 'Ubicación del caso'] = 'Casa'    
df.loc[df['Ubicación del caso'] == 'casa', 'Ubicación del caso'] = 'Casa'
df.loc[df['Estado'] == 'leve', 'Estado'] = 'Leve'
df.loc[df['Estado'] == 'LEVE', 'Estado'] = 'Leve'
# Punto1
num = df['ID de caso'].size
print(f'El total de casos es : {num}')
# Punto3
num3 = pd.unique(df['Nombre municipio'])
print(f'Los municipios afectados son : {num3}')
# Punto4
num4 = df[df['Ubicación del caso']== 'Casa']
num4['Ubicación del caso'].value_counts()
# Punto5
num5 = df[df['Recuperado']== 'Recuperado']
num5['Recuperado'].value_counts()
# Punto6
num6 = df[df['Recuperado']== 'Fallecido']
num6['Recuperado'].value_counts()
# Punto7
df.groupby(['Tipo de contagio']).size().sort_values(ascending=False)
# Punto9
num9 = pd.unique(df['Nombre departamento'])
print(f'Los departamentos afectados son : {num9}')
# Punto10
df['Ubicación del caso'].value_counts().sort_values(ascending=False)
# Punto11
num11 = df[df['Estado']== 'Leve']
num11.groupby(['Nombre departamento', 'Estado']).size().head(10).sort_values(ascending=False)
# Punto12
num12 =df[df['Estado']== 'Fallecido']
num12.groupby(['Nombre departamento', 'Estado']).size().head(10).sort_values(ascending=False)
# Punto13
num13 =df[df['Recuperado']== 'Recuperado']
num13.groupby(['Nombre departamento', 'Recuperado']).size().head(10).sort_values(ascending=False)
# Punto14
num14 = df[df['Estado']== 'Leve']
num14.groupby(['Nombre municipio', 'Estado']).size().head(10).sort_values(ascending=False)
# Punto15
num15 =df[df['Estado']== 'Fallecido']
num15.groupby(['Nombre municipio', 'Estado']).size().head(10).sort_values(ascending=False)
# Punto32
df['Estado'].value_counts().sort_values(ascending=True).plot()
# Punto33
df['Sexo'].value_counts().sort_values(ascending=True).plot()