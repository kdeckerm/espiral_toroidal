import matplotlib
matplotlib.use('TkAgg')  # Usa un backend interactivo
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros de la espiral toroidal
a = 7  # Radio mayor
b = 3  # Amplitud de oscilación
c = 1  # Altura de oscilación
alpha = 40  # Frecuencia angular

# Valores de t
t = np.linspace(0, 10 * np.pi, 1000)  # Más vueltas para una espiral más definida

# Función vectorial
x = (a + b * np.sin(alpha * t)) * np.cos(t)
y = (a + b * np.sin(alpha * t)) * np.sin(t)
z = c * np.cos(alpha * t)

# Crear la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la espiral toroidal
ax.plot(x, y, z, label="Espiral Toroidal", color="blue")

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Cambiar el ángulo de vista
elev = 90  # Elevación
azim = 120  # Rotación
ax.view_init(elev=elev, azim=azim)  # Ajusta elevación y rotación de la cámara

# Título
ax.set_title('Espiral Toroidal')

# Añadir los datos en la gráfica
text_str = (
    f"Parámetros:\na = {a}\nb = {b}\nc = {c}\nα = {alpha}\n"
    f"Ángulo de Vista:\nElevación = {elev}°\nRotación = {azim}°"
)
ax.text2D(0.05, 0.95, text_str, transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle="round", alpha=0.5))

# Leyenda
ax.legend()

# Guardar la gráfica como archivo PNG
plt.savefig("/home/decker/Documentos/Carpeta.py/espiral_toroidal_con_datos_y_angulo.png")



