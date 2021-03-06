import numpy as np


def choice_of_int_sch(a, P, dt, n, intschChoice):
    if intschChoice == 1:  # choice of BD1
        a = a - dt * np.dot(a, P)  # TODO: Flipped a and P
        return a

    elif intschChoice == 2:  # choice of RK2
        F1 = -dt * P * a
        F2 = -dt * P * (a + .5 * F1)
        a = a + .5 * (F1 + F2)
        return a

    elif intschChoice == 4:  # choice of RK4
        F1 = -dt * P * a
        F2 = -dt * P * (a + .5 * F1)
        F3 = -dt * P * (a + .5 * F2)
        F4 = -dt * P * (a + F3)
        a = a + 1 / 6 * (F1 + 2 * F2 + 2 * F3 + F4)
        return a

    elif intschChoice == 5:  # choice of Implicit backward time integration
        theta = 0.5
        matrix1 = np.identity(n) + dt * (1 - theta) * P
        matrix2 = np.identity(n) - dt * theta * P
        a = matrix1 / matrix2 * a
    elif intschChoice == 6:  # choice of Parallel Time Step
        V1 = np.linalg.inv((np.identity(n) + 1 * dt * P)) * a
        V2 = np.linalg.inv((np.identity(n) + 2 / 5 * dt * P)) * a
        V3 = np.linalg.inv((np.identity(n) + 9 / 14 * dt * P)) * a
        V4 = np.linalg.inv((np.identity(n) + 1 / 2 * dt * P)) * a
        a = 19 / 45 * V1 - 2500 / 153 * V2 - 2401 / 255 * V3 + 79 / 3 * V4
        return a

        # Reference: Wn of R(z); of; Page; 5; of; Fasshauer; 2004; end

    return a
