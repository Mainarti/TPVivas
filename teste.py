from base import *

def main():
    print("1: inserir dados extraídos da api")
    print("2: lista todos os registros da coleção")
    print("3: listar os registros que batem com o parâmetro")
    print("4: alterar o primeiro registro que bate com o parâmetro")
    print("5: alterar todos os registros que batem com o parâmetro")
    print("6: deletar o primeiro registro que bate com o parâmetro")
    print("7: deletar todos os registros que batem com o parâmetro")
    print("8: deletar todos os registros da coleção")
    opcao = int(input('Digite o número da opção que você deseja: '))
    if opcao == 1:
        data = get_api()
    elif opcao == 2:
        read_all()
    elif opcao == 3:
        read_many({'x':1})
    elif opcao == 4:
        update_one({"_id":"i6Oi-YtXnAU"}, {"_id": "20"})
    elif opcao == 5:
        update_many({"nome":"amanda"},{"nome":"teste"})
    elif opcao == 6:
        delete_one({"x": 1})
    elif opcao == 7:
        delete_many({"nome": "amanda"})
    elif opcao == 8:
        delete_all()
    
    

if __name__=="__main__":
    main()
