from matplotlib.pyplot import *
from numpy import *

import fonctions

n = int(input("Which dimension do you want to study?"))
k = int(input("Which eigenvalue do you want to study?"))

# first interval that we want to study
X = linspace(0, 7, max(400, k ** 2))
# for each value of L, find the sharp upper bound depending on n, k, L
Y = []
for l in X:
    Y.append(fonctions.sharp_upper_bound(n, k, l))
# find the critical length
y_max_index = Y.index(max(Y))
if max(Y) > Y[-1]:
    critical_length = round(X[y_max_index], 3)
else:
    critical_length = "infinite"

# refine the interval according to the critical length
if critical_length == "infinite":
    pass
else:
    X = linspace(0, min(critical_length * 4, 7), max(400, k ** 2))
    Y = []
    for l in X:
        Y.append(fonctions.sharp_upper_bound(n, k, l))
    # find the critical length
    y_max_index = Y.index(max(Y))
    if max(Y) > Y[-1]:
        critical_length = round(X[y_max_index], 3)
    else:
        critical_length = "infinite"
# endtry


if max(Y) > Y[-1]:
    critical_length2 = "Finite critical length"
else:
    critical_length2 = "Infinite critical length"

# find the sharp upper bound depending on n, k
if max(Y) > Y[-1]:
    upper_bound = round(max(Y), 3)
else:
    upper_bound = round(max(Y))

# plotting Steklov-Dirichlet eigenvalues
for i in range(0, fonctions.l_0(n, k) + 1):
    dirichlet_i = []
    for l in X:
        dirichlet_i.append(fonctions.sigma_dirichlet(n, i, l))
    plot(X, dirichlet_i, "b")
# plotting Steklov-Neumann eigenvalues
for i in range(1, fonctions.l_0(n, k) + 2):
    neumann_i = []
    for l in X:
        neumann_i.append(fonctions.sigma_neumann(n, i, l))
    plot(X, neumann_i, "g")
# centering the figure
if critical_length == round(X[y_max_index], 3):
    center_x = min(critical_length * 4, 7)
else:
    center_x = 7
# plotting the sharp upper bound
plot(X, Y, "r")
# lengending according to the indicators found
title(critical_length2)
xlabel("Value of L")
ylabel(f"{k}th eigenvalue")
figtext(0.6, 0.3, f"Critical length {critical_length}", style="italic")
figtext(0.6, 0.2, f"B_{n} = {upper_bound}", style="italic")
axis([0, center_x, 0, max(Y) + 2])
show()