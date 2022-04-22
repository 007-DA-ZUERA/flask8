# Convenção PEP-8 ~~~ Classes devem usar o "CapModel", cada palavra, começa
# com letra maiuscula

# Funções e variaveis devem usar somente letras minusculas e "_" espaços snake
from fila_base import FilaBase


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self):
        self.senha_atual = f'PR{self.codigo}'
    # Padrão Pep-8 ~~Uma linha de espaçamento entre métodos e funções

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente Atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quanntidade clientes atendidos'] = (
                len(self.clientes_atendidos)
            )
        return estatistica
