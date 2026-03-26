# Passo 1: Entrada de dados
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do(a) {nome_aparelho} em watts (W): "))
horas_dia = float(input(f"Quantas horas por dia o(a) {nome_aparelho} fica ligado(a)? "))

# Passo 2: Cálculo do consumo mensal (considerando 30 dias)
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Passo 3: Exibição do resultado formatado
print("-" * 40)
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print("-" * 40)