import random

def generateKeystream(size: int, clave: int):
    random.seed(clave)
    key = []

    for i in range(size):
        key.append(random.randint(0, 255))
    
    return key

# Referencia de chat para arreglar error básico y mejorar zip:   
# https://chatgpt.com/share/698e729c-aba0-800f-8104-f5303d1999fb
def cifrar(mensaje: str, clave: int) -> bytes:
    print(f"Mensaje recibido: {mensaje}")
    mensaje_bytes = mensaje.encode('utf-8')
    print(f"Mensaje en bytes: {mensaje_bytes}")

    keystream = generateKeystream(len(mensaje_bytes), clave)
    print(f"Keystream: {keystream}")

    mensaje_cifrado = bytes([mb ^ ks for mb, ks in zip(mensaje_bytes, keystream)])
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    return mensaje_cifrado

def decifrar(mensaje_cifrado: bytes, clave: int) -> str:
    keystream = generateKeystream(len(mensaje_cifrado), clave)
    print(f"Keystream para desencriptar: {keystream}")

    mensaje_descifrado = bytes([mb ^ ks for mb, ks in zip(mensaje_cifrado, keystream)])
    print(f"Mensaje desencriptado: {mensaje_descifrado}")

    return mensaje_descifrado


clave = 1428
texto = "Tarea cargada"
cifrado = cifrar(texto, clave)
decifrar(cifrado, clave)

