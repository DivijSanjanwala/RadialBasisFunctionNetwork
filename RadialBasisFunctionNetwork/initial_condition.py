import numpy as np


def initial_condition(X, y, initialCondChoice):
    if initialCondChoice == 1:  # American (or European) put
        IC = np.maximum(X - np.exp(np.transpose(y)), 0)

        return IC

    elif initialCondChoice == 10:  # American (or European) call
        IC = np.maximum(np.exp(np.transpose(y)) - X, 0)
        # Cash - or -Nothing
        return IC

    elif initialCondChoice == 2:  # cash - or -nothing put
        IC = 1 * (X - np.exp(np.transpose(y)) > 0)

        return IC

    elif initialCondChoice == 20:  # cash- or -nothing call
        IC = 1 * (np.exp(np.transpose(y)) - X > 0)
        # Asset- or -Nothing
        return IC

    elif initialCondChoice == 3:  # asset- or -nothing put
        IC = np.exp(np.transpose(y)) * (X - np.exp(np.transpose(y)) > 0)

        return IC

    elif initialCondChoice == 30:  # asset - or -nothing call
        IC = np.exp(np.transpose(y)) * (np.exp(np.transpose(y)) - X > 0)

        return IC
