import pandas as pd
 
# Загружаем данные
data = pd.read_csv('C:\Users\User\Desktop\Данные хуйни\obs.csv')
 
# Вычисляем коэффициент корреляции
correlation = data['variable1'].corr(data['variable2'])
 
print('Коэффициент корреляции:', correlation)