import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

# Call instance of GlobalBestPSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
                                    options=options)
# point1
# Perform optimization, func rastrigin instead of sphere
# stats = optimizer.optimize(fx.rastrigin, iters=100)

# Perform optimization, func matyas instead of sphere
# stats = optimizer.optimize(fx.matyas, iters=100)

# Perform optimization, func rosenbrock instead of sphere
stats = optimizer.optimize(fx.rosenbrock, iters=100)


# plot
hist=optimizer.cost_history

plot_cost_history(hist)
print(hist)
plt.show()