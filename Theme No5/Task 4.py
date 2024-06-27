import pandas as pd

# Загрузка CSV файла
file_path = 'bikes.csv'
df = pd.read_csv(file_path)

# Вычисление суммы столбца 'Rachel1'
column_sum = df['Rachel1'].sum()

print(f"Сумма столбца Rachel1: {column_sum}")
