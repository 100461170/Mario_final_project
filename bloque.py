import constantes
class Bloque:
    def __init__(self, x : int, y : int, dir:bool):
        """Este método crea la clase bloque
        @ param x será una variable que se inicializa en 0 y aumentará según Mario esté en el centro
        de la pantalla para que esta se reste a la x de todos los objetos y de la sensación de que la pantalla se mueva
        También se aplica a los colliders
        @ param y su posición y
        @ direction sin uso
        """
        self.x = 0
        self.y = y
        self.direction = dir
        self.sprite = constantes.BLOQUE_SPRITE
    def move(self, direction: str):
        # Cuando Mario llegue a la mitad de la pantalla desde Tablero se transmitirá direction como left
        # y entonces self.x comenzará a aumentar de dos en dos. Esta variable se resta a todas las posiciones x
        # de los bloques y colliders para que dé la sensación de que la cámara se mueve. Nótese que aumenta de
        # dos en dos, al igual que la posición x de Mario para que de la sensación de misma velocidad.
        if direction.lower() == "left":
            self.x += 2

