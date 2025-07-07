print ("El juego de piedra, papel o tijeras esta por empezar")
import random
puntos=0
cpup=0
empezar=["empezar","salir"]
while True:
    print('Escriba "empezar" para iniciar el juego''\no "salir" para terminar el juego')
    elementos_a_escoger=["piedra","papel","piedra"]
    msg_principal=input("[Empezar|Salir]:\n")
    if msg_principal == "Salir":
        print("Hasta la próxima")
        break
    elif msg_principal == "Empezar":
        print("El juego empezo")
        ready = input("Elige entre piedra, papel o tijeras:\n").lower()
        bot = random.choice(elementos_a_escoger)
        print(f"La máquina eligió: {bot}")
        
        if ready == bot:
            print("¡Empate!\n")
        elif ((ready == "piedra" and bot == "tijeras") or (ready == "papel" and bot == "piedra") or (ready == "tijeras" and bot == "papel")):
            print("Felicidades, ganaste esta partida\n")
            userpts += 1
            print(f"Puntaje - Tú: {puntos} | Máquina: {cpup}\n")
        else:
            print("Perdiste esta partida...\n")
            cpupts += 1
            print(f"Puntaje - Tú: {puntos} | Máquina: {cpup}\n")
        continue
    else:
        print("Opción no válida.\n")
        continue
    
print("\n Resultado total:")
if puntos > cpup:
    print("¡Ganaste el juego!")
    print("Tu puntaje:",puntos)
    print("Estos los los puntos del bot:", cpup)

elif puntos < cpup:
    print("El bot ganó.")
    print("Tu puntaje:", puntos)
    print("Estos los los puntos del bot:", cpup)
else:
    print("Es un empate")
    print("Tu puntaje:",puntos)
    print("Estos los los puntos del bot:", cpup)