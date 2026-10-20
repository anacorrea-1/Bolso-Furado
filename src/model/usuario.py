from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login: str, senha: str) -> bool:
        con, cur = Conexao.conectar()
        con.execute("""
        INSERT INTO tb_usuarios (usuario, senha) VALUES (%s, %s)
        """, [login, senha])

        con.commit()
        con.close()

        return True 