# RBF It is the main program for basic section
import time
import numpy as np
import math
from initial_condition import initial_condition
from TransformBack import TransformBack
from type_of_option import type_of_option
from choice_of_int_sch import choice_of_int_sch
from choice_of_standard_data import choice_of_standard_data
from choice_of_kernel import choice_of_kernel
from random_number_generator import random_number_generator
from EigenvalueRepresentation import Eigenvalue_Representation

datachoice = 1
randomchoice = 0
putorcall = 1
kernelchoice = 10
optionchoice = 10
intschchoice = 1
eigen_rep_choice = 0

t = time.time()

# Output for choice_of_standard_data [X r sigma T n m Smin Smax index]
choice = choice_of_standard_data(datachoice)
indexlength = len(choice[-1])  # Verified with MATLAB

dt = choice[3] / choice[5]

k = np.linspace(1, choice[4], choice[4])

dy = np.log(choice[7] / choice[6]) / (choice[4] - 1)
small_ds = dy / 100  # for calculating delta
if randomchoice == 0:
    y = np.log(choice[6]) + (k - 1) * dy
elif randomchoice == 1:
    y = np.log(choice[6]) + random_number_generator(choice[7], choice[4])
    # we still define dy as constant, for the use of Hardy's MQ

IC = initial_condition(choice[0], y, putorcall)

# Output for choice_of_kernel_var [L DL D2L c]
choice_of_kernel_var = choice_of_kernel(kernelchoice, choice[4], y, dy)

# inv_L = np.linalg.inv(np.transpose(choice_of_kernel_var[0]))

inv_L = (choice_of_kernel_var[0]) ** (-1)
a = (np.dot(np.transpose(inv_L), IC))
part_P = np.dot(inv_L * choice_of_kernel_var[2], 0.5 * (choice[2] ** 2))
part_P_1 = np.dot((choice[1] - 0.5 * choice[2] ** 2),
                  inv_L * choice_of_kernel_var[1])
P_1 = np.subtract(np.transpose(part_P),
                  (choice[1] * np.eye(choice[4], choice[4]))) # Transposed part_P

P = np.subtract(P_1, np.transpose(part_P_1))  # Transposed part_P_1

for i in range(1, choice[5]):  # time
    a = type_of_option(choice_of_kernel_var[0],
                       inv_L, a, choice[0], i, choice[1],
                       dt, y, choice[4], optionchoice, putorcall)
    a = choice_of_int_sch(a, P, dt, choice[4], intschchoice)

# Backward transform to obtain the European option prices (Compare with Table
# 2 on Page 11) [u uplus]
transform_back = TransformBack(choice[-1], y, choice_of_kernel_var[-1], a,
                               small_ds, indexlength, kernelchoice)
delta = (transform_back[1] - transform_back[0]) / small_ds

print([['Stock  ' 'Option ' 'Delta  '],
       str([choice[-1], transform_back[0], delta])])

elapsed = time.time() - t

if eigen_rep_choice == 1:
    alpha_by_eigen = Eigenvalue_Representation(P, choice_of_kernel_var[0], inv_L
                                               , IC, choice[3], choice[1], y,
                                               choice_of_kernel_var[-1],
                                               small_ds, indexlength,
                                               kernelchoice)

else:
    eigen_rep_choice = 0
