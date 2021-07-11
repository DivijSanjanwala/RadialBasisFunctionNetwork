import numpy as np
import time
import math
from TransformBack import TransformBack


def Eigenvalue_Representation(P, L, inv_L, IC, T, index, y, c, small_ds,
                              indexLength, kernelChoice):
    # TODO: L is an unused parameter

    t = time.time()
    lambda_, W = np.linalg.eig(P)

    # TODO: np.divide instead of / since W =np eig doesnt have class _truediv_

    k_coefficient = (W / (inv_L * IC)) * np.exp(- np.diag(lambda_) * T)

    alpha_by_eigen = W * k_coefficient

    transformBack = TransformBack(index, y, c,
                                  np.real(alpha_by_eigen),
                                  small_ds, indexLength, kernelChoice)

    delta = (transformBack[1] - transformBack[0]) / small_ds
    print('\n')  # line break in the command view
    print('Above is the result of the Original Result')
    print([['Stock  ', 'Option ', 'Delta  '],
           str([index, transformBack[0], delta])])
    elapsed = time.time() - t
    print('\n')  # line break in the command view
    print(
        'Above is the result obtained by the Eigen Value Representation Method')

    return alpha_by_eigen
