from usuario import Usuario #importando a classe Usuario
from imc import IMC #importando a classe IMC

#mensagem para orientar o usuario
print(f"Bem-Vindo! Calcule o seu IMC\n")

caleb = Usuario("Caleb", 18, 'M', 180.22, 1.50) #criando o objeto caleb com dados pessoais
caleb.imprimir_dadosUsuario() #imprimindo os dados do usuario

imc = IMC() #criando o objeto imc
imc.classificar(caleb.calculo_imc) #classificando o imc do usuario
imc.imprimir_classificacao() #imprimindo a classificacao do imc

