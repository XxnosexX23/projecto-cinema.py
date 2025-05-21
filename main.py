import random
import matplotlib.pyplot as plt
from variables import *

#? Simulación de ventas mientras haya clientes y boletos disponibles
while customers > 0 and tickets > 0:
    money = random.randint(0, 300)  #? Dinero aleatorio para cada cliente

    #? Verifica si el cliente puede comprar un ticket
    if money >= cost_tickets:
        tickets -= 1
        tickets_sold += 1
        money -= cost_tickets
        
        #? Elige aleatoriamente un combo de comida
        food_choice = random.choice([1, 2, 3])

        #? Si elige combo 1 y hay stock y dinero suficiente
        if food_choice == 1 and food_combo_1 > 0 and money >= cost_combo_1:
            food_combo_1 -= 1
            combo_1_sold += 1
            money -= cost_combo_1
        #? Si elige combo 2 y hay stock y dinero suficiente
        elif food_choice == 2 and food_combo_2 > 0 and money >= cost_combo_2:
            food_combo_2 -= 1
            combo_2_sold += 1
            drinks_sold += 1
            drinks -= 1
            money -= cost_combo_2
        #? Si elige combo 3 y hay stock y dinero suficiente
        elif food_choice == 3 and food_combo_3 > 0 and money >= cost_combo_3:
            food_combo_3 -= 1
            combo_3_sold += 1
            drinks_sold += 1
            drinks -= 1
            snacks_sold += 1
            snacks -= 1
            money -= cost_combo_3
        else:
            none += 1  #? Si no elige nada, se suma a la variable none
    else:
        customers_attended -= 1

    customers -= 1  #? Pasa al siguiente cliente

food_sold = combo_1_sold + combo_2_sold + combo_3_sold  #? Total de comida vendida

#? Mostrar los productos vendidos
print(f"Tickets vendidos: {tickets_sold}")
print(f"Comidas vendidas: {food_sold}")
print(f"Bebidas vendidas: {drinks_sold}")
print(f"Snacks vendidos: {snacks_sold}")
print(f"Clientes que no compraron nada: {none}")
print(f"clientes que compraron el combo 1: {combo_1_sold}")
print(f"clientes que compraron el combo 2: {combo_2_sold}")
print(f"clientes que compraron el combo 3: {combo_3_sold}")

#? Calcular las ganancias totales
total_sales = int(
    (tickets_sold * cost_tickets) +
    (combo_1_sold * cost_combo_1) +
    (combo_2_sold * cost_combo_2) +
    (combo_3_sold * cost_combo_3) +
    (drinks_sold * cost_drinks) +
    (snacks_sold * cost_snacks)
)

print(f"Ganancias totales: {total_sales}")

#? Crear el diagrama de barras de ventas

fig, axs = plt.subplots(2, 2, figsize=(18, 6))                      #* 1 fila, 2 columnas

#? Primer gráfico: Ventas de productos
axs[0, 0].bar(
    ['Tickets', 'Comida', 'Bebida', 'Snacks'],                      #* Etiquetas
    [tickets_sold, food_sold, drinks_sold, snacks_sold],            #* Valores
    color=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],             #* Colores
    edgecolor=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],         #* Colores de borde
    linewidth=2,                                                    #* Grosor del borde
    alpha=0.5                                                       #* Transparencia
)
axs[0, 0].set_title('Ventas de productos')                          #* Título del gráfico
axs[0, 0].set_ylim(0, 200)                                          #* Límite del eje y 

#? Segundo gráfico: Ventas de combos y ninguno
axs[0, 1].bar(
    ['Combo 1', 'Combo 2', 'Combo 3', 'Ninguno'],                   #* Etiquetas
    [combo_1_sold, combo_2_sold, combo_3_sold, none],               #* Valores
    color=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],             #* Colores
    edgecolor=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],         #* Colores de borde
    linewidth=2,                                                    #* Grosor del borde   
    alpha=0.5                                                       #* Transparencia
)
axs[0, 1].set_title('Elección de combos')                           #* Título del gráfico
axs[0, 1].set_ylim(0, 100)                                          #* Límite del eje y

#? primer gráfico circular
axs[1, 1].pie(
    [tickets_sold, food_sold, drinks_sold, snacks_sold],            #* Valores
    labels=['Tickets', 'Comida', 'Bebida', 'Snacks'],               #* Etiquetas
    colors=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],            #* Colores
    autopct='%1.1f%%',                                              #* Formato de porcentaje
    startangle=90,                                                  #* Ángulo de inicio
    shadow=False,                                                   #* Sombra
)

#? segundo grafico circular
axs[1, 0].pie(
    [combo_1_sold, combo_2_sold, combo_3_sold, none],               #* Valores
    labels=['Combo 1', 'Combo 2', 'Combo 3', 'Ninguno'],            #* Etiquetas
    colors=['#14a1e7', '#f2a900', '#f24c00', '#27ae60'],            #* Colores
    autopct='%1.1f%%',                                              #* Formato de porcentaje
    startangle=90,                                                  #* Ángulo de inicio
    shadow=False,                                                   #* Sombra
)

#? Texto de ganancias
fig.text(
    0.5, 0.85, f"Ganancias totales:\n${total_sales}",               #* Texto a mostrar
    fontsize=14,                                                    #* Tamaño de fuente
    ha='center',                                                    #* Alineación horizontal
    va='center',                                                    #* Alineación vertical
    bbox=dict(facecolor='white', edgecolor='black')                 #* Caja de texto
)

#? texto de clientes atendidos
fig.text(
    0.5, 0.2, f"Clientes atendidos:\n{customers_attended}",         #* Texto a mostrar 
    fontsize=14,                                                    #* Tamaño de fuente 
    ha='center',                                                    #* Alineación horizontal       
    va='center',                                                    #* Alineación vertical    
    bbox=dict(facecolor='white', edgecolor='black')                 #* Caja de texto
)

plt.tight_layout()                                                  #* Ajustar espacio de los gráficos
plt.show()                                                          #* Mostrar el gráfico