import pyxel
import random
import constantes
from mario import Mario
from bloque import Bloque
from enemy import Enemy
from powerup import Powerup
class Tablero:
    # Esta clase contiene la información necesaria
    # para crear el tablero
    def __init__(self, w: int , h: int):
        # Los parámetros son el ancho y el alto del tablero
        self.width = w
        self.heigh = h
        # Aquí vamos a crear también Mario
        # aqui le damos a Mario sus valores de x, y, un booleano para la dirección y la posición inicio de salto
        # que es 0
        self.mario = Mario(25, 204, True, 0)
        # aqui le damos los valores a la clase bloque
        # la función en clase bloque hace que los bloques se muevan cuando Mario llegue al final de la pantalla
        self.bloque = Bloque(self.width / 3, 205, True)
        # Aquí creamos a los enemigos
        # con esta lista vamos a saber cual es tipo de enemigo que toca colocar en pantalla
        self.typeenemy = []
        # se crea un lista posenemy para darle una posición aleatoria a los enemigos
        # la posición de los enemigos empieza desde la segunda pantalla por ello el 256
        posenemy = []
        for i in range(4):
            g = random.randint(1,100)
            if g <= 75:
                self.typeenemy.append("goomba")
                x = random.randint(256, 709)
                posenemy.append(x)
            else:
                self.typeenemy.append("Koopa")
                x = random.randint(256, 709)
                posenemy.append(x)
        # Enemigos
        # aqui se ejecutan las cuatro funciones para los enemigos con todos los parametros anteriores
        self.e1 = Enemy(posenemy[0], 204, self.typeenemy[0], False)
        self.e2 = Enemy(posenemy[1], 204, self.typeenemy[1], False)
        self.e3 = Enemy(posenemy[2], 204, self.typeenemy[2], False)
        self.e4 = Enemy(posenemy[3], 204, self.typeenemy[3], False)
        # powerup
        # estas son las coordenadas donde se va imprimir la seta y un booleano para imprimirla y luego quitarla en el
        # momento que la toca Mario
        self.seta = Powerup(652,148,False,False)
        # bloques sorpresa
        # estas variables controlan que la interaccion con los bloques sorpresa solo occura una vez
        self.sorpresa1 = False
        self.coin1 = False
        self.sorpresa2 = False
        self.sorpresa3 = False
        self.sorpresa4 = False
        self.sorpresa5 = False
        self.sorpresa6 = False
        # bloques de ladrillos
        # estas variables hacen que los ladrillos puedan desaparecer cuando Super Mario los toque
        self.ladrillo1 = True
        self.ladrillo2 = True
        self.ladrillo3 = True
        # Esto es para la fila de ladrillos que se genera con un for
        # esta lista es para los ladrillos al final de el nivel que se generan en fila y hacen los mismo que las
        # anteriores
        self.ladrillo = [True, True, True, True, True]
        # Esta variable sirve para reiniciar el nivel después de morir
        self.death = False
        # vidas
        # van bajando cuando Mario pierde
        self.lives = 3
        # para que el jugador pueda salir del área goomba sin morir después de perder los efectos del powerup
        self.parpadeo = False
        # score
        self.score = 0
    def update(self):
        # tiempo por partida
        self.time = [180, 190, 210]

        # colisión bloques
        # estas son las listas con todas las colisiones que se usan para comparar con la posición de Mario
        self.colsup = []
        self.mario.bloqueinf = []
        self.mario.colleft = []
        self.mario.colright = []
        # colisión superior de clase bloque
        # estas variables son los bloques que Super Mario puede romper si Mario toca estos valores se cambia su
        # coordenada x a -500 para asi remover la colisión
        # se tienen que remover las cuatro colisiones del bloque que Super Mario golpea
        if self.ladrillo1:
            bloque1 = 594
        else:
            bloque1 = -500
        if self.ladrillo2:
            bloque2 = 630
        else:
            bloque2 = -500
        if self.ladrillo3:
            bloque3 = 666
        else:
            bloque3 = -500
        if self.ladrillo[0]:
            bloque4 = 790
        else:
            bloque4 = -500
        if self.ladrillo[1]:
            bloque5 = 808
        else:
            bloque5 = -500
        if self.ladrillo[2]:
            bloque6 = 826
        else:
            bloque6 = -500
        if self.ladrillo[3]:
            bloque7 = 844
        else:
            bloque7 = -500
        if self.ladrillo[4]:
            bloque8 = 862
        else:
            bloque8 = -500
        # estas tres listas contienen todos los valores necesarios para crear las colisiones superiores
        # estas son las colisiones de todos los bloques del juego
        # primero se da una valor x
        # después se da un range que sirve para crear todos los valores x e y de un bloque
        # se da un valor y
        # en este caso el valor que se movería sería la x ya que en las colisiones superiores la y no cambia
        listaxup = [90, 255, 470, bloque1, 612, bloque2, 648, bloque3, bloque4, bloque5, bloque6, bloque7, bloque8, 910, 190, 310, 550, 700]
        rangeup = [90, 25, 50, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 25, 25, 25, 25, 25]
        listayup = [148, 148, 164, 148, 148, 148, 148, 148, 148, 148, 148, 148, 148, 148, 180, 180, 180, 180]
        # el for rellena la lista colsup (la colisión superior)
        for i in range(len(listaxup)):
            posbloque1 = listaxup[i]
            for j in range(rangeup[i]):
                sublist = [posbloque1, listayup[i]]
                self.colsup.append(sublist)
                posbloque1 += 1

        # repasa toda la lista de las colisiones superiores(excepto el suelo)
        # este for hace que todas las colisiones se muevan conforme Mario se mueve
        for i in range(470):
            self.colsup[i][0] -= self.bloque.x
        # colisión inferior de bloque
        # estas variables son los bloques que Super Mario puede romper si Mario toca estos valores se cambia su
        # coordenada x a -500 para asi remover la colisión
        # se tienen que remover las cuatro colisiones del bloque que Super Mario golpea
        if self.ladrillo1:
            bloque1 = 594
        else:
            bloque1 = -500
        if self.ladrillo2:
            bloque2 = 630
        else:
            bloque2 = -500
        if self.ladrillo3:
            bloque3 = 666
        else:
            bloque3 = -500
        if self.ladrillo[0]:
            bloque4 = 790
        else:
            bloque4 = -500
        if self.ladrillo[1]:
            bloque5 = 808
        else:
            bloque5 = -500
        if self.ladrillo[2]:
            bloque6 = 826
        else:
            bloque6 = -500
        if self.ladrillo[3]:
            bloque7 = 844
        else:
            bloque7 = -500
        if self.ladrillo[4]:
            bloque8 = 862
        else:
            bloque8 = -500
        # estas tres listas contienen todos los valores necesarios para crear las colisiones inferiores
        # primero se da una valor x
        # después se da un range que sirve para crear todos los valores x e y de un bloque
        # se da un valor y
        # en este caso el valor que se movería sería la x ya que en las colisiones inferiores la y no cambia
        listaxdown = [94, 255, 470, bloque1, 612, bloque2, 648, bloque3, 626, bloque4, bloque5, bloque6, bloque7, bloque8, 910]
        rangedown = [90, 25, 50, 18, 18, 18, 18, 18, 25, 18, 18, 18, 18, 18, 25]
        listaydown = [172, 172, 192, 172, 172, 172, 172, 172, 120, 172, 172, 172, 172, 172, 172]
        # el for rellena la lista bloqueinf (la colisión inferior)
        for i in range(len(listaxdown)):
            posbloque2 = listaxdown[i]
            for j in range(rangedown[i]):
                sublist = [posbloque2, listaydown[i]]
                self.mario.bloqueinf.append(sublist)
                posbloque2 += 1

        # Repasa toda la lista de colisiones inferiores
        # este for hace que todas las colisiones se muevan conforme Mario se mueve
        for i in range(395):
            self.mario.bloqueinf[i][0] -= self.bloque.x

        # colisión suelo
        self.suelo = []
        # suelo
        # estos dos for crean las colisiones del suelo de que se usan en el nivel
        possuelo1 = -1
        for i in range(512):
            sublist = [possuelo1, 204]
            self.suelo.append(sublist)
            possuelo1 += 1
        # hay dos for porque entre medio de las dos listas hay un hueco entonces ahi no debe haber colisión
        possuelo2 = 550
        for i in range(650):
            sublist = [possuelo2, 204]
            self.suelo.append(sublist)
            possuelo2 += 1
        for i in range(1162):
            self.suelo[i][0] -= self.bloque.x
        # Colisiones laterales
        # por la izquierda
        # estas variables son los bloques que Super Mario puede romper si Mario toca estos valores se cambia su
        # coordenada x a -500 para asi remover la colisión
        # se tienen que remover las cuatro colisiones del bloque que Super Mario golpea
        if self.ladrillo1:
            bloque1 = 593
        else:
            bloque1 = -500
        if self.ladrillo[0]:
            bloque4 = 789
        else:
            bloque4 = -500
        if self.ladrillo[1]:
            bloque5 = 807
        else:
            bloque5 = -500
        if self.ladrillo[2]:
            bloque6 = 825
        else:
            bloque6 = -500
        if self.ladrillo[3]:
            bloque7 = 843
        else:
            bloque7 = -500
        if self.ladrillo[4]:
            bloque8 = 861
        else:
            bloque8 = -500
        # estas tres listas contienen todos los valores necesarios para crear las colisiones por izquierda
        # primero se da una valor x
        # después se da un range que sirve para crear todos los valores x e y de un bloque
        # se da un valor y
        # en este caso el valor que se movería sería la y ya que en las colisiones por izquierda la x no cambia
        listaizqx = [93, 253, 469, bloque1, 611, 629, 665, 647, 625, bloque4, bloque5, bloque6, bloque7, bloque8, 909, 189, 309, 551, 699]
        listaizqrange = [30, 70, 30, 40, 40, 40, 40, 40, 60, 40, 40, 40, 40, 40, 60, 30, 30, 30, 30]
        listaizqy = [180, 196, 196, 190, 190, 190, 190, 190, 124, 176, 176, 176, 176, 176, 176, 215, 215, 215, 215]
        # el for rellena la lista colleft (la colisión por izquierda)
        for i in range(len(listaizqx)):
            posleft = listaizqy[i]
            for j in range(listaizqrange[i]):
                sublist = [listaizqx[i], posleft]
                self.mario.colleft.append(sublist)
                posleft -= 1

        # Repasa toda la lista de colisiones por la izquierda
        # este for hace que todas las colisiones se muevan conforme Mario se mueve
        for i in range(770):
            self.mario.colleft[i][0] -= self.bloque.x
        # Por la derecha
        # estas variables son los bloques que Super Mario puede romper si Mario toca estos valores se cambia su
        # coordenada x a -500 para asi remover la colisión
        # se tienen que remover las cuatro colisiones del bloque que Super Mario golpea
        if self.ladrillo3:
            bloque3 = 667
        else:
            bloque3 = -500
        if self.ladrillo[0]:
            bloque4 = 813
        else:
            bloque4 = -500
        if self.ladrillo[1]:
            bloque5 = 829
        else:
            bloque5 = -500
        if self.ladrillo[2]:
            bloque6 = 845
        else:
            bloque6 = -500
        if self.ladrillo[3]:
            bloque7 = 863
        else:
            bloque7 = -500
        if self.ladrillo[4]:
            bloque8 = 881
        else:
            bloque8 = -500
        # estas tres listas contienen todos los valores necesarios para crear las colisiones por derecha
        # primero se da una valor x
        # después se da un range que sirve para crear todos los valores x e y de un bloque
        # se da un valor y
        # en este caso el valor que se movería sería la y ya que en las colisiones por derecha la x no cambia
        listaderx = [185, 281, 621, 653, 613, 631, 649, bloque3, bloque4, bloque5, bloque6, bloque7, bloque8, 937, 215, 335, 575, 725]
        listaderrange = [40, 40, 40, 40, 25, 25, 25, 25, 25, 25, 25, 25, 25, 40, 30, 30, 30, 30]
        listadery = [180, 180, 124, 124, 176, 176, 176, 176, 176, 176, 176, 176, 176, 176, 215, 215, 215, 215]
        # el for rellena la lista colright (la colisión por la derecha)
        for i in range(len(listaderx)):
            posright = listadery[i]
            for j in range(listaderrange[i]):
                sublist = [listaderx[i], posright]
                self.mario.colright.append(sublist)
                posright -= 1

        #Repasa toda la lista de colisiones por la derecha
        # este for hace que todas las colisiones se muevan conforme Mario se mueve
        for i in range(545):
            self.mario.colright[i][0] -= self.bloque.x

        #botones
        # si se presiona el botón q o las vidas son 0 o Mario llega al final del nivel se acaba el juego
        if pyxel.btnp(pyxel.KEY_Q) or self.lives == 0 or self.mario.x >= 1024 - self.bloque.x:
            pyxel.quit()
        # si se presiona la tecla derecha invoca la función Mario move
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.move("right", self.width)
        # cuando Mario llega a la mitad de la pantalla y se pulsa la tecla derecha todos los objetos se mueven
        # a la izquierda. La condicion not in self.Mario.colleft hace que Mario no se mueva si colisiona con un bloque.
        # esto simula que Mario se mueve.
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario.perm == True \
                and [self.mario.x,self.mario.y] not in self.mario.colleft:
            self.bloque.move("left")
            self.e1.screen(True)
            self.e2.screen(True)
            self.e3.screen(True)
            self.e4.screen(True)
            self.seta.screen(True)
        #muerte por altura
        # si la posición de Mario es mayor a 236 Mario death es True y se ejecuta el death
        if self.mario.y > 236:
            self.death = True

        # si se presiona la tecla izquierda invoca la función Mario move
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.move("left", self.width)
        # si se presiona la tecla up y mario esta en el suelo o en una colisión superior entonce se ejecuta la funcion
        # jump. Se inicia el algoritmo que permite el salto
        if pyxel.btn(pyxel.KEY_UP) and ([self.mario.x,self.mario.y] in self.suelo
                                        or [self.mario.x,self.mario.y] in self.colsup):
            self.mario.up = True
            self.mario.inicio = self.mario.y
        if self.mario.up == True:
            self.mario.jump("up")
        if self.mario.up == False and [self.mario.x,self.mario.y] not in self.colsup \
                and [self.mario.x,self.mario.y] not in self.suelo:
            self.mario.jump("down")
        # aca se todas las funciones de los enemigos
        #movimiento enemigos
        #e1: este es el enemigo uno
        # los ifs comprueban si el enemigo esta en las colisiones de derecha o izquierda. Si es que es el caso el
        # enemigo cambiara de dirección
        if [self.e1.x, self.e1.y] in self.mario.colright:
            self.e1.direction = True
        if [self.e1.x, self.e1.y] in self.mario.colleft or self.e1.x >= 1024:
            self.e1.direction = False
            self.e1.move("left")
        if self.e1.direction == False:
            self.e1.move("left")
        if self.e1.direction == True:
            self.e1.move("right")
        # este if da gravedad al enemigo
        if [self.e1.x, self.e1.y] not in self.suelo:
            self.e1.gravity(True)
        #matar enemigos
        # se crea con un for la lista de colisión de Mario con enemigos
        e1collide = []
        for i in range(-10, 10):
            sublist = [self.e1.x + i, self.e1.y - 16]
            e1collide.append(sublist)
        # si la posición de Mario se alinea con la lista collide self.live se hace false y el enemigo muere
        if [self.mario.x, self.mario.y] in e1collide:
            self.e1.live = False
            self.score += 100
        #matar a Mario
        # se crea con un for la lista de colisión de Mario con enemigos
        e1kill = []
        for i in range(-10, 10):
            sublist = [self.e1.x + i, self.e1.y]
            e1kill.append(sublist)
        # si la posición de mario se alinea con la lista y el enemigo esta vivo y Mario no es Super
        # y no esta en el parpadeo mientras que pierde una vida entonces muere
        if [self.mario.x, self.mario.y] in e1kill and self.e1.live and self.mario.supermario == False \
                and self.parpadeo == False:
            self.death = True
        # esto es igual que el de arriba solo que hace que Mario vaya de Super Mario a Mario pequeño
        elif [self.mario.x, self.mario.y] in e1kill and self.e1.live and self.mario.supermario \
                and self.parpadeo == False:
            self.mario.supermario = False
            self.parpadeo = True
        # e2
        # es exactamente igual al enemigo 1
        if [self.e2.x, self.e2.y] in self.mario.colright:
             self.e2.direction = True
        if [self.e2.x, self.e2.y] in self.mario.colleft or self.e2.x >= 1024:
            self.e2.direction = False
            self.e2.move("left")
        if self.e2.direction == False:
            self.e2.move("left")
        if self.e2.direction == True:
            self.e2.move("right")
        # este if da gravedad al enemigo
        if [self.e2.x, self.e2.y] not in self.suelo:
            self.e2.gravity(True)
        # matar enemigos
        e2collide = []
        for i in range(-10, 10):
            sublist = [self.e2.x + i, self.e2.y - 16]
            e2collide.append(sublist)
        if [self.mario.x, self.mario.y] in e2collide:
            self.e2.live = False
            self.score += 100
        # matar a Mario
        e2kill = []
        for i in range(-10, 10):
            sublist = [self.e2.x + i, self.e2.y]
            e2kill.append(sublist)
        if [self.mario.x, self.mario.y] in e2kill and self.e2.live and self.mario.supermario == False \
                and self.parpadeo == False:
            self.death = True
        elif [self.mario.x, self.mario.y] in e2kill and self.e2.live and self.mario.supermario \
                and self.parpadeo == False:
            self.mario.supermario = False
            self.parpadeo = True
        # e3
        # es exactamente igual al enemigo 1
        if [self.e3.x, self.e3.y] in self.mario.colright:
            self.e3.direction = True
        if [self.e3.x, self.e3.y] in self.mario.colleft or self.e3.x >= 1024:
            self.e3.direction = False
            self.e3.move("left")
        if self.e3.direction == False:
            self.e3.move("left")
        if self.e3.direction == True:
            self.e3.move("right")
        if [self.e3.x, self.e3.y] not in self.suelo:
            self.e3.gravity(True)
        # matar enemigos
        e3collide = []
        for i in range(-10, 10):
            sublist = [self.e3.x + i, self.e3.y - 16]
            e3collide.append(sublist)
        if [self.mario.x, self.mario.y] in e3collide:
            self.e3.live = False
            self.score += 100
        # matar a Mario
        e3kill = []
        for i in range(-10, 10):
            sublist = [self.e3.x + i, self.e3.y]
            e3kill.append(sublist)
        if [self.mario.x, self.mario.y] in e3kill and self.e3.live and self.mario.supermario == False \
                and self.parpadeo == False:
            self.death = True
        elif [self.mario.x, self.mario.y] in e3kill and self.e3.live and self.mario.supermario \
                and self.parpadeo == False:
            self.mario.supermario = False
            self.parpadeo = True
        # e4
        # es exactamente igual al enemigo 1
        if [self.e4.x, self.e4.y] in self.mario.colright:
            self.e4.direction = True
        if [self.e4.x, self.e4.y] in self.mario.colleft or self.e4.x >= 1024:
            self.e4.direction = False
            self.e4.move("left")
        if self.e4.direction == False:
            self.e4.move("left")
        if self.e4.direction == True:
            self.e4.move("right")
        if [self.e4.x, self.e4.y] not in self.suelo:
            self.e4.gravity(True)
        # matar enemigos
        e4collide = []
        for i in range(-10, 10):
            sublist = [self.e4.x + i, self.e4.y - 16]
            e4collide.append(sublist)
        if [self.mario.x, self.mario.y] in e4collide:
            self.e4.live = False
            self.score += 100
        # matar a Mario
        e4kill = []
        for i in range(-10, 10):
            sublist = [self.e4.x + i, self.e4.y]
            e4kill.append(sublist)
        if [self.mario.x, self.mario.y] in e4kill and self.e4.live and self.mario.supermario == False\
                and self.parpadeo == False:
            self.death = True
        elif [self.mario.x, self.mario.y] in e4kill and self.e4.live and self.mario.supermario \
                and self.parpadeo == False:
            self.mario.supermario = False
            self.parpadeo = True
        # Parpadeo
        # Cuando Mario no está en ninguna de las áreas de muerte y el parpadeo viene siendo True
        # Se cambia el parpadeo a False para que Mario vuelva a ser vulnerable
        if [self.mario.x, self.mario.y] not in e1kill and self.parpadeo == True \
                and [self.mario.x, self.mario.y] not in e2kill and self.parpadeo == True \
                and [self.mario.x, self.mario.y] not in e3kill and self.parpadeo == True \
                and [self.mario.x, self.mario.y] not in e4kill and self.parpadeo == True:
            self.parpadeo = False


        # Se inicializan las listas de colliders de los bloques sopresa
        bloquesorpesacolide = []
        bloquesorpesacolide2 = []
        bloquesorpesacolide3 = []
        bloquesorpesacolide4 = []
        bloquesorpesacolide5 = []
        bloquesorpesacolide6 = []

        # relleno de las listas con las coordenadas de sus partes inferiores

        for j in range(0, 18):
            self.mario.bloqueinf[j][1] += 4
            bloquesorpesacolide.append(self.mario.bloqueinf[j])
        for j in range(90, 115):
            self.mario.bloqueinf[j][1] += 4
            bloquesorpesacolide2.append(self.mario.bloqueinf[j])
        for j in range(183, 201):
            self.mario.bloqueinf[j][1] += 4
            bloquesorpesacolide3.append(self.mario.bloqueinf[j])
        for j in range(219, 237):
            self.mario.bloqueinf[j][1] += 4
            bloquesorpesacolide4.append(self.mario.bloqueinf[j])
        for j in range(255, 280):
            self.mario.bloqueinf[j][1] += 4
            bloquesorpesacolide5.append(self.mario.bloqueinf[j])
        for j in range(370, 395):
            self.mario.bloqueinf[j][1] += 4
            bloquesorpesacolide6.append(self.mario.bloqueinf[j])
        # Condicionales que detectan si Mario golpea los bloques. mediante un if anidado se hace posible
        # que Mario solo reciba el premio si es la primera vez que golpea el bloque.
        # Todos dan monedas menos uno que da el power up
        if [self.mario.x, self.mario.y] in bloquesorpesacolide:
            if self.sorpresa1 == False:
                self.mario.coins += 1
                self.score += 200
            self.sorpresa1 = True
        if [self.mario.x, self.mario.y] in bloquesorpesacolide2:
            if self.sorpresa2 == False:
                self.mario.coins += 1
                self.score += 200
            self.sorpresa2 = True
        if [self.mario.x, self.mario.y] in bloquesorpesacolide3:
            if self.sorpresa3 == False:
                self.mario.coins += 1
                self.score += 200
            self.sorpresa3 = True
        # Este es el que ofrece la seta tan solo una vez
        if [self.mario.x, self.mario.y] in bloquesorpesacolide4:
            if self.sorpresa4 == False:
                self.seta.life = True
            self.sorpresa4 = True
        if [self.mario.x, self.mario.y] in bloquesorpesacolide5:
            if self.sorpresa5 == False:
                self.mario.coins += 1
                self.score += 200
            self.sorpresa5 = True
        if [self.mario.x, self.mario.y] in bloquesorpesacolide6:
            if self.sorpresa6 == False:
                self.mario.coins += 1
                self.score += 200
            self.sorpresa6 = True
        # Powerup
        # Basicamente se comporta igual que un enemigo. De hecho el algoritmo es el mismo.
        # a excepción de las partes que matan a Mario ya que no es el caso del Power up.
        if self.seta.life:
            if [self.seta.x, self.seta.y] in self.mario.colright:
                self.seta.direction = True
            if [self.seta.x, self.seta.y] in self.mario.colleft:
                self.seta.direction = False
                self.seta.move("left")
            if self.seta.direction == False:
                self.seta.move("left")
            if self.seta.direction == True:
                self.seta.move("right")
            if [self.seta.x, self.seta.y] not in self.colsup:
                if [self.seta.x, self.seta.y] not in self.suelo:
                    self.seta.gravity(True)
        # obtener seta
        # Crea la lista de collider de la seta para que Mario la coja.
        # Una vez las coordenadas se alineen seta.life será False y no se imprimirá en el draw
        # Mario.supermario será True y el sprite de Mario cambiará
        # Se suma score
        if self.seta.life:
            setacollide = []
            for i in range(-15, 15):
                sublist = [self.seta.x + i, self.seta.y]
                setacollide.append(sublist)
            for i in range(-15, 15):
                sublist = [self.seta.x, self.seta.y+i]
                setacollide.append(sublist)
            if [self.mario.x, self.mario.y] in setacollide:
                self.seta.life = False
                self.mario.supermario = True
                self.score += 1000
        #destruir los bloques con super mario
        # Se iniciazan las listas de los colliders de los bloques de ladrillos
        # estas son las listas de los objetos que se pueden destruir
        bloquedestruir1 = []
        bloquedestruir2 = []
        bloquedestruir3 = []
        bloquedestruir4 = []
        bloquedestruir5 = []
        bloquedestruir6 = []
        bloquedestruir7 = []
        bloquedestruir8 = []
        # crear lista para cada bloque que mario debe detectar cuando es super Mario
        # aqui se llena la lista con de los bloques a destruir con las sublistas de la colision inferior
        # respectivas. Para poder hacer esto se usa el range respectivo de cada bloque a destruir
        for j in range(165, 183):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir1.append(self.mario.bloqueinf[j])
        for j in range(201, 219):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir2.append(self.mario.bloqueinf[j])
        for j in range(237, 255):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir3.append(self.mario.bloqueinf[j])
        for j in range(280, 298):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir4.append(self.mario.bloqueinf[j])
        for j in range(298, 316):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir5.append(self.mario.bloqueinf[j])
        for j in range(316, 334):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir6.append(self.mario.bloqueinf[j])
        for j in range(334, 352):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir7.append(self.mario.bloqueinf[j])
        for j in range(352, 370):
            self.mario.bloqueinf[j][1] += 4
            bloquedestruir8.append(self.mario.bloqueinf[j])
        # detección cuando Mario toca un bloque destructible por debajo usando las listas de arriba
        # siempre que mario.supermario sea True claro. Ya que si no no puede romperlos.
        # si se produce la colisión adecuada ladrillo[i] será False y dejará de imprimirse en el Draw
        if self.mario.supermario:
            if [self.mario.x, self.mario.y] in bloquedestruir1:
                self.ladrillo1 = False
            if [self.mario.x, self.mario.y] in bloquedestruir2:
                self.ladrillo2 = False
            if [self.mario.x, self.mario.y] in bloquedestruir3:
                self.ladrillo3 = False
            if [self.mario.x, self.mario.y] in bloquedestruir4:
                self.ladrillo[0] = False
                self.ladrillo4 = False
            if [self.mario.x, self.mario.y] in bloquedestruir5:
                self.ladrillo[1] = False
            if [self.mario.x, self.mario.y] in bloquedestruir6:
                self.ladrillo[2] = False
            if [self.mario.x, self.mario.y] in bloquedestruir7:
                self.ladrillo[3] = False
            if [self.mario.x, self.mario.y] in bloquedestruir8:
                self.ladrillo[4] = False

        # funcion para el tiempo
        if self.lives == 3:
            self.time[0] -= pyxel.frame_count//30
        elif self.lives == 2:
            self.time[1] -= pyxel.frame_count // 30
        elif self.lives == 1:
            self.time[2] -= pyxel.frame_count // 30



        # En caso de morir para reiniciar los atributos de Tablero. Es igual que el __init__
        # ocurre solo cuando las vidas de Mario son mayores que 0
        if self.death and self.lives > 0:
            # Aquí vamos a crear también Mario
            self.mario = Mario(25, 204, True,0)
            # self.bloque = Bloque(200,200)
            self.bloque = Bloque(self.width / 3, 205, True)
            # Aquí creamos a los enemigos
            self.typeenemy = []
            posenemy = []
            for i in range(4):
                g = random.randint(1, 100)
                if g <= 75:
                    self.typeenemy.append("goomba")
                    x = random.randint(256, 709)
                    posenemy.append(x)
                else:
                    self.typeenemy.append("Koopa")
                    x = random.randint(256, 709)
                    posenemy.append(x)
            # Enemigos
            self.e1 = Enemy(posenemy[0], 204, self.typeenemy[0], False)
            self.e2 = Enemy(posenemy[1], 204, self.typeenemy[1], False)
            self.e3 = Enemy(posenemy[2], 204, self.typeenemy[2], False)
            self.e4 = Enemy(posenemy[3], 204, self.typeenemy[3], False)
            # powerup
            self.seta = Powerup(652, 148, False, False)
            # bloques sorpresa
            self.sorpresa1 = False
            self.coin1 = False
            self.sorpresa2 = False
            self.sorpresa3 = False
            self.sorpresa4 = False
            self.sorpresa5 = False
            self.sorpresa6 = False
            # bloques de ladrillos
            self.ladrillo1 = True
            self.ladrillo2 = True
            self.ladrillo3 = True
            # Esto es para la fila de ladrillos que se genera con un for
            self.ladrillo = [True, True, True, True, True]
            # Para reiniciar el death para que el juego pueda correr
            self.death = False
            self.lives -= 1
            #Para salir del goomba si te ha quitado super Mario
            self.parpadeo = False
            self.score = 0



    def draw(self):
        # aqui se dibuja el fondo
        pyxel.cls(6)
        # Aquí dibujaremos el resto de los objetos
        # este es el suelo
        x = 0
        for i in range(32):
            pyxel.blt(x - self.bloque.x,220,0,16,16,16,16)
            x += 16
        x = 560
        for i in range(39):
            pyxel.blt(x - self.bloque.x,220,0,16,16,16,16)
            x += 16

        #tuberías
        pyxel.blt(200 - self.bloque.x, 196, 0, 0, 16, 16, 24,6)
        pyxel.blt(320 - self.bloque.x, 196, 0, 0, 16, 16, 24, 6)
        pyxel.blt(560 - self.bloque.x, 196, 0, 0, 16, 16, 24, 6)
        pyxel.blt(710 - self.bloque.x, 196, 0, 0, 16, 16, 24, 6)
        #texto
        pyxel.text(10, 10, "LIVES", 0)
        pyxel.text(18, 17, str(self.lives), 0)
        pyxel.text(60, 10, "COINS", 0)
        pyxel.text(68, 17, str(self.mario.coins), 0)
        pyxel.text(130, 10, "WORLD\n 1-1", 0)
        pyxel.text(179, 10, "TIME", 0)
        # condición para imprimir el tiempo que queda en el nivel
        if self.lives == 3:
            pyxel.text(180, 17, str(self.time[0]), 0)
        elif self.lives == 2:
            pyxel.text(180, 17, str(self.time[1]), 0)
        elif self.lives == 1:
            pyxel.text(180, 17, str(self.time[2]), 0)
        # imprimir el score
        pyxel.text(200, 10, "SCORE", 0)
        pyxel.text(208, 17, str(self.score), 0)



        #fondo(arbusto y nubes)
        pyxel.blt(160 - self.bloque.x, 204, 0, 0, 40, 32, 16,6)
        pyxel.blt(140 - self.bloque.x, 100, 0, 0, 56, 24, 16, 6)
        pyxel.blt(250 - self.bloque.x, 40, 0, 0, 56, 24, 16, 6)
        pyxel.blt(390 - self.bloque.x, 80, 0, 0, 56, 24, 16, 6)
        pyxel.blt(450 - self.bloque.x, 110, 0, 0, 56, 24, 16, 6)
        #ladrillos
        x = 0
        for i in range(4):
            pyxel.blt(x + 120 - self.bloque.x, 164, 0, 32, 0, 16, 16)
            x += 16
        x = 0
        for i in range(2):
            pyxel.blt(x + 480 - self.bloque.x, 180, 0, 32, 0, 16, 16)
            x += 16
        # se usa este if para imprimir los ladrillos destructibles, si es false se dejan de imprimir
        if self.ladrillo1 == True:
            pyxel.blt(604 - self.bloque.x, 164, 0, 32, 0, 16, 16)
        if self.ladrillo2 == True:
            pyxel.blt(636 - self.bloque.x, 164, 0, 32, 0, 16, 16)
        if self.ladrillo3 == True:
            pyxel.blt(668 - self.bloque.x, 164, 0, 32, 0, 16, 16)
        x = 0
        for i in range(5):
            if self.ladrillo[i] == True:
                pyxel.blt(x + 800 - self.bloque.x, 164, 0, 32, 0, 16, 16)
            x += 16
        #bloque sorpresa
        # esto hace que se pueda cambiar de sprite los bloques sorpresa
        # mientras Mario no los toque la condición va ser False entonces se imprimiran en su estado normal
        # si Mario los toca la condición se vuelve True y se imprimiran en su estado "vacio"
        if self.sorpresa1 == False:
            pyxel.blt(104 - self.bloque.x, 164, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(104 - self.bloque.x, 164, 0, 16, 0, 16, 16)
        if self.sorpresa2 == False:
            pyxel.blt(265 - self.bloque.x, 164, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(265 - self.bloque.x, 164, 0, 16, 0, 16, 16)
        if self.sorpresa3 == False:
            pyxel.blt(620 - self.bloque.x, 164, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(620 - self.bloque.x, 164, 0, 16, 0, 16, 16)
        if self.sorpresa5 == False:
            pyxel.blt(636 - self.bloque.x, 110, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(636 - self.bloque.x, 110, 0, 16, 0, 16, 16)
        if self.sorpresa4 == False:
            pyxel.blt(652 - self.bloque.x, 164, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(652 - self.bloque.x, 164, 0, 16, 0, 16, 16)
        if self.sorpresa6 == False:
            pyxel.blt(920 - self.bloque.x, 164, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(920 - self.bloque.x, 164, 0, 16, 0, 16, 16)
        #bandera del final del nivel
        pyxel.blt(1024 - self.bloque.x, 189, 0, 0, 72, 18, 31,6)
        #Mario y animaciones
        # Mario tomando los valores del objeto Mario
        # este if revisa si mario esta en el suelo o en una colision superior si se cumple no pasa nada
        # si no se cumple la animacion cambia a la de salto
        if self.mario.supermario == False and ([self.mario.x, self.mario.y] in self.colsup\
                or [self.mario.x, self.mario.y] in self.suelo):
            pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0], self.mario.sprite[1], self.mario.sprite[2],
                      self.mario.sprite[3], self.mario.sprite[4], 11)
        elif self.mario.supermario == False and [self.mario.x, self.mario.y] not in self.colsup\
                and [self.mario.x, self.mario.y] not in self.suelo:
            pyxel.blt(self.mario.x, self.mario.y, 0, 32, 32, 16, 16, 6)
        # el mismo proceso que arriba solo que para Super Mario
        elif self.mario.supermario == True and [self.mario.x, self.mario.y] not in self.colsup \
                and [self.mario.x, self.mario.y] not in self.suelo:
            pyxel.blt(self.mario.x, self.mario.y - 16, 0, 56, 72, 16, 32, 6)
        elif self.mario.supermario == True:
            pyxel.blt(self.mario.x, self.mario.y-16, 0, 40, 72, 16, 32, 6)
        #Enemigos
        # esto imprime los enemigos si estan vivos.
        # si su type es goomba imprime un goomba sino imprime un koopa
        if self.e1.live:
            if self.typeenemy[0] == "goomba":
                pyxel.blt(self.e1.x, self.e1.y, 0, 48, 16, 16, 16, 6)
            else:
                pyxel.blt(self.e1.x, self.e1.y, 0, 24, 56, 16, 16, 6)
        if self.e2.live:
            if self.typeenemy[1] == "goomba":
                pyxel.blt(self.e2.x, self.e2.y, 0, 48, 16, 16, 16, 6)
            else:
                pyxel.blt(self.e2.x,  self.e2.y, 0, 24, 56, 16, 16, 6)
        if self.e3.live:
            if self.typeenemy[2] == "goomba":
                pyxel.blt(self.e3.x, self.e3.y, 0, 48, 16, 16, 16, 6)
            else:
                pyxel.blt(self.e3.x, self.e3.y, 0, 24, 56, 16, 16, 6)
        if self.e4.live:
            if self.typeenemy[3] == "goomba":
                pyxel.blt(self.e4.x, self.e4.y, 0, 48, 16, 16, 16, 6)
            else:
                pyxel.blt(self.e4.x, self.e4.y, 0, 24, 56, 16, 16, 6)
        #powerup este if imprime el powerup
        if self.seta.life:
            pyxel.blt(self.seta.x, self.seta.y, 0, 48, 0, 16, 16, 6)

