# Convenção PEP-8 ~~~ Classes devem usar o "CapModel", cada palavra, começa
# com letra maiuscula

# Funções e variaveis devem usar somente letras minusculas e "_" espaços snake

# Constantes devem ser palavras maiusculas separadas por "_"
from typing import Dict, List, Union

from fila_base import FilaBase

from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self):
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'
    # Padrão Pep-8 ~~Uma linha de espaçamento entre métodos e funções

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente Atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        if flag != 'detail':
            estatistica[f'{agencia}-{dia}'] = len(self.clientes_atendidos)
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quanntidade clientes atendidos'] = (
                len(self.clientes_atendidos)
            )
        return estatistica
