class Usuario: #criando a classe Usuario
    def __init__(self, nome, idade, sexo, peso, altura):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo 
        self._peso = peso
        self._altura = altura
    
    # Properties com getters e setters para encapsulamento e validacao dos atributos
    @property
    def nome(self): 
        return self._nome
    
    @nome.setter
    def nome(self, novo):
        if isinstance(novo, str) and novo:
            self._nome = novo
        else:
            raise ValueError("Tem que ser string")
    
    @property
    def idade(self): 
        return self._idade
    
    @idade.setter
    def idade(self, novo):
        if isinstance(novo, int) and novo >= 0:
            self._idade = novo
        else:
            raise ValueError("Tem que ser inteiro")    
 
    @property
    def sexo(self): 
        return self._sexo
    
    @sexo.setter
    def sexo(self, novo):
        if isinstance(novo, str) and novo in ['F', 'M']:
            self._sexo = novo
        else:
            raise ValueError("Tem que ser string")
        
    @property
    def peso(self): 
        return self._peso
    
    @peso.setter
    def peso(self, novo):
        if isinstance(novo, (int, float)) and novo > 0:
            self._peso = novo
        else:
            raise ValueError("Tem que ser float")    
    
    @property
    def altura(self): 
        return self._altura
    
    @altura.setter
    def altura(self, novo):
        if isinstance(novo, (int, float)) and novo > 0:
            self._altura = novo
        else:
            raise ValueError("Tem que ser float")
    
    @property
    def calculo_imc(self): #metodo que calcula o imc
        return self._peso / (self._altura ** 2) #formula do imc: peso dividido por altura ao quadrado
    
    def imprimir_dadosUsuario(self):
        print(f"Usuario: {self._nome}\nIdade: {self._idade} anos\nSexo: {self._sexo}\nPeso: {self._peso}kg\nAltura: {self._altura}m \nIMC: {self.calculo_imc:.2f}")