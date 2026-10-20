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

    @staticmethod
    def verificar(login: str, senha: str) -> dict:
        con, cur = Conexao.conectar()
        
        if not con:
            print("Erro ao tentar conectar!!")
            return False
        
        try:
            cur.execute(""" 
            SELECT id_usuario,usuario,senha 
            FROM tb_usuarios where usuario 
            = %s and senha = %s; """[login,senha])

            resu_select = cur.fetchone()
            resultado = {
                "login": resu_select[0][1],
                "senha": resu_select[0][1]
            }
            con.close()
            return resultado

        except Exception as e:
            print (f"Usuario ou Senha errados: {e}")
            return{}