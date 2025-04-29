idade_eleitor = int(input("Digite a idade do eleitor: "))

if idade_eleitor < 16:
  print("Não pode votar")
  
elif idade_eleitor > 16 and idade_eleitor <= 17:
  print("Voto facultativo")
  
elif idade_eleitor >= 18 and idade_eleitor <= 65:
  print("Voto obrigatório")
  
elif idade_eleitor > 65:
  print("Não é obrigatório, mas pode votar")

else:
  print("Idade inválida")
