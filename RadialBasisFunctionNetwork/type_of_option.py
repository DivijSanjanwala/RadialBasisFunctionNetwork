import numpy as np


def type_of_option(L, inv_L, a, X, i, r, dt, y, n, optionchoice, putorcall):
    U = L * a
    if optionchoice == 10 and putorcall == 1:  # European put option
        U[1] = X * np.exp(-r * i * dt)
    elif optionchoice == 10 and putorcall == 10:  # European call options
        U[1] = 0
        U[n] = np.exp(y(n))  # boundary condition for call
    elif optionchoice == 10 and putorcall == 2:  # European Cash or Nothing
        # put option
        U[1] = 1 * np.exp(-r * i * dt)
    elif optionchoice == 10 and putorcall == 20:  # European Cash or Nothing
        # call options
        U[1] = 0
        U[n] = 1 * np.exp(-r * i * dt)
    elif optionchoice == 10 and putorcall == 3:  # European Asset or Nothing
        # put option
        U[1] = 0
    elif optionchoice == 10 and putorcall == 30:  # European Asset or Nothing
        # call options
        U[n] = np.exp(y[n])
    elif optionchoice == 20 and putorcall == 1:  # American put option
        for j in range(1, n):
            U[j] = np.maximum(X - np.exp(y[j]), U[j])
    elif optionchoice == 20 and putorcall == 10:  # American call option
        for j in range(1, n):
            U[j] = np.maximum(np.exp(y[j]) - X, U[j])
            # but it should in fact same as the European case since we don't
            # consider dividend
    elif optionchoice == 20 and putorcall == 2:  # American Cash or Nothing
        # put option
        for j in range(1, n):
            U[j] = np.maximum(X - np.exp(y[j]) > 0, U[j])
    elif optionchoice == 20 and putorcall == 20:  # American Cash or Nothing
        # call option
        for j in range(1, n):
            U[j] = np.maximum(np.exp(y[j]) - X > 0, U[j])
    elif optionchoice == 20 and putorcall == 3:  # American Asset or Nothing
        # put option
        for j in range(1, n):
            U[j] = np.maximum(np.exp(y[j]) * (X - np.exp(y[j]) > 0), U[j])
    elif optionchoice == 20 and putorcall == 30:  # American Asset or Nothing
        # call option
        for j in range(1, n):
            U[j] = np.maximum(np.exp(y[j]) * (np.exp(y[j]) - X > 0), U[j])
    a = inv_L * U

    return a
