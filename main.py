conteo = 0
cartas = 0
app_state = 1

cartas_bajas = ("2", "3", "4", "5", "6")
cartas_altas = ("10", "J", "Q", "K", "A")
cartas_medias = ("7", "8", "9")

while app_state == 1:
    
    carta = str(input("Ingrese su carta: "))
    
    if carta in cartas_bajas:
        conteo += 1
        cartas += 1
    elif carta in cartas_altas:
        conteo -= 1
        cartas += 1
    elif carta in cartas_medias:
        cartas += 1
    else:
        print ("Carta Invalida")
        
    print(f'El conteo es: {conteo}')
    print(f'La cantidad de cartas es: {cartas}')