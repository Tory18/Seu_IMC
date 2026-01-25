# Calculadora de IMC

Um programa simples em Python que calcula o Índice de Massa Corporal (IMC) e classifica o resultado.

## Funcionalidades

- Criar perfil de usuário com dados pessoais (nome, idade, sexo, peso, altura)
- Calcular IMC automaticamente
- Classificar o resultado em categorias (Magreza, Normal, Sobrepeso, Obesidade, Obesidade Grave)

## Estrutura do Projeto

```
Seu IMC/
├── main.py          # Arquivo principal - executa o programa
├── usuario.py       # Classe Usuario - gerencia dados do usuário
├── imc.py          # Classe IMC - calcula e classifica o IMC
└── README.md       # Este arquivo
```

## Como Usar

1. Execute o programa:
```bash
python main.py
```

2. O programa criará um usuário de exemplo e exibirá:
   - Dados como nome, idade, sexo, peso, altura
   - Cálculo do IMC
   - Seu do resultado

## Exemplo de Saída

```
Bem-Vindo! Calcule o seu IMC

Usuario: Caleb
Idade: 18 anos
Sexo: M
Peso: 75.8kg
Altura: 1.81m
IMC: 23.13

Sua Classificacao é: NORMAL
```

## Classes

### `Usuario`
Gerencia os dados do usuário com validação:
- `nome`: string não vazio
- `idade`: inteiro >= 0
- `sexo`: 'F' ou 'M'
- `peso`: número > 0
- `altura`: número > 0
- `calculo_imc`: property que retorna o IMC calculado

### `IMC`
Classifica o IMC do usuário:
- `classificar(imc_valor)`: classifica o IMC em faixas
- `imprimir_classificacao()`: exibe o resultado

## Classificacoes de IMC

| Faixa de IMC | Classificacao |
|--------------|---------------|
| < 18.5       | Magreza       |
| 18.5 - 24.9  | Normal        |
| 25 - 29.9    | Sobrepeso     |
| 30 - 39.9    | Obesidade     |
| >= 40        | Obesidade Grave |




## Requisitos

- Python 3.7+







