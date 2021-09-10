class Pessoa(object):
    nome = ""
    telefone = ""
    genero = ''

    def __init__(self, nm, tlf, gn):
        self.nome = nm
        self.telefone = tlf
        self.genero = gn

    def toString(self):
        return f"{self.genero}, {self.nome}, {self.telefone}"

    def validar(self):
        validacao = ""
        validacao += (self.nome == "") and "Nome Invalido" or ""
        validacao += (self.telefone == "") and "Telefone Invalido" or ""
        validacao += (self.genero == '') and "Genero Invalido" or ""
        return validacao

leonardo = Pessoa("Leonardo", "991341735", 'M')

print (leonardo.toString())

print(leonardo.validar())

