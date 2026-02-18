import base64
from stream_cipher import decifrar, cifrar
#hecho con chat: https://chatgpt.com/share/698e729c-aba0-800f-8104-f5303d1999fb (ultimo mensaje)
def ejemplo(mensaje: str, clave: int):
    cifrado = cifrar(mensaje, clave)
    descifrado = decifrar(cifrado, clave).decode("utf-8")

    print("=" * 60)
    print(f"Texto plano:        {mensaje}")
    print(f"Clave utilizada:    {clave}")
    print(f"Cifrado (hex):      {cifrado.hex()}")
    print(f"Cifrado (base64):   {base64.b64encode(cifrado).decode()}")
    print(f"Texto descifrado:   {descifrado}")

if __name__ == "__main__":
    ejemplo("Tarea cargada", 1428)
    ejemplo("Hola mundo", 2026)
    ejemplo("Cifrado de flujo con XOR", 999)
