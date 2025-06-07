QuantidadeDeFitas=50
Aluguel=10
MultaAtraso=int(50/10)
FaturamentoAnual=int((QuantidadeDeFitas/3)*12+MultaAtraso*12)

print(f"O faturamento Anual é de {FaturamentoAnual}")
print(f"O valor ganho com multas por mês é {MultaAtraso}")