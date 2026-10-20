from src.model.categoria import Categoria
from src.model.usuario import Usuario

print(Usuario.cadastrar('Anaclara','123'))
user = Usuario.verificar('Anaclara','123')
print(user)
id_cat = Categoria.adicionar('Entretenimento', user['id_usuario'])
print(id_cat)