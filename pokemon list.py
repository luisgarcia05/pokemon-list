x= input("Eres chico o chica?")
w= "Bienvenid"
if x== "chico":
    w +="o"
else:
    w += "a"
print(w, "al mundo de los pokemon!")

y= input("Que edad tienes?")

if int(y)<10:
    if x== "chico":
        print("No tienes edad para ser entrenador")
    else:
        print("No tienes edad para ser entrenadora")
    quit()

reg= input("Necesitarás un compañero de viaje. En que región te encuentras")
if reg=="kanto" and x=="chico":
    print("Tu compañera de viaje es Misty")
else:
    print("Tu compañero de viaje es Brock")

tipo= input("Que tipo de pokemon quieres para empezar?")
if tipo ==("agua"):
    print("Tu starter es Oshawott")
elif tipo==("fuego"):
    print("Tu starter es Cyndaquil")
else:
    tipo== "planta"
    print("Tu starter es Rowlet")

print("Es hora de que comiences tu aventura")
print("Pero primero, tengamos un combate")

print("EL COMBATE HA EMPEZADO")

if tipo== "agua":
 starte_rrival="planta"
 PS_jugador= 20
 ataque_jugador= 15
 defensa_jugador= 15
 PS_Oponente= 25
 ataque_oponente= 10
 defensa_oponente= 15

elif tipo== "fuego":
  starte_rrival="agua"
  PS_jugador= 15
  ataque_jugador= 25
  defensa_jugador= 10
  PS_Oponente= 20
  ataque_oponente= 15
  defensa_oponente= 15

else:
 tipo== "planta"
 starte_rrival="fuego"
 PS_jugador= 25
 ataque_jugador= 10
 defensa_jugador= 15
 PS_Oponente= 15
 ataque_oponente= 25
 defensa_oponente= 10

if tipo=="fuego":
 list= "placaje", "ascuas", "malicioso"
 while PS_jugador>0 and PS_Oponente>0:
    movimientojugador= ""
    while not movimientojugador:
     print("tus movimientos son:", list)
     movimientojugador= input("que movimiento escoges")
     if movimientojugador=="malicioso":
       print("has usado", movimientojugador)
       defensa_oponente = defensa_oponente- 2

       print("el oponente tiene", PS_Oponente, "PS")
       print("tienes", PS_Oponente, "PS")

       movimientojugador= ""
       

       movimientoenemigo=("Malicioso", "placaje")
       import random
       print("tu oponente ha usado",random.choice(movimientoenemigo))
       if random.choice(movimientoenemigo)== "placaje":
        PS_jugador= PS_jugador-5


        print("el oponente tiene", PS_Oponente, "PS")
        print("tienes", PS_Oponente, "PS")

        if PS_jugador<=0:
         print("has perdido")
         quit()
        
       else:
          defensa_jugador= defensa_jugador-2

          print("el oponente tiene", PS_Oponente, "PS")
          print("tienes", PS_Oponente, "PS")
          

       #el enemigo ha terminado su turno, ahora te toca a ti
       


     elif movimientojugador=="ascuas":
       print("has usado", movimientojugador)
       PS_Oponente= PS_Oponente - defensa_oponente/4
       print("el oponente tiene", PS_Oponente, "PS")
       print("tienes", PS_Oponente, "PS")

       if PS_Oponente<=0:
          print("has ganado")
          quit()
       movimientojugador= ""

       movimientoenemigo=("Malicioso", "placaje")
       import random
       print("tu oponente ha usado",random.choice(movimientoenemigo))

       if random.choice(movimientoenemigo)== "placaje":
        PS_jugador= PS_jugador-5

        print("el oponente tiene", PS_Oponente, "PS")
        print("tienes", PS_Oponente, "PS")
        if PS_jugador <=0:
           print("has perdido")
           quit()
       else:
          defensa_jugador= defensa_jugador-2

          print("el oponente tiene", PS_Oponente, "PS")
          print("tienes", PS_Oponente, "PS")
       #el enemigo ha terminado su turno, ahora te toca a ti

     elif movimientojugador=="placaje":
       print("has usado", movimientojugador)
       PS_Oponente= PS_Oponente-5
       print("el oponente tiene", PS_Oponente, "PS")
       print("tienes", PS_Oponente, "PS")

       if PS_Oponente<=0:
          print("has perdido")
          quit()

       movimientojugador= ""

       movimientoenemigo=("Malicioso", "placaje")
       import random
       print("tu oponente ha usado",random.choice(movimientoenemigo))

       if random.choice(movimientoenemigo)== "placaje":
        PS_jugador= PS_jugador-5

        print("el oponente tiene", PS_Oponente, "PS")
        print("tienes", PS_Oponente, "PS")
        
        if PS_jugador<=0:
           print("has perdido")
           quit()
       else:
          defensa_jugador= defensa_jugador-2
       #el enemigo ha terminado su turno, ahora te toca a ti
       
       
     else:
       print("Tus movimientos son ascuas, placaje y malicioso")
       movimientojugador==""
    #el jugador ha terminado su turno, ahora le toca al oponente
    
