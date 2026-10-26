from src.model.despesas import Despesa

resultado = Despesa.incluir(1, 'Saida para o shopping', 80, '2026-10-06', 1)

print(resultado)