from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_igor = ContaSalario(36)
conta_igor.deposita(100)
conta_cecilia = ContaSalario(7)
conta_cecilia.deposita(100)
conta_cady = ContaSalario(40)
conta_cady.deposita(100)
contas = [conta_igor, conta_cecilia, conta_cady]

print(conta_igor >= conta_cady)

# for conta in sorted(contas):
#     print(conta)