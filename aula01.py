# Declaração de variaveis 
curso = 25
alunos = curso
curso = "Analista de Dados"
media_nota = 8.5
ativo = True 
# exibindo os valores 
print(curso, alunos, ativo)

valor = float(input("Digite um valor de acordo com o seu desejo:"))
desejo = input("Digite o seu maior desejo:")
if valor >= 1.000 or valor <= 2.000 and valor < 1.000:
    print("Seu desejo sera atendido!")
elif valor > 2.000 and valor <= 3.000:
    print("Seu deseja passara por analise!")
elif valor > 3.000: 
 print("Seu desejo esta acima do esperado, tente outra vez!")


