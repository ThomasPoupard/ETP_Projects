import numpy as np

param_names = ['method', 'inflation growth rate', 'walls element size factor', 'in/outlets element size factor']
categorical_params_mapping = {
    'method' : {0 : 'quadrilateral dominant', 1 : 'triangles', 2 : 'multizone quad/tri'}
}

L9 = np.array([
    [1, 1, 1, 1],
    [1, 2, 2, 2],
    [1, 3, 3, 3],
    [2, 1, 2, 3],
    [2, 2, 3, 1],
    [2, 3, 1, 2],
    [3, 1, 3, 2],
    [3, 2, 1, 3],
    [3, 3, 2, 1]
], dtype=int)

param_levels = np.array([
    [0, 1, 2],
    [1.2, 1.4, 1.6],
    [.5, .75, 1.],
    [.5, .75, 1.]
])

exp_results = np.array([
    0.98564, 0.99368, 0.99283, 0.97398, 0.97323, 0.97283, 0.99356, 0.98953, 0.99132
])

nb_exp, nb_params = L9.shape
nb_levels = param_levels.shape[1]

for p in range(nb_params):
    level_scores = np.array([exp_results[L9[:, p] == level].mean() for level in range(1, nb_levels+1)])
    opt_level = np.argmax(level_scores)

    param_name = param_names[p]
    opt_value = param_levels[p, opt_level] if param_name not in categorical_params_mapping.keys() else categorical_params_mapping[param_name][param_levels[p, opt_level]]

    print(f"Optimal value for {param_name}: {opt_value}")