import constantes
class Mario:
    #Esta clase almacena toda la información necesaria para Mario
    def __init__(self, x : int, y: int, dir:bool, inicio: int):
        """Este método crea el objeto Mario
        @ param x inicializa la posición x de Mario
        @ param y inicializa la posición y de Mario
        @ param dir es un booleano que indica la dirección de
        Mario de izquierda a derecha
        @ param up sirve para iniciar el salto, claramente se inicia como False
        @ param inicio guarda la posición y de Mario en el momento de pulsar la flecha de arriba
        @ param perm sirve para dar permiso a todos los bloques de moverse
        @ param sprite las constantes de Mario
        @ param coins
        @ param bloqueinf, colleft, colright son las listas con las coordenadas de colisiones inicializadas vacías"""
        self.x = x
        self.y = y
        self.up = False
        self.inicio = inicio
        self.perm = False
        self.direction = dir
        self.sprite = constantes.MARIO_SPRITE
        self.bloqueinf = []
        self.colleft = []
        self.colright = []
        self.coins = 0
        self.supermario = False
    def move(self, direction: str, size: int):
        # Este es un ejemplo de método que mueve a Mario,
        # recibe la dirección y el tamaño del tablero
        # Se mueve en horizontal
        mario_x_size = self.sprite[3]
        if direction.lower() == "right" and self.x < size / 2 - mario_x_size:
            # excepción de colisiones
            if [self.x,self.y] not in self.colleft:
                self.x = self.x+2

        elif direction.lower() == "left" and self.x > 0:
            # excepción de colisiones
            if [self.x, self.y] not in self.colright:
                self.x -= 2
        # Si Mario x no es menor que la mitad de la pantalla la variable perm será True y en Tablero
        # permitirá el movimiento de todos los bloques dando la sensación de que la cámara se mueve.
        if not self.x < size / 2 - mario_x_size:
            self.perm = True
        else:
            self.perm = False

    def jump(self, jump):
    # cuando jump sea up y la posición y de mario + 56 sea distinto de la inicial bajará.
        if jump == "up" and self.y + 56 != self.inicio:
            self.y -= 4
            # Esto es para golpear con la cabeza los bloques
            if [self.x,self.y] in self.bloqueinf:
                self.up = False
                if jump == "down":
                    self.y += 4
        else:
            # Cuando lo anterior se incumple entonces bajará
            self.up = False
            if jump == "down":
                self.y += 4









