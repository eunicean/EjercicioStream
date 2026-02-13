import random

def generateKeystream(size: int, clave: int):
    random.seed(clave)
    key = []

    for i in range(size):
        key.append(random.randint(0, 255))
    
    return key

def cifrar(mensaje: str, clave: int) -> bytes:
    print(f"Mensaje recibido: {mensaje}")
    mensaje_bytes = mensaje.encode('utf-8')
    print(f"Mensaje en bytes: {mensaje_bytes}")

    keystream = generateKeystream(len(mensaje_bytes), clave)
    print(f"Keystream: {keystream}")

    mensaje_cifrado = bytes([mb ^ ks for mb, ks in zip(mensaje_bytes, keystream)])
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    return mensaje_cifrado

texto = "Tarea cargada"
cifrar(texto, 15)