import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Definir las variables y la función Z
x1, x2 = sp.symbols('x1 x2')
Z = 6*x1 + 3*x2

# Definir las restricciones
eq1 = 2*x1 + 4*x2 - 8
eq2 = -x1 + 4*x2 - 4
eq3 = x1 - x2 - 2

# Resolver las ecuaciones para x2 en términos de x1
x2_1 = sp.solve(eq1, x2)[0]
x2_2 = sp.solve(eq2, x2)[0]
x2_3 = sp.solve(eq3, x2)[0]

# Crear un rango de valores de x1 para graficar
x1_values = np.linspace(0, 4, 400)

# Calcular los correspondientes valores de x2 para cada ecuación
x2_values_1 = [x2_1.subs(x1, val) for val in x1_values]
x2_values_2 = [x2_2.subs(x1, val) for val in x1_values]
x2_values_3 = [x2_3.subs(x1, val) for val in x1_values]

# Graficar las restricciones
plt.plot(x1_values, x2_values_1, label='2x1 + 4x2 <= 8')
plt.plot(x1_values, x2_values_2, label='-x1 + 4x2 <= 4')
plt.plot(x1_values, x2_values_3, label='x1 - x2 <= 2')

# Añadir etiquetas y leyenda
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()

# Mostrar el gráfico
plt.show()
