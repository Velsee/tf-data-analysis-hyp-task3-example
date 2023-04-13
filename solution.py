import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(control: np.array, test: np.array) -> bool:
    alpha = 0.01  # Установим уровень значимости
    t_stat, p_value = stats.ttest_ind(control, test)  # Сравниваем выборки

    # Если p_value меньше уровня значимости, отклоняем нулевую гипотезу
    if p_value < alpha:
        return True
    else:
        return False


# Выполняем скрипт с данными в формате .csv
url = "https://raw.githubusercontent.com/Velsee/Data/main/hyp3_historical_data.csv"

# Считываем данные из файла
df = pd.read_csv(url)

# Формируем массив для анализа
control_data = df[df["group"] == "control"]["NPV"].values
test_data = df[df["group"] == "test"]["NPV"].values

# Вызываем функцию и выводим ответ
answer = solution(control_data, test_data)
print("Отклонить ли нулевую гипотезу?", answer)

