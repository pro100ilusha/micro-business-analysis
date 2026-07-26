# Анализ данных микро-бизнеса
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('transactions.csv')

# Средний чек по месяцам
df['month'] = pd.to_datetime(df['date']).dt.to_period('M')
monthly_avg = df.groupby('month')['amount'].mean()
print("Средний чек по месяцам:")
print(monthly_avg)

# Визуализация
monthly_avg.plot(kind='bar', title='Средний чек по месяцам')
plt.ylabel('Сумма, руб')
plt.tight_layout()
plt.savefig('avg_check.png')
print("График сохранён в avg_check.png")
