# Flake8 - Checador de estilo de código
# Flake8 com o comando --select codigo_erro, pode pesquisar por somente um tipo de erro
# Flake8 com o comando --ignore codigo_erro, pode ignorar por um tipo de erro
# Você pode pre-configurar o flake8
# Version Control Hook, ou seja, algo built-in que irá aplicar um padrão na evolução do código

class FilaNormal:
    # type hint
    codigo: int = 0
    fila = []
    clientesatendidos = []
    # type hint
    senhatual: str = ""
    # type hint, não retorna nada
    def gerasenhaatual(self)->None:
        self.senhatual = f'NM{self.codigo}'
    # type hint, não retorna nada
    def resetafila(self)->None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
    # type hint, não retorna nada
    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)
                        #type hint, retorna string
    def chamacliente(self, caixa:int)->str:
                        #.pop() retorna
        cliente_atual = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
