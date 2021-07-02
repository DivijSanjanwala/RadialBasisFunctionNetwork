import math
import random
from typing import List
import numpy as np


def random_number_generator(Smax, n) -> List:
    loop = 1
    minimum_distance = 0.025
    y = [0] + np.sort(math.log(Smax) * np.random.uniform(2, n - 1, size=(n - 1)))
    while loop == 1:
        flag = [0]
        loop = 0
        for i in range(2, n - 1, 1):
            if (y[i] - y[i - 1]) - minimum_distance:
                loop = 1
                flag = np.concatenate((flag, [i]), 1)

        size_of_flag_plus_1, x = np.shape(flag)

        flag = flag[2: size_of_flag_plus_1]

        y[flag] = math.log(Smax) * np.random.uniform(1, size_of_flag_plus_1 - 1)

        y = np.sort(y)

    return y


# if __name__ == "__main__":
#     random_number_generator(30, 101)

