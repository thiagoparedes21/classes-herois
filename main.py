

class Hero:
    def __init__(self, nome_heroi, idade_heroi, tipo_heroi):
        self.nome = nome_heroi
        self.idade = idade_heroi
        self.tipo = tipo_heroi

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        else:
            ataque = "ataque desconhecido"

        return f"o {self.tipo} atacou usando {ataque}"

lista_herois = [
    Hero("Jorginho", 1000, "mago"),
    Hero("Cleiton", 38, "ninja"),
    Hero("Paulinho", 46, "monge"),
    Hero("Robson", 51, "guerreiro")
]

for hero in lista_herois:
    print(hero.atacar())


                

