import random
import time

def monitorear_servidor(umbral=80):
    """Simula la carga del servidor y genera una alerta si supera el umbral."""
    carga = random.randint(30, 100)  # Genera un valor aleatorio entre 30% y 100%
    print(f"Carga del servidor: {carga}%")
    
    if carga > umbral:
        print("ALERTA: La carga del servidor ha superado el 80%")
    else:
        print("Estado normal.")

# Simulación con varias ejecuciones
for _ in range(3):  # Ejecuta el monitoreo 3 veces
    monitorear_servidor()
    time.sleep(2)  # Espera 2 segundos entre cada medición
