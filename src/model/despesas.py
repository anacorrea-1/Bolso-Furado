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

    @staticmethod
    def recuperar_todos(id_usuario: int) -> list[dict]:
        con, cur = Conexao.conectar()
        if not con:
            print('Erro ao tentar conectar')
            return None
        
        try:
            cur.execute("""
                SELECT d.id_despesa, d.id_categoria, c.nome AS categoria,
                d.descricao, d.valor, d.data_despesa
                FROM tb_despesas d LEFT JOIN tb_categoria c
                ON c.id_categoria = d.id_categoria
                AND c.id_usuario = d.id_usuario
                WHERE d.id_usuario = %s
                ORDER BY d.data_despesa DESC, d.id_despesa DESC;
                """, (id_usuario,))
            
            despesas = cur.fetchall()
            con.close()
            return despesas
        
        except Exception as e:
                    print(f'Erro: {e}')
                    return None

    @staticmethod
    def recuperar_por_categoria(id_categoria: int, id_usuario: int) -> list[dict]:
        con, cur = Conexao.conectar()
        if not con:
            print('Erro ao tentar conectar')
            return None

        try:
            cur.execute("""
                        SELECT d.id_despesa, d.id_categoria, c.nome AS categoria,
                        d.descricao, d.valor, d.data_despesa
                        FROM tb_despesas d
                        LEFT JOIN tb_categoria c
                        ON c.id_categoria = d.id_categoria
                        AND c.id_usuario = d.id_usuario
                        WHERE d.id_usuario = %s AND d.id_categoria = %s
                        ORDER BY d.data_despesa DESC, d.id_despesa DESC;
                        """, (id_usuario, id_categoria))
            despesas = cur.fetchall()
            con.close()
            return despesas

        except Exception as e:
            print(f'Erro: {e}')
            return None

    def excluir(id_despesa:int) -> bool:
            con, cur = Conexao.conectar()
            if not con:
                print('Erro ao tentar conectar')
                return None
            try:
                cur.execute("""
                            delete from tb_despesas
                            where id_despesa = %s;
                            """, (id_despesa,))
                con.commit()
                con.close()
                return True
            
            except Exception as e:
                print(f'Erro: {e}')
                return None