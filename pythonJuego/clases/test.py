from clases import Explosion
import unittest
from unittest.mock import patch
import pygame
from tu_archivo import Juego  # Asegúrate de importar tu clase Juego y otras dependencias

class TestJuego(unittest.TestCase):

    @patch('builtins.input', return_value='NombreDePrueba')
    def test_main(self, mock_input):
        # Deshabilitamos la ventana de Pygame para evitar problemas en las pruebas de unidad
        pygame.display.init()
        pygame.display.set_mode((1, 1))

        # Ejecutamos la función main y probamos su comportamiento
        with self.assertRaises(SystemExit) as cm:
            main()

        # Verificamos que la excepción SystemExit sea lanzada (indicando que la ventana se cerró correctamente)
        self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main() 




class TestExplosion(unittest.TestCase):

    def setUp(self):
        # Configuramos Pygame para evitar problemas durante las pruebas
        pygame.init()

    def tearDown(self):
        # Limpiamos Pygame después de las pruebas
        pygame.quit()

    def test_explosion_update(self):
        explosion_anim = [pygame.Surface((32, 32))]  # Supongamos una animación con un solo cuadro
        center = (100, 100)
        explosion = Explosion(center, explosion_anim)

        # Simulamos el tiempo necesario para actualizar los cuadros de la animación
        pygame.time.set_timer(pygame.USEREVENT, explosion.frame_rate)

        # Realizamos varias actualizaciones para avanzar la animación
        for _ in range(len(explosion_anim) - 1):
            explosion.update()

        # Verificamos que la explosión se haya eliminado al finalizar la animación
        self.assertTrue(explosion not in pygame.sprite.Group())

if __name__ == '__main__':
    unittest.main()