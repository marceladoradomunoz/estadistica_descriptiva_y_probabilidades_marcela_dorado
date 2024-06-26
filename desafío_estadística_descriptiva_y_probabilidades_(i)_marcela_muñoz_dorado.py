# -*- coding: utf-8 -*-
"""Desafío.Estadística.Descriptiva.y.Probabilidades.(I).Marcela.Muñoz.Dorado.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXHNFUnHp_b2z6-hAPqUEaKWeRCvjA45

# **DESAFÍO ESTADÍSTICA DESCRIPTIVA Y PROBABILIDADES(I).**
"""

#IMPORTACIÓN DE LIBRERÍAS
import pandas as pd
import numpy as np
import math as math
import matplotlib as mtlb
import matplotlib.pyplot as plt
import seaborn as sns

#IMPORTACIÓN DEL ARCHIVO DS_SALARIES.CSV

df_salaries = pd.read_csv('ds_salaries.csv')
df_salaries.head(1)

#INSPECCIÓN DEL ARCHIVO Y DE LOS TIPOS DE DATOS EN EL.

print(df_salaries.shape)
#print(df_salaries.info())
#print(df_salaries.isnull())
#print(df_salaries.notnull())

print(df_salaries.info())

print(df_salaries.isnull())

print(df_salaries.notnull())

print(df_salaries.isna())

print(df_salaries.columns)

#PREGUNTA 1: OBTENER EL PROMEDIO GENERAL DE LOS SALARIOS, DESVIACIÓN ESTÁNDAR, QUINTILES Y RANGO (UTILIZANDO FUNCIÓN DESCRIBE)

calculo = df_salaries['salary_in_usd'].describe()
print(calculo)

#PREGUNTA 1: OBTENER EL PROMEDIO GENERAL DE LOS SALARIOS, DESVIACIÓN ESTÁNDAR, QUINTILES Y RANGO (UTILIZANDO FUNCIONES PANDAS)

prom = df_salaries['salary_in_usd'].mean()                                       #Promedio.
des_estand = df_salaries['salary_in_usd'].std()                                  #Desviación estándar.
q_1 = df_salaries['salary_in_usd'].quantile(0.25)                                #primer quintil.
q_2 = df_salaries['salary_in_usd'].quantile(0.50)                                #segundo quintil.
q_3 = df_salaries['salary_in_usd'].quantile(0.75)                                #Tercer quintil.
max = df_salaries['salary_in_usd'].max()                                         #Máximo.
min = df_salaries['salary_in_usd'].min()                                         #Mínimo.
rang = df_salaries['salary_in_usd'].max() - df_salaries['salary_in_usd'].min()   #Rango.

print(prom)
print(des_estand)
print(q_1)
print(q_2)
print(q_3)
print(q_4)
print(max)
print(min)
print(rang)

#PREGUNTA 1: OBTENER EL PROMEDIOR GENERAL DE LOS SALARIOS, DESVIACIÓN ESTÁNDAR, QUINTILES Y RANGO (UTILIZANDO LIBRERÌA NUMPY)

promedio = np.mean(df_salaries['salary_in_usd'])                                    #Promedio.
desviacion_estandar = np.std(df_salaries['salary_in_usd'], ddof=1)                  #Desviación estándar.
quintil_1 = np.quantile(df_salaries['salary_in_usd'],0.20)                          #Primir quintil.
quintil_2 = np.quantile(df_salaries['salary_in_usd'],0.40)                          #Segundo quintil.
quintil_3 = np.quantile(df_salaries['salary_in_usd'],0.60)                          #Tercer quintil.
ma = np.max(df_salaries['salary_in_usd'])                                           #Màximo.
mi = np.min(df_salaries['salary_in_usd'])                                           #Medio.
rang = df_salaries['salary_in_usd'].max() - df_salaries['salary_in_usd'].min()      #Rango.

print(promedio)
print(desviacion_estandar)
print(quintil_1)
print(quintil_2)
print(quintil_3)
print(ma)
print(mi)
print(rang)

df_1 = df_us['job_title'].value_counts()
df_1
df_salaries.info()

df = df_salaries.loc[:,['salary_in_usd', 'experience_level', 'employment_type', 'remote_ratio']]
df = df[(df['salary_in_usd'] >= 0) & (df['experience_level'].isin(['MI', 'SE'])) & (df['employment_type'] == 'FT') & (df['remote_ratio'] >= 50)]
df

# @title salary_in_usd

from matplotlib import pyplot as plt
df['salary_in_usd'].plot(kind='hist', bins=20, title='salary_in_usd')
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title experience_level vs salary_in_usd

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(df['experience_level'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(df, x='salary_in_usd', y='experience_level', inner='box', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

df_1.dtypes

df_1 = df_salaries.loc[:, ['salary_in_usd', 'experience_level', 'company_size']]
df_2 = df_1[(df_1['salary_in_usd'] >= 0) & (df_1['experience_level'] == 'MI') & ((df_1['company_size'] == 'S') | (df_1['company_size'] == 'M'))]
df_2

df_2 = df_salaries[(df_1['salary_in_usd'] >= 0) & (df_1['experience_level'] == 'MI') & ((df_1['company_size'] == 'S') | (df_1['company_size'] == 'M'))]
df_test = df_2.loc[:, ['salary_in_usd', 'experience_level', 'company_size']]
media = df_2.mean()
mediana = df_2.median()
print(media)
print(mediana)
df_test

mean_salary = float(df_test['salary_in_usd'].mean())

sns.barplot(data=df_test, x='company_size', y='salary_in_usd', hue='experience_level')
plt.axvline(x=mean_salary, color='red')

salary_mean = df_c2['salary_in_usd'].mean()
salary_median = df_c2['salary_in_usd'].median()
sns.barplot(data=df_test, x='salary_in_usd', y='company_size', hue='experience_level')
plt.axvline(x=salary_mean, color='red', label='Mean Salary')

# @title company_size vs salary_in_usd

salary_mean = df_c2['salary_in_usd'].mean()
salary_median = df_c2['salary_in_usd'].median()

figsize = (12, 1.2 * len(df_test['company_size'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(df_test, x='salary_in_usd', y='company_size', inner='box', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)
plt.axvline(x=salary_mean, color='red', linestyle='--', label='Mean')
plt.axvline(x=salary_median, color='blue', linestyle='--', label='Median')
plt.legend()
plt.show()

media = df_2.mean()
mediana = df_2.median()
print(media)
print(mediana)

promedio = df_2.mean()                                  #Promedio.

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(df_2['company_size'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(df_2, x='salary_in_usd', y='company_size', hue='experience_level', inner='box', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

# @title salary_in_usd

from matplotlib import pyplot as plt
df_2['salary_in_usd'].plot(kind='hist', bins=20, title='salary_in_usd')
plt.gca().spines[['top', 'right',]].set_visible(False)

#PREGUNTA 3: CARGOS QUE RECIBEN MEJORES SUELDOS EN EMPRESAS CON SEDE EN ESTADOS UNIDOS

df_c = df_salaries.loc[:, ['job_title', 'company_location', 'salary_in_usd']]
df_c1 = df_c[df_c['company_location'] == "US"]
df_c2 = df_c1.groupby(['job_title']). max().sort_values(by='salary_in_usd', ascending=False)
df_c2 = df_c2[:10]
df_c2 = df_c2
df_c2

#GRÁFICO 1

sns.barplot(data=df_c2, x="salary_in_usd", y="job_title", legend=True, estimator="sum", errorbar=None, orient='y')
plt.axvline(df_c2['salary_in_usd'].mean(), color = 'red', linestyle='--')

#GRÁFICO 2
df_c2['salary_in_usd'].plot(kind= 'line', figsize=(20, 7), title='CARGOS QUE RECIBEN MAYOR SALARIO EN COMPAÑÍAS  CON SEDE EN EEUU', color = 'orangered', linestyle='--')

df_c2['salary_in_usd'].plot(kind='line', figsize=(20, 10), title='Cargos mejor remunerados en Compañías con sede en EEUU', color = 'orangered', linestyle='--')

#PREGUNTA 3: CARGOS QUE RECIBEN MEJORES SUELDOS EN EMPRESAS CON SEDE EN ESTADOS UNIDOS / SIN FILTROS

df_c = df_salaries.loc[:, ['job_title', 'company_location', 'salary_in_usd']]
df_c1 = df_c[df_c['company_location'] == "US"]
df_c2 = df_c1.groupby(['job_title']). max().sort_values(by='salary_in_usd', ascending=False)
print(df_c2)

#GRÀFICO PREGUNTA 3 SIN FILTROS
plt.figure(figsize=(20, 15))
sns.boxplot(data=df_c1, x='salary_in_usd', y='job_title', flierprops={'marker': 'x', 'markersize': 10, 'markerfacecolor': 'red'}, dodge=False, gap=.1)
plt.axvline(df_c2['salary_in_usd'].mean(), color = 'red', linestyle='--')

df = df_salaries.loc[:, ['salary_in_usd', 'experience_level']]
df_ex_en = df[df['experience_level'] == 'EN']
df_0 = df_ex_en.groupby('salary_in_usd', ).mean().sort_values(by='salary_in_usd', ascending=False)

#df_ex_mi = df[df['experience_level'] == 'MI']
#df_ex_se = df[df['experience_level'] == 'SE']
#df_agrupado = groupby([])

df_0

df = df_salaries.loc[:,['salary_in_usd', 'experience_level', 'employment_type', 'remote_ratio']]
df = df[(df['salary_in_usd'] >= 0) & (df['experience_level'].isin(['MI', 'SE'])) & (df['employment_type'] == 'FT') & (df['remote_ratio'] >= 50)]
#df.groupby('salary_in_usd').mean().sort_values(by='salary_in_usd', ascending=False)
df_1 = pd.DataFrame(df)
print(df_1)

df = df_salaries.loc[:,['salary_in_usd', 'experience_level']]
df_1 = df[(df['salary_in_usd'] >= 0) & (df['experience_level'] == 'EN')].agg(['mean', 'median'])
df_2 = df[(df['salary_in_usd'] >= 0) & (df['experience_level'] == 'MI')].agg(['mean', 'median'])
df_3 = df[(df['salary_in_usd'] >= 0) & (df['experience_level'] == 'SE')].agg(['mean', 'median'])

df_x = [[df_1 + df_2 + df_3]]
print(df_x)
#print(df_1)
#print(df_2)
#print(df_3)



 #[[df_1]]

df = df_salaries.loc[:,['salary_in_usd', 'experience_level']]
df_1 = df[(df['salary_in_usd'] >= 0) & (df['experience_level'] == 'EN')]
df_2 = df[(df['salary_in_usd'] >= 0) & (df['experience_level'] == 'MI')]
df_3 = df[(df['salary_in_usd'] >= 0) & (df['experience_level'] == 'SE')]



df_4 = pd.merge(df_1, df_2, on='salary_in_usd', how='inner')
df_5 = pd.merge(df_4, df_3, on='salary_in_usd', how='inner')
print(df_5)

#print(df_1.info())
#print(df_2)
#print(df_3)

#print(df_1.agg(['mean', 'median']))

print(df_1.head())

print(df_2.head())

from matplotlib import pyplot as plt
df_1['salary_in_usd'].plot(kind='hist', bins=20, title='salary_in_usd')
plt.gca().spines[['top', 'right',]].set_visible(False)