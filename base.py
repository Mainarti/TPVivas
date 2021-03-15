# _*_ coding: utf-8 -*_

from pymongo import MongoClient
import requests
from googleapiclient.discovery import build

client = MongoClient('mongodb+srv://amanda:aof123456@projetosd.gxvil.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.learnObjects
coll = db.testes

#pega e retorna os dados da api do youtube
def get_api():
    api_key = "AIzaSyAIKVPDKfnmrHCOFPIHLJkH7cfgr0ejX5I"
    youtube = build('youtube', 'v3', developerKey = api_key)
    request = youtube.videos().list(
        part = 'id, snippet,contentDetails, statistics, status',
        id = 'i6Oi-YtXnAU'
    )
    response = request.execute()
    data = response.get("items")
    for item in data:
        entrada = {
        "geral":{
            "_id":item["id"],
            "Titulo":item.get("snippet")["title"],
            "Keywords":item.get("snippet")["tags"],
            "Descrição":item.get("snippet")["description"]
        },
        "ciclo_de_vida":{
            "versao": "youtube v3",
            "status": item.get("status")["uploadStatus"],
            "contribuinte": {
                "entidade": None,
                "data": None,
                "papel": None
	        }
	    },
        "meta_metadados":{
            "identificador": {
                "catalogo": None,
                "entrada": None
            },
            "contribuinte": {
                "entidade": "Youtube",
                "data": None,
                "papel": None,
            },
            "esquema_de_metadados": "IEEE LOM",
            "idioma": "Português"
        },
        "metadados_tecnicos" :{
            "formato": "video",
            "tamanho": None,
            "localizacao":"https://youtube.com/S9uPNppGsGo&t" ,
            #"requisitos": item.get("contentDetails")["regionRestriction"]["allowed"],
            "observacoes_de_Instalacoes": None,
            "outros_requisitos_de_sistema": None,
            "duracao": item.get("contentDetails")["duration"]
        },
	    "aspectos_educacionais": {
            "tipo_de_interatividade": "Nenhuma",
            "tipo_de_recurso_de_aprendizado": item.get("kind"),
            "nivel_de_interatividade": "Pequena",
            "densidade_semantica": "Alta",
            "usuario_final": "Público geral",
            "contexto_de_aprendizagem": "Programação",
            "idade_recomendada": "None",
            "grau_de_dificuldade": "Medio",
            "tempo_de_aprendizado": "Relativo",
            "descricao": None,
            "linguagem": "Português"
	    },
	    "direitos" : {
            "custo": 0.0,
            "direitos_autorais": "Domínio público",
            "descricao": None
        },
	    "relacoes" : {
            "genero": "Fontes Externas",
            "recurso": {
                "referencias": None,
                "links_externos": None,
            }
        },
	    "classificacao" : {
            "finalidade": "Video Aula",
            "diretorio": "https://youtube.com/S9uPNppGsGo&t",
            "descricao": item.get("snippet")["description"],
            "Keywords":item.get("snippet")["tags"],
	    },
	    "conteudo" : {
            "data": item.get("snippet")["publishedAt"],
            "entidade": item.get("snippet")["channelTitle"],
            "imagens": item.get("snippet")["thumbnails"],
            "comentarios": item.get("statistics")["commentCount"],
        }
	    }
        create_one(entrada) #inserindo json
    print(entrada)


#insere um registro na coleção
def create_one(input):
    insert = coll.insert_one(input)
    print(insert.inserted_id)

#insere vários registros na coleção
def create_many(input):
    insert = coll.insert_many(input)
    print(insert.inserted_ids)

#consulta e retorna o primeiro registro da coleção
def read_one():
    read = coll.find_one()
    print(read)

#consulta e retorna registros que cumprem o parâmetro
def read_many(filter):
    for read in coll.find(filter):
        print(read)

#consulta e retorna todos os registros da coleção
def read_all():
    for read in coll.find():
        print(read)

#altera o primeiro registro que bate com o parâmetro
def update_one(filter, newValue):
    update = coll.update_one(filter, {"$set":newValue})
    read_all()

#altera todos os registros que batem com o parâmetro
def update_many(filter, newValues):
    update = coll.update_many(filter, {"$set": newValues})
    print(update.modified_count, "Documentos alterados")
    read_all()

#deleta o primeiro registro que bate com o parâmetro
def delete_one(filter):
    delete = coll.delete_one(filter)

#deleta um ou mais registros de acordo com o parâmetro
def delete_many(filter):
    delete = coll.delete_many(filter)
    print(delete.deleted_count, "Documentos deletados")

#deleta todos os registros da coleção
def delete_all():
    delete = coll.delete_many({})
    print(delete.deleted_count, "Documentos deletados")