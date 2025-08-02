# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 09:16:21 2025

@author: andre
"""

import matplotlib.pyplot as plt
import time  # Importamos el módulo time para medir la duración

def collatz(n):
    """
    Calcula la secuencia de Collatz para un número dado y devuelve los pasos hasta llegar a 1.
    """
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:  # Si es par
            n = n // 2
        else:  # Si es impar
            n = 3 * n + 1
    secuencia.append(1)  # Añadir el último valor (1)
    return secuencia

def medir_tiempo_collatz(n):
    """
    Mide el tiempo que tarda en calcular la secuencia de Collatz para un número dado
    y devuelve tanto la secuencia como el tiempo de ejecución en segundos.
    """
    inicio = time.time()  # Registra el tiempo de inicio
    secuencia = collatz(n)
    fin = time.time()  # Registra el tiempo de finalización
    tiempo_ejecucion = fin - inicio
    return secuencia, tiempo_ejecucion

def collatz_con_grafica(n):
    """
    Genera una gráfica de la secuencia de Collatz y muestra información adicional
    incluyendo el tiempo de ejecución.
    """
    secuencia, tiempo = medir_tiempo_collatz(n)
    
    print(f"\nSecuencia para {n}:")
    print(" → ".join(map(str, secuencia)))
    print(f"\nTotal de pasos: {len(secuencia) - 1}")
    print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
    
    plt.figure(figsize=(10, 5))
    plt.plot(secuencia, 'ro-')
    plt.title(f"Secuencia 3x+1 para n = {n} (Tiempo: {tiempo:.6f} s)")
    plt.xlabel("Paso")
    plt.ylabel("Valor")
    plt.grid()
    plt.show()

# --- Programa principal ---
if __name__ == "__main__":
    numero = int(input("Ingrese un número entero positivo: "))
    if numero <= 0:
        print("¡Error! Debe ser un número positivo.")
    else:
        collatz_con_grafica(numero)