import numpy as np


def choice_of_standard_data(dataChoice):
    # don't change the value of choice 1, choice 2,
    # choice 3 and choice 4 unless necessary.
    # for free variables, use choice 5 only.
    if dataChoice == 1:  # for example of European put; n can be 21, 61, 101,
        # 141
        X = 10.0
        r = 0.05
        sigma = 0.2
        T = 0.5
        n = 81
        m = 30
        Smin = 1.0
        Smax = 30
        index = np.array([2, 4, 6, 8, 10, 12, 14, 16])

        return [X, r, sigma, T, n, m, Smin, Smax, index]

    elif dataChoice == 2:  # for example of American put;
        X = 100.0
        r = 0.1
        sigma = 0.3
        T = 1
        n = 101
        m = 100
        Smin = 1.0
        Smax = np.exp(6)
        index = np.arange(80, 120, 5)

    elif dataChoice == 3:  # for example of random;
        X = 10.0
        r = 0.05
        sigma = 0.2
        T = 0.5
        n = 61
        m = 5
        Smin = 1.0
        Smax = 30
        index = np.arange(2, 16, 2)

        return [X, r, sigma, T, n, m, Smin, Smax, index]

    elif dataChoice == 4:  # for example of Binary Options;
        X = 15.0
        r = 0.05
        sigma = 0.2
        T = 0.25
        n = 101
        m = 60
        Smin = 1.0
        Smax = 30
        index = np.arange(5, 20, 1)

        return [X, r, sigma, T, n, m, Smin, Smax, index]

    elif dataChoice == 5:  # for free choices;
        X = 10.0
        r = 0.05
        sigma = 0.2
        T = 0.5
        n = 61
        m = 30
        Smin = 1.0
        Smax = 30
        index = np.arange(2, 16, 2)

        return [X, r, sigma, T, n, m, Smin, Smax, index]


if __name__ == "__main__":
    print(type(choice_of_standard_data(1)[4]))
