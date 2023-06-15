import constantes
class Enemy:
    def __init__(self, x: int, y: int, genere: str, dir: str):
        """Este método crea el objeto Enemy
        @ param x posición x del enemigo
        @ param y posición y del enemigo
        @ param genere sirve para definir si es goomba o koopa
        @ param direction su dirección
        @ param live su vida
        @ param init lo inicializa"""
        self.x = x
        self.y = y
        self.genere = genere
        self.direction = dir
        self.live = True
        self.init = True
    def move(self, direction: str):
        # lo mueve en horizontal, su dirección depende de Tablero donde comprueba las colisiones laterales
        if direction == "left":
            self.x -= 1
        if direction == "right":
            self.x += 1
    def screen(self, move: False):
        # Hace que se mueva al igual que los bloques cuando Mario está en su centro. No usamos la misma
        # que los bloques porque daba fallos al colisionar el enemigo con los laterales.
        if move == True:
            self.x -= 2
    def gravity(self, collide: bool):
        # Hace que caiga cuando no colisiona con el suelo
        if collide:
            self.y += 4