import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

# Выполняем скрипт с данными в формате .csv
url = "https://raw.githubusercontent.com/Velsee/Data/main/hyp3_historical_data.csv"

# Считываем данные из файла
data = pd.read_csv(url)

control_data = data.loc[data["group"] == "control"]
test_data = data.loc[data["group"] == "test"]

# Целевая переменная, предположительно "NPV"
control_NPV = control_data["NPV"]
test_NPV = test_data["NPV"]

# Функция для проверки статистической значимости
def solution(control_NPV: np.array, test_NPV: np.array, alpha: float) -> bool:
    t_stat, p_val = stats.ttest_ind(control_NPV[:500], test_NPV[:500], equal_var=False)
    
    # Отклонить нулевую гипотезу, если p-значение меньше заданного уровня значимости
    reject_null_hypothesis = p_val < alpha
    
    return reject_null_hypothesis

# Уровень значимости критерия
alpha = 0.01

result = solution(control_NPV, test_NPV, alpha)

print("Отклонить ли нулевую гипотезу:", result)
