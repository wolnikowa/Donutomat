import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import matplotlib.pyplot as plt
# Set-up hyperparameters
from pyswarms.utils.plotters import plot_cost_history

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

# Call instance of GlobalBestPSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
                                    options=options)

# Perform optimization
stats = optimizer.optimize(fx.sphere, iters=100)

# plot
hist=optimizer.cost_history

plot_cost_history(hist)
print(hist)
plt.show()