import pygame
import sys

from clases.conexion import Conexion
from clases.juego import Juego
from clases.variables import ancho, alto

def main():

    pygame.init()
    pygame.mixer.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("JUEGO ")
    clock = pygame.time.Clock()
    juego = Juego()
    done=False
    player_name = juego.mostrar_pantalla_inicio(ventana)
    juego.set_player_name(player_name)
    while not done:
        juego.vista_ventana(ventana)
        juego.logica()
        done= juego.eventos()
        clock.tick(60)

if __name__=="__main__":
    main()
