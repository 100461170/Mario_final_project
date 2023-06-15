class Powerup:
    def __init__(self, x: int, y:int, life:bool, dir:str):
        """Este método crea el objeto power up
        @ param x inicializa la posición x de Power up
        @ param y inicializa la posición y de Power up
        @ life es su "vida" osea si se imprime o no
        @ direction dirección
        @ init sirve para inicializarlo"""

        self.x = x
        self.y = y
        self.life = life
        self.direction = dir
        self.init = True
    def move(self, direction: str):
        # igual que el movimiento de Mario solo que en el tablero depende de las colisiones no de los botones
        if direction == "left":
            self.x -= 1
        if direction == "right":
            self.x += 1
    def screen(self, move: False):
        # hace que se mueva al igual que los bloques cuando Mario está en su centro. No usamos la misma
        # que los bloques porque daba fallos al colisionar la seta con los laterales.
        if move == True:
            self.x -= 2
    def gravity(self, collide: bool):
        # Hace que caiga cuando no colisiona con el suelo
        if collide:
            self.y += 4
