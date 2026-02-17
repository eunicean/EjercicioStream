# Ejercicio Stream de cifrados

Es este ejercicio se realizó un stream cipher usando operaciones básicas como la generación de un keystream y XOR de bytes.

## Archivos
- [Stream cipher](stream_cipher.py)

## Instalación y uso
### **Requisitos**
- Python

### **Instalación**
Clonar repo
```
git clone https://github.com/eunicean/EjercicioStream
```

### **Uso**

**Prueba básica de las funciones**
```
python stream_cipher.py
```
Variables a cambiar 
```python
clave = 1428
texto = "Tarea cargada"
```
---
**Prueba con mensaje personalizado**

Correr el programa
```bash
python tests.py
```
Ingresar los valores deseados cuando se soliciten:
```bash
Ingresa tu MENSAJE a encriptar
   → (MENSAJE DESEADO)
Ingresa la clave para generar el KEYSTREAM
   → (NUMERO DESEADO)
```

Luego verá el proceso que cada función realizó