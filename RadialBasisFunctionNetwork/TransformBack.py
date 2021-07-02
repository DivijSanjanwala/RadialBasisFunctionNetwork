import math
import numpy as np


def TransformBack(index, y, c, a, small_ds, indexLength, kernelchoice):
    u = []
    uplus = []

    for i in range(indexLength):
        if kernelchoice == 10:
            u[i] = math.sqrt(np.transpose((math.log(index[i])) - y)
                             ** 2 + (c ** 2)) * a
            uplus[i] = math.sqrt(
                np.transpose((math.log(index[i]) + small_ds) - y)
                ** 2 + (c ** 2)) * a
        elif kernelchoice == 20:
            u[i] = math.exp(-(c ** 2) * np.transpose(math.log(index[i])
                                                     - y) ** 2) * a
            uplus[i] = math.exp(-(c ** 2) *
                                np.transpose(math.log(index[i]
                                                      + small_ds) - y) ** 2) * a
        elif kernelchoice == 30:
            u[i] = (np.transpose(math.log(index[i]) - y)
                    ** np.transpose(2 * c) *
                    math.log(abs(math.log(index[i]) - y))) * a

            uplus[i] = (np.transpose(math.log(index[i] + small_ds) - y)
                        ** np.transpose(2 * c) *
                        math.log(abs(math.log(index(i) + small_ds) - y))) * a

    return [u, uplus]
