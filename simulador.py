import random
import math
import matplotlib.pyplot as plt

# Simula geração solar (0-100%) e consumo residencial (50-80%)
def simular_dados(hora):
    solar = 100 * abs(math.sin(hora * math.pi / 12))  # Pico ao meio-dia
    consumo = 50 + 30 * random.random()  # Variação aleatória
    return solar, consumo

# Algoritmo de decisão
def decidir_fonte(solar, consumo):
    if solar >= consumo * 1.1:
        return "SOLAR", solar - consumo
    elif solar >= consumo * 0.5:
        return "HÍBRIDO", 0
    else:
        return "REDE", 0

# Teste para 24 horas
horas = range(24)
resultados = [decidir_fonte(*simular_dados(h)) for h in horas]

# Plotagem
plt.plot(horas, [r[1] for r in resultados], label="Excedente Solar")
plt.xlabel("Hora do Dia")
plt.ylabel("Energia (W)")
plt.legend()
plt.savefig("resultado.png")
