class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

class ContaCorente(Conta):
    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Cogigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaSalario(Conta):
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Cogigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaMultiSalario(ContaSalario):
    pass


conta_igor1 = ContaSalario(789)
conta_igor1.deposita(100)
conta_igor2 = ContaMultiSalario(789)
conta_igor2.deposita(100)

condicao = conta_igor1 == conta_igor2
print(condicao)