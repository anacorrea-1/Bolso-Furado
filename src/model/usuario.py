from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login: str, senha: str) -> bool:
        con, cur = Conexao.conectar()

        if not con:
            print("Erro ao tentar conectar!!")
            return False

        try:
            cur.execute("""
            INSERT INTO tb_usuarios (usuario, senha) VALUES (%s, %s)
            """, [login, senha])

            con.commit()
            con.close()

            return True 
        
        except Exception as e:
            print(f"ERRO AO INSERIR {e}")
            return False