import mysql.connector

class Conexao:
    def __init__(self):
        pass

    # o @staticmethod mostra que a função não precisa de atributos para funcionar  
    @staticmethod
    def conectar() -> list:
        try:
            #Conectando ao banco de bados
            conexao = mysql.connector.connect(
                host="127.0.0.1",
                port= "3306",
                user="root",
                password="root",
                database = "bolso_furado")
            cursor = conexao.cursor()
            
            return conexao, cursor

        except Exception as e:
            print(e)
            return None, None