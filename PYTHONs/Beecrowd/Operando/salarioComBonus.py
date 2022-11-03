nome_vendedor = str(input())
fixo = float(input())
total_vendas = float(input())

salario_total = (fixo + total_vendas*0.15)

print("TOTAL = R$ {:.2f}".format(salario_total))
