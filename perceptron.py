def soma(w, x):
    d = w[0]  # Inicializa com o viés (bias)
    for i in range(1, 6):  # Itera de 1 a 5
        d += w[i] * x[i]  # Soma ponderada dos pesos e entradas
    return d

def ativacao(d):
    return 1 if d >= 0 else -1  # Função degrau (threshold)

# Exemplo de uso:
w = [0.2, -0.4, 0.6, -0.3, 0.5, -0.7]  # Pesos (incluindo o bias em w[0])
x = [1, 0.1, 0.9, -0.6, 0.2, -0.8]    # Entradas (x[0] normalmente é 1 para o bias)

d = soma(w, x)
o = ativacao(d)

print(f"Saída intermediária (d): {d}")
print(f"Saída ativada (o): {o}")
