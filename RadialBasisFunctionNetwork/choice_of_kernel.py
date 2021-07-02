import numpy as np
import math
from typing import List


def choice_of_kernel(kernelChoice, n, y, dy):
    deltaY = np.subtract(np.conjugate(np.meshgrid(y, y)), np.meshgrid(y, y))
    if kernelChoice == 10:  # suppose kernelchoice = 10 refers to Hardy's MQ;
        c = 4 * dy
        L = np.sqrt((np.square(np.transpose(deltaY))) + (c ** 2))
        DL = np.transpose(deltaY) / L
        denominator = np.divide((np.subtract(L, np.square(np.transpose(deltaY)))),
                                (np.transpose(np.square(np.transpose(L)))))
        D2L = np.divide(1, denominator)
        return [L, DL, D2L, c]

    elif kernelChoice == 20:  # suppose kernelchoice = 20; refers; to;
        # Gaussian; spline;
        c = np.exp(6) * dy
        L = np.exp(- np.conjugate(c * deltaY) ** 2)
        DL = -2 * (c ^ 2) * np.conjugate(deltaY) * L
        D2L = -2 * (c ^ 2) * np.conjugate(deltaY) * DL - 2 * (c ** 2) * L

        return [L, DL, D2L, c]

    elif kernelChoice == 30:  # which refers; to; thin # plate; spline;
        c = 2  # Power; of; the; kernel
        L = np.conjugate(deltaY) ^ np.conjugate(2 * c) * np.log(abs(deltaY))
        DL = np.conjugate(deltaY) ^ (2 * c - 1) \
             + 2 * c * np.conjugate(L) / deltaY
        D2L = (4 * c - 1) * np.conjugate(deltaY) ** (2 * c - 2) + (
                4 * c ^ 2 - 2 * c) * np.conjugate(L) / np.conjugate(deltaY) ** 2
        # to; place; the ?¡±NaN?? diagonal; by; the; limit; of; the; function

        L[1: len(L) + 1:len(L)] = 0
        DL[1: len(DL) + 1:len(DL)] = 0
        D2L[1: len(D2L) + 1:len(D2L)] = 0

        return [L, DL, D2L, c]
