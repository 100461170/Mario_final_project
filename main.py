# Aquí tendremos que importar la clase tablero y lo que nos haga falta
from tablero import Tablero
import constantes
import pyxel
Tablero = Tablero(constantes.ANCHO, constantes.ALTO)
# Lo primero que hay que hacer es iniciar la pantalla
pyxel.init(Tablero.width, Tablero.heigh, caption=constantes.CAPTION)

# cargar las imágenes.
pyxel.load("my_resource.pyxres")

# Para iniciar el juego, invocamos el método run con las funciones Update y Draw
pyxel.run(Tablero.update, Tablero.draw)
