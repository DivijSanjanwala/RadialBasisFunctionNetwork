import numpy as np


def TransformBack(index, y, c, a, small_ds, indexLength, kernelchoice):
    u = []
    uplus = []
    # list_index = np.arange(1, indexLength + 1)
    for i in range(indexLength):
        if kernelchoice == 10:
            u.append(np.sqrt(((np.log(index[i])) - y) ** 2 + (c ** 2)) * a)
            uplus.append(np.sqrt(((np.log(index[i]) + small_ds) - y) ** 2 + (c ** 2)) * a)

        elif kernelchoice == 20:
            u[i] = np.exp(-(c ** 2) *
                          (np.log(index[i]) - y) ** 2) * a
            uplus[i] = np.exp(-(c ** 2) *
                              (np.log(index[i] + small_ds) - y) ** 2) * a
        elif kernelchoice == 30:
            u[i] = (np.log(index[i]) - y) ** np.transpose(2 * c) \
                   * np.log(abs(np.log(index[i]) - y)) * a

            uplus[i] = (np.log(index[i] + small_ds) - y) ** (2 * c) \
                       * np.log(abs(np.log(index[i] + small_ds) - y)) * a

    return [u, uplus]


