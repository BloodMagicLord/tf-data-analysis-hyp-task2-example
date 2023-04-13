import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 632165934  # Ваш chat ID, не меняйте название переменной
CONST = 0.02


def solution(x: np.array, y: np.array) -> bool:
    return anderson_ksamp([x, y]).significance_level < CONST
