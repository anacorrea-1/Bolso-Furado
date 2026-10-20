from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod    
    def adicionar(categoria: str, usuario: str) -> int:
        con, cur = Conexao.conectar()

        if not con:
            print("Erro ao tentar conectar!!")
            return False

        try:
            cur.execute("""
            INSERT INTO tb_categoria (id_usuario, nome) VALUES (%s, %s)
            """, [usuario, categoria])
        
            id_cate = cur.lastrowid
            con.commit()
            con.close()
        
            return id_cate
                
        except Exception as e:
            print(f"ERRO: {e}")
            return None
        
        