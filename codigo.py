import random
import matplotlib.pyplot as plt
import numpy as np

# Variables de cantidad
tickets = 200
food = 100
drinks = 100
customers = 300

# Costo de los productos
cost_tickets = 100
cost_food = 50
cost_drinks = 25

# Contadores de tickets y comida vendidos
tickets_sold = 0
food_sold = 0
drinks_sold = 0

while customers > 0 and tickets > 0:
    money = random.randint(0, 250)

    # Verificar si el cliente puede comprar un ticket
    if money >= cost_tickets:
        tickets -= 1
        tickets_sold += 1
        money -= cost_tickets
        
        # Verificar si el cliente puede comprar comida
        if food > 0 and money >= cost_food:
            food -= 1
            food_sold += 1
            money -= cost_food

            # Verificar si el cliente puede comprar bebida
            if drinks > 0 and money >= cost_drinks:
                drinks -= 1
                drinks_sold += 1
                money -= cost_drinks

    customers -= 1

# Mostrar los productos restantes y los vendidos
print(f"Quedaron {tickets} tickets")
print(f"Quedaron {food} comidas")
print(f"Quedaron {drinks} bebidas")
print(f"Tickets vendidos: {tickets_sold}")
print(f"Comidas vendidas: {food_sold}")
print(f"Bebidas vendidas: {drinks_sold}")

# Calcular ganancias
total_sales = (tickets_sold * cost_tickets) + (food_sold * cost_food) + (drinks_sold * cost_drinks)
print(f"Ganancias totales: {total_sales}")


# hacer diagrama de barras

# hace la ventana mas grande
plt.figure(figsize=(10, 5))

# hace las barras y sus atributos
plt.bar(
    # etiquetas de las barras
    ['Tickets', 'Comida', 'Bebida'],

    # valores de las barras
    [tickets_sold, food_sold, drinks_sold],

    # color de las barras
    color=['#14a1e7', '#f2a900', '#f24c00'],

    # color de el borde de las barras
    edgecolor=['#14a1e7', '#f2a900', '#f24c00'],

    # tamaño del borde de las barras
    linewidth=2,

    # transparencia de las barras
    alpha=0.5
)

# titulo de la grafica
plt.title('Ventas de productos')

# maximo de la barra
plt.ylim(0, 200)

# mostrar la barra
plt.show()