from base import *

#TESTES DE FUNÇÕES

def main():
    print("1: inserir dados extraídos da api \n 2: listar todos os registros da coleção \n 3: listar os registros que batem com o parâmetro"
    "\n 4: alterar o primeiro registro que bate com o parâmetro \n 5: alterar mais de um campo do primeiro registro que bate com o parâmetro"
    "\n 6: alterar todos os registros que batem com o parâmetro \n 7: deletar o primeiro registro que bate com o parâmetro"
    "\n 8: deletar todos os registros que batem com o parâmetro \n 9: deletar todos os registros da coleção")
    opcao = int(input('Digite o número da opção que você deseja: '))
    if opcao == 1:
        data = get_api()
    elif opcao == 2:
        read_all()
    elif opcao == 3:
        read_many({"geral._id":"i6Oi-YtXnAU"})
    elif opcao == 4:
        update_one({"geral._id":"i6Oi-YtXnAU"}, {"geral._id": "20"})
    elif opcao == 5:
        update_one({"geral._id":"i6Oi-YtXnAU"}, {"geral._id": "20", "geral.Titulo":"mudando"})
    elif opcao == 6:
        update_many({"geral._id":"i6Oi-YtXnAU"}, {"geral._id": "20"})
    elif opcao == 7:
        delete_one({"geral._id":"i6Oi-YtXnAU"})
    elif opcao == 8:
        delete_many({"geral._id":"i6Oi-YtXnAU"})
    elif opcao == 9:
        delete_all()
    
    

if __name__=="__main__":
    main()
