# Flake8 - Checador de estilo de código

# Flake8 com o comando --select codigo_erro, pode pesquisar
# por somente um tipo de erro

# Flake8 com o comando --ignore codigo_erro, pode ignorar
# por um tipo de erro

# Você pode pre-configurar o flake8

# Version Control Hook, ou seja, algo built-in que irá aplicar
# um padrão na evolução do código
from fila_base import FilaBase


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senhatual = f'NM{self.codigo}'

    # type hint, não retorna nada
    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senhatual)

    # type hint, retorna string
    def chamacliente(self, caixa: int) -> str:
        # .pop() retorna o valor
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
