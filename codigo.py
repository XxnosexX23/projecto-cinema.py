import random

# Variables de cantidad
tickets = 200
customers = 300

# Costo de los productos
cost_tickets = 100

# Contadores de tickets y comida vendidos
tickets_sold = 0

while customers > 0 and tickets > 0:
    money = random.randint(0, 200)

    # Verificar si el cliente puede comprar un ticket
    if money >= cost_tickets:
        tickets -= 1
        tickets_sold += 1
        money -= cost_tickets

    customers -= 1

# Mostrar los tikets restantes y los vendidos
print(f"Quedaron {tickets} tickets")
print(f"Tickets vendidos: {tickets_sold}")