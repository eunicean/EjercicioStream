from stream_cipher import generateKeystream, cifrar, decifrar


print("\n==================================")
print("  ENCRIPTACIÓN Y DESENCRIPTACIÓN")
print("================================\n")

mensaje = input("Ingresa tu MENSAJE a encriptar\n   → ")
clave = input("Ingresa la clave para generar el KEYSTREAM\n   → ")

print("\n--- VERIFICANDO QUE KEYSTREAM SIEMPRE ES EL MISMO ---\n  Generando 10 llaves")
# para la función all, la voy a simplificar para no realizar una función
# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-equal 
keystreamList = []
for x in range(10): keystreamList.append(generateKeystream(len(mensaje), clave))
if all(keystreamList[0] == x for x in keystreamList): print("  → Todas las llaves son iguales :)")
else: print("  → No todas las llaves son iguales")

print("\n--- ENCRIPTANDO---")
cifrado = cifrar(mensaje,clave)

print("\n--- DESENCRIPTANDO ---")
decifrado = decifrar(cifrado, clave)

print("\n--- COMPARANDO ---")
if mensaje.encode('utf-8') == decifrado: print("  Cifrado y decifrado funcionan correctamente\n")
else: print("  Cifrado y decifrado NO funcionan correctamente\n")

