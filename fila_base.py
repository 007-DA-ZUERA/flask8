class FilaBase:
    # type hint
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    # type hint
    senha_atual: str = ""

    # type hint, não retorna nada
    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1
