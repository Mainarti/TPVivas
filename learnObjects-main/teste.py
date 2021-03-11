import requests
from base import *


response = requests.get(url = "https://jsonplaceholder.typicode.com/todos")
data = response.json()


#       TESTES      #

#mostra os bancos de dados existentes
#print(client.list_database_names())

#mostra as coleções existentes no banco de dados
#print(db.list_collection_names())

#insere um registro na coleção
#create_one({"nome": "amanda"})
#create_one(data) #inserindo json

#insere vários registros na coleção
#create_many([{"name": "testando", "numero":"1"},{"name": "testando", "numero":"2"},{"name": "testando", "numero":"3"}])
#create_many(data) #inserindo json

#consulta e retorna o primeiro registro da coleção
#read_one()

#consulta e retorna todos os registros da coleção
#read_all()

#consulta e retorna registros que cumprem o parâmetro
#read_many({'x':1})
#read_many({"nome":{"$regex": "^a"}}) #documentos que o nome começa com a letra a

#altera o primeiro registro que bate com o parâmetro
#update_one({"userId":2}, {"userId": 20})

#altera todos os registros que batem com o parâmetro
#update_many({"nome":"amanda"},{"nome":"teste"})

#deleta o primeiro registro que bate com o parâmetro
#delete_one({"x": 1})

#deleta um ou mais registros de acordo com o parâmetro
#delete_many({"nome":{"$regex": "^a"}}) #documentos que o nome começa com a letra a
#delete_many({"nome": "amanda"}) #documentos com o nome espeficicado

#deleta todos os registros da coleção
#delete_all()