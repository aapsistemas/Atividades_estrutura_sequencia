import math

# Solicita o tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcula a quantidade de tinta necessária considerando uma folga de 10%
litros_tinta = math.ceil(area / 6 * 1.1)

# Calcula a quantidade de latas de 18 litros necessárias
latas_18_litros = math.ceil(litros_tinta / 18)

# Calcula o preço total das latas de 18 litros
preco_latas_18_litros = latas_18_litros * 80.00

# Calcula a quantidade de galões de 3,6 litros necessários
galoes_3_6_litros = math.ceil(litros_tinta / 3.6)

# Calcula o preço total dos galões de 3,6 litros
preco_galoes_3_6_litros = galoes_3_6_litros * 25.00

# Calcula a quantidade de latas de 18 litros e galões de 3,6 litros necessários para minimizar o desperdício
latas_minimizadas = math.ceil(litros_tinta / 18)
galoes_minimizados = math.ceil((litros_tinta - latas_minimizadas * 18) / 3.6)

# Calcula o preço total das latas de 18 litros e galões de 3,6 litros minimizados
preco_minimizado = latas_minimizadas * 80.00 + galoes_minimizados * 25.00

# Exibe os resultados
print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas de 18 litros a serem compradas:", latas_18_litros)
print("Preço total: R$", preco_latas_18_litros)
print()

print("Situação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões de 3,6 litros a serem comprados:", galoes_3_6_litros)
print("Preço total: R$", preco_galoes_3_6_litros)
print()

print("Situação 3: Misturar latas de 18 litros e galões de 3,6 litros para minimizar o desperdício")
print("Quantidade de latas de 18 litros a serem compradas:", latas_minimizadas)
print("Quantidade de galões de 3,6 litros a serem comprados:", galoes_minimizados)
print("Preço total: R$", preco_minimizado)
