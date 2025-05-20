import random

# Variables de cantidad
tickets = 200
food = 100
customers = 300

# Costo de los productos
cost_tickets = 100
cost_food = 50

# Contadores de tickets y comida vendidos
tickets_sold = 0
food_sold = 0

while customers > 0 and tickets > 0:
    money = random.randint(0, 200)

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

    customers -= 1

# Mostrar los tikets restantes y los vendidos
print(f"Quedaron {tickets} tickets")
print(f"Quedaron {food} comidas")
print(f"Tickets vendidos: {tickets_sold}")
print(f"Comidas vendidas: {food_sold}")