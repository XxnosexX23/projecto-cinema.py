import random
import matplotlib.pyplot as plt
# import numpy as np  # No se usa en este código, puedes eliminarlo si quieres
from variables import *

# Simulación de ventas mientras haya clientes y boletos disponibles
while customers > 0 and tickets > 0:
    money = random.randint(0, 300)  # Dinero aleatorio para cada cliente

    # Verifica si el cliente puede comprar un ticket
    if money >= cost_tickets:
        tickets -= 1
        tickets_sold += 1
        money -= cost_tickets
        
        # Elige aleatoriamente un combo de comida
        food_choice = random.choice([1, 2, 3])

        # Si elige combo 1 y hay stock y dinero suficiente
        if food_choice == 1 and food_combo_1 > 0 and money >= cost_combo_1:
            food_combo_1 -= 1
            combo_1_sold += 1
            money -= cost_combo_1
        # Si elige combo 2 y hay stock y dinero suficiente
        elif food_choice == 2 and food_combo_2 > 0 and money >= cost_combo_2:
            food_combo_2 -= 1
            combo_2_sold += 1
            drinks_sold += 1
            drinks -= 1
            money -= cost_combo_2
        # Si elige combo 3 y hay stock y dinero suficiente
        elif food_choice == 3 and food_combo_3 > 0 and money >= cost_combo_3:
            food_combo_3 -= 1
            combo_3_sold += 1
            drinks_sold += 1
            drinks -= 1
            snacks_sold += 1
            snacks -= 1
            money -= cost_combo_3

    customers -= 1  # Pasa al siguiente cliente

food_sold = combo_1_sold + combo_2_sold + combo_3_sold  # Total de comida vendida

# Mostrar los productos vendidos
print(f"Tickets vendidos: {tickets_sold}")
print(f"Comidas vendidas: {food_sold}")
print(f"Bebidas vendidas: {drinks_sold}")
print(f"Snacks vendidos: {snacks_sold}")

# Calcular las ganancias totales
total_sales = int(
    (tickets_sold * cost_tickets) +
    (combo_1_sold * cost_combo_1) +
    (combo_2_sold * cost_combo_2) +
    (combo_3_sold * cost_combo_3) +
    (drinks_sold * cost_drinks) +
    (snacks_sold * cost_snacks)
)

print(f"Ganancias totales: {total_sales}")

# Crear el diagrama de barras de ventas

plt.figure(figsize=(10, 5))                                     # Tamaño de la ventana del gráfico

plt.bar(
    ['Tickets', 'Comida', 'Bebida', 'Snacks'],                  # Etiquetas de las barras
    [tickets_sold, food_sold, drinks_sold, snacks_sold],        # Valores de las barras
    color=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],         # Colores de las barras
    edgecolor=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],     # Colores del borde
    linewidth=2,                                                # Grosor del borde
    alpha=0.5                                                   # Transparencia de las barras
)

plt.figtext(
    0.85,                                                       # Posición X del texto
    0.5,                                                        # Posición Y del texto 
    f"Ganancias:\n${total_sales}",                              # Texto a mostrar
    fontsize=14,                                                # Tamaño de la fuente
    ha='left',                                                  # Alineación horizontal
    va='center',                                                # Alineación vertical
    bbox=dict(facecolor='white', edgecolor='black')             # Caja de texto
)

plt.title('Ventas de productos')                                # Título del gráfico
plt.ylim(0, 200)                                                # Límite superior del eje Y
plt.show()                                                      # Mostrar el gráfico