import modelo

lista_usuario = []
lista_filmes = []
lista_series = []

def cadastro_usuario():
    nome = input("Digite o nome de usuario: ")
    email = input("Email: ")
    senha = input("Senha: ")
    
    usuario = modelo.Usuario(nome, email, senha)
    
    lista_usuario.append(usuario)
    

while(True):
    print("======== Opções ========")
    print("= 1 - Cadastra Usuario =")
    print("========================")
    op = input()
    
    if op == "1":
        cadastro_usuario()
    else:
        break

print(len(lista_usuario))
for usuario in lista_usuario:
    print(usuario)