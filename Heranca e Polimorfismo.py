from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    def passa_o_mes(self):
        self._saldo += 2

# conta_igor77 = ContaInvestimento(99)
# print(conta_igor77)

# conta_igor88 = ContaPoupanca(88)
# conta_igor88.deposita(1000)
# conta_igor88.passa_o_mes()
# print(conta_igor88)
# #
# conta_igor99 = ContaCorrente(99)
# conta_igor99.deposita(1000)
# conta_igor99.passa_o_mes()
# print(conta_igor99)

conta_igor77 = ContaInvestimento(77)
conta_igor77.deposita(1000)
conta_igor88 = ContaPoupanca(88)
conta_igor88.deposita(1000)
conta_igor99 = ContaCorrente(99)
conta_igor99.deposita(1000)

contas = [conta_igor88, conta_igor99, conta_igor77]

for conta in contas:
    conta.passa_o_mes()
    print(conta)