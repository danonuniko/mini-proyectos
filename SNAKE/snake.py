import turtle                                   #Importamos módulo que nos permite dibujar.
import time                                     #Podremos manipular las velocidades a las que se ejecuta el programa
import random                                   #Lo utilizaremos entre otras para poder ir moviendo la manzana.

posponer = 0.1                                  #Creamos variable que nos servirá para variar la velocidad entre frames de ejecución.

#Marcador
score = 0
high_score = 0

#Configuración de la ventana
wn = turtle.Screen()                            #Dibujamos la pantalla del juego.
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)                                    #(I) Parace que hace que los movimientos sean más fluidos

#Cabeza serpiente
cabeza = turtle.Turtle()                        #Dibujamos el cuadrado dentro del espacio Turtle
cabeza.speed(0)                                 #Comienza parado
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()                                  #Evitamos que vaya dejando rastro al ir dibujando.
cabeza.goto(0,0)                                #Turtle dibuja desde el centro como si fueran ejes xy normales.
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()                        
comida.speed(0)                                 
comida.shape("circle")
comida.color("red")
comida.penup()                                  
comida.goto(0,100)

#Segmentos - Cuerpo serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)                                  #Para que cuando abramos la pantalla ya aparezca dibujado.
texto.color("white")
texto.penup()                                   #Escondemos trazo del pincel.
texto.hideturtle()                              #Escondemos pincel.
texto.goto(0,260)
texto.write("Score: 0     High Score: 0", align="center", font=("Courier", 24, "normal"))

#Funciones
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def derecha():
    cabeza.direction = "right"

def izquierda():
    cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":                
        y = cabeza.ycor()                       #Obtenemos la cordenada y de la posición de nuestra cabeza
        cabeza.sety(y + 20)                     #Le añadimos 20px.

    if cabeza.direction == "down":                
        y = cabeza.ycor()                       
        cabeza.sety(y - 20) 
        
    if cabeza.direction == "left":                
        x = cabeza.xcor()                       
        cabeza.setx(x - 20) 
        
    if cabeza.direction == "right":                
        x = cabeza.xcor()                       
        cabeza.setx(x + 20)  

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:                                     #Bucle principal normal en la mayoría de juegos.
    wn.update()

    #Colisiones bordes.
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Reseteamos el cuerpo de la serpiente.
        [i.hideturtle() for i in segmentos]
        segmentos.clear()
        posponer = 0.1

        #Resetear marcador
        score = 0
        texto.clear() 
        texto.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Colisiones comida-serpiente.
    if cabeza.distance(comida) < 20:
        #Mover la comida a posición random
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        posponer *= 0.99

        #Cuerpo de la serpiente
        nuevo_segmento = turtle.Turtle()                        
        nuevo_segmento.speed(0)                                 
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 1

        if score > high_score:
            high_score = score

        texto.clear() 
        texto.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Mover el cuerpo de la serpiente.
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Reseteamos el cuerpo de la serpiente.
            [i.hideturtle() for i in segmentos]
            segmentos.clear()
            posponer = 0.1

             #Resetear marcador
            score = 0
            texto.clear() 
            texto.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(posponer)                        #Establecemos un periodo de descanso entre repetición y repetición de la función mov.
