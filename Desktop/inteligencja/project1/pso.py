import pyswarms as ps
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
from random import randint
import time

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
n_variables=10
n_formulas = 3
n_c = 10
x_max = np.ones(n_variables)
x_min = np.zeros(n_variables)
my_bounds = (x_min, x_max)

def endurance(genome, formulas):
    sum_f = 0
    # print(genome,formulas)
    for formula in formulas:
        for cla in formula:
            for el in cla:
                number_of_variable = el["x_n"]
                value_of_variable = round(genome[number_of_variable]) #zaokrąglam taka aby otrzymac tylko 0 lub 1
                # print(number_of_variable,value_of_variable)
                if el["negative"] == 1:
                    value_of_variable = abs(value_of_variable - 1)
                if value_of_variable == 1:
                    sum_f += 1
                    break
    # print(sum_f)
    return -sum_f

formulas = []
formula = []
for i in range(0, n_formulas):
    while len(formula) < n_c:
        x1 = randint(0,n_variables-1)
        x2 = randint(0,n_variables-1)
        x3 = randint(0,n_variables-1)
        if x1 != x2 and x1 != x3 and x2 != x3:
            formula.append([{"x_n": x1, "negative": randint(0,1)}, {"x_n": x2, "negative": randint(0,1)}, {"x_n": x3, "negative": randint(0,1)}])
    formulas.append(formula)
    formula = []

def f(x):
    n_particles = x.shape[0]
    j = [endurance(x[i],formulas) for i in range(n_particles)]
    return np.array(j)


optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=n_variables,
options=options, bounds=my_bounds)
start=time.time()
optimizer.optimize(f, iters=100)
end=time.time()
print('it took: ', end-start)
cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()