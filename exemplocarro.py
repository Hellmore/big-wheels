# Definindo a classe

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.velocidade_max = 200
        self.velocidade_min = 0

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10

    def freiar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10


# Criando instancia

palio = Carro("prata", "palio")
vectra = Carro("preto", "vectra")
fusca = Carro("azul", "fusca")

# Ligando carro

palio.ligar()
vectra.ligar()

print("Palio esta ligado?: {}".format(palio.ligado))
print("Vectra esta ligado?: {}".format(vectra.ligado))

# Acelerando e freiando

for _ in range(10):
    palio.acelerar()

print("Palio: velocidade é {}".format(palio.velocidade))
print("Vectra: velocidade é {}".format(vectra.velocidade))

for _ in range(10):
    palio.freiar()

print("Palio: velocidade é {}".format(palio.velocidade))
print("Vectra: velocidade é {}".format(vectra.velocidade))
