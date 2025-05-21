import random

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

            # Verificar si el cliente puede comprar bebida
            if drinks > 0 and money >= cost_drinks:
                drinks -= 1
                drinks_sold += 1
                money -= cost_drinks

    customers -= 1

# Mostrar los tikets restantes y los vendidos
print(f"Quedaron {tickets} tickets")
print(f"Quedaron {food} comidas")
print(f"Quedaron {drinks} bebidas")
print(f"Tickets vendidos: {tickets_sold}")
print(f"Comidas vendidas: {food_sold}")
print(f"Bebidas vendidas: {drinks_sold}")

# Calcular ganancias

total_sales = (tickets_sold * cost_tickets) + (food_sold * cost_food) + (drinks_sold * cost_drinks)
print(f"Ganancias totales: {total_sales}")