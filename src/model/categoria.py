from src.database.conexao import Conexao
class Categoria:
    def __init__(self):
        pass
    @staticmethod
    def adicionar(categoria:str, id_usuario:int) -> int:
        con, cur = Conexao.conectar()
        if not con:
            print('Erro ao tentar conectar')
            return None
        
        try:
            cur.execute("""
                        INSERT INTO tb_categorias(id_usuario, nome)
                        values(%s, %s)
                        """, (id_usuario, categoria))
            id_cat = cur.lastrowid
            con.commit()
            con.close()
            return id_cat
    
        except Exception as e:
            print(f'Erro: {e}')
            return None
    
    @staticmethod
    def recuperar_todos(id_usuario:int) -> list[dict]:
        con, cur = Conexao.conectar()
        if not con:
            print('Erro ao tentar conectar')
            return None
        try:
            cur.execute("""
                        SELECT nome from tb_categorias
                        where id_usuario = %s;
                        """, (id_usuario,))
            categorias = cur.fetchall()
            con.close()
            return categorias
        
        except Exception as e:
            print(f'Erro: {e}')
            return None