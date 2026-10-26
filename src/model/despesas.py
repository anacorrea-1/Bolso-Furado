from src.database.conexao import Conexao


class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(id_categoria: int, descricao: str, valor: float, data_despesa: str, id_usuario: int) -> int:
        con, cur = Conexao.conectar()
        if not con:
            print('Erro ao tentar conectar')
            return None

        try:
            cur.execute("""
                        INSERT INTO tb_despesas (id_usuario, valor, data_despesa, descricao, id_categoria)
                        VALUES (%s, %s, %s, %s, %s)
                        """, (id_usuario, valor, data_despesa, descricao, id_categoria))
            id_despesa = cur.lastrowid
            con.commit()
            con.close()
            return id_despesa

        except Exception as e:
            print(f'Erro: {e}')
            return None