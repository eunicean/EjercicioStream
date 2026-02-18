import unittest

# importa tus funciones desde tu archivo
# si tu archivo se llama ejerciciosClase.py, sería:
from stream_cipher import cifrar, decifrar

class TestStreamCipher(unittest.TestCase):

    def test_descifrado_recupera_original(self):
        clave = 1428
        mensaje = "Prueba de descifrado exacto"
        cifrado = cifrar(mensaje, clave)
        descifrado = decifrar(cifrado, clave).decode("utf-8")
        self.assertEqual(descifrado, mensaje)

    def test_diferentes_claves_dan_cifrados_diferentes(self):
        mensaje = "Mismo mensaje"
        c1 = cifrar(mensaje, 1111)
        c2 = cifrar(mensaje, 2222)
        self.assertNotEqual(c1, c2)

    def test_misma_clave_mismo_cifrado_determinismo(self):
        mensaje = "Mensaje determinista"
        clave = 777
        c1 = cifrar(mensaje, clave)
        c2 = cifrar(mensaje, clave)
        self.assertEqual(c1, c2)

    def test_mensajes_diferentes_longitudes(self):
        clave = 555
        mensajes = [
            "",
            "a",
            "hola",
            "Este es un mensaje más largo para probar longitudes.",
            "Texto con caracteres especiales: ñáéíóú 😄"
        ]

        for m in mensajes:
            cifrado = cifrar(m, clave)
            descifrado = decifrar(cifrado, clave).decode("utf-8")
            self.assertEqual(descifrado, m)

if __name__ == "__main__":
    unittest.main()