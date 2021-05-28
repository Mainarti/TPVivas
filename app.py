from flask import Flask, render_template, request, redirect, url_for, Response
import json
from bson import ObjectId, json_util
from bson.json_util import dumps
from base import *
import os
import re


app = Flask(__name__)

#renderiza página inicial mostrandos todos os registros
@app.route('/')
def index():
    result = read_all()
    return render_template('index.html', resultados=result)

#busca por registro que contenha a string buscada
@app.route('/search', methods=['GET'])
def search():
    param = request.values.get('search')
    param = re.escape(param)
    if not param:
        result = None
    else:
        result = read_many({'geral.titulo': {"$regex":param, "$options": "i"}})
        if result.count() == 0:
            result = None
        
    return render_template('index.html', resultados=result)

#encaminha para a página de busca avançada
@app.route('/searching')
def searching():
    return render_template('search.html')

#renderiza a página inicial passando o resultado da busca avançada
#(pesquisa por registros que batem com os parâmetros id, titulo e descrição passados)
@app.route('/advanced_search', methods=['GET'])
def advanced_search():
    cod = request.values.get('cod')
    title = request.values.get('title')
    description = request.values.get('description')

    cod = re.escape(cod)
    title = re.escape(title)
    description = re.escape(description)

    if not cod and not title:
        result = read_many({'geral.descricao': {"$regex":description, "$options": "i"}})
    elif not cod and not description:
        result = read_many({'geral.titulo': {"$regex":title, "$options": "i"}})
    elif not title and not description:
        result = read_many({'geral._id': {"$regex":cod, "$options": "i"}})
    elif not cod:
        result = read_many({'geral.titulo': {"$regex":title, "$options": "i"},'geral.descricao': {"$regex":description, "$options": "i"}})
    elif not title:
        result = read_many({'geral._id': {"$regex":cod, "$options": "i"} ,'geral.descricao': {"$regex":description, "$options": "i"}})
    elif not description:
        result = read_many({'geral._id': {"$regex":cod, "$options": "i"}, 'geral.titulo': {"$regex":title, "$options": "i"},'geral.descricao': {"$regex":description, "$options": "i"}})

    else:
        result = read_many({'geral._id': {"$regex":cod, "$options": "i"}, 'geral.titulo': {"$regex":title, "$options": "i"}})
        
    if result.count() == 0:
        result = None

    return render_template('index.html', resultados=result)

#renderiza a página de detalhes, que mostra todos os dados de um registro
@app.route('/details')
def details():
    key = request.values.get('_id')
    result = read_many({'_id':ObjectId(key)})
    return render_template('details.html', resultados=result)

#encaminha para a página de inserção de dados
@app.route('/create')
def create():
    return render_template('create.html')

#pega os dados passados, insere no banco e redireciona para a página inicial
@app.route('/creating', methods=['POST'])
def creating():
    _id=request.values.get('_id')
    titulo=request.values.get('titulo')
    keywords=request.values.get('keywords')
    descricao=request.values.get('descricao')
    versao=request.values.get('versao')
    status=request.values.get('status')
    entidade=request.values.get('entidade')
    data=request.values.get('data')
    papel=request.values.get('papel')
    catalogo=request.values.get('catalogo')
    entrada=request.values.get('entrada')
    entidade1=request.values.get('entidade1')
    data1=request.values.get('data1')
    papel1=request.values.get('papel1')
    esquema_de_metadados=request.values.get('esquema_de_metadados')
    idioma=request.values.get('idioma')
    formato=request.values.get('formato')
    tamanho=request.values.get('tamanho')
    localizacao=request.values.get('localizacao')
    requisitos=request.values.get('requisitos')
    observacoes_de_Instalacoes=request.values.get('observacoes_de_Instalacoes')
    outros_requisitos_de_sistema=request.values.get('outros_requisitos_de_sistema')
    duracao=request.values.get('duracao')
    tipo_de_interatividade=request.values.get('tipo_de_interatividade')
    tipo_de_recurso_de_aprendizado=request.values.get('tipo_de_recurso_de_aprendizado')
    nivel_de_interatividade=request.values.get('nivel_de_interatividade')
    densidade_semantica=request.values.get('densidade_semantica')
    usuario_final=request.values.get('usuario_final')
    contexto_de_aprendizagem=request.values.get('contexto_de_aprendizagem')
    idade_recomendada=request.values.get('idade_recomendada')
    grau_de_dificuldade=request.values.get('grau_de_dificuldade')
    tempo_de_aprendizado=request.values.get('tempo_de_aprendizado')
    descricao1=request.values.get('descricao1')
    linguagem=request.values.get('linguagem')
    custo=request.values.get('custo')
    direitos_autorais=request.values.get('direitos_autorais')
    descricao2=request.values.get('descricao2')
    genero=request.values.get('genero')
    referencias=request.values.get('referencias')
    links_externos=request.values.get('links_externos')
    finalidade=request.values.get('finalidade')
    diretorio=request.values.get('diretorio')
    descricao3=request.values.get('descricao3')
    keywords1=request.values.get('keywords1')
    data2=request.values.get('data2')
    entidade2=request.values.get('entidade2')
    imagens=request.values.get('imagens')
    comentarios=request.values.get('comentarios')

    param = {
            "geral":{
                "_id":_id,
                "titulo":titulo,
                "keywords":'['+keywords+']',
                "descricao":descricao
            },
            "ciclo_de_vida":{
                "versao": versao,
                "status": status,
                "contribuinte": {
                    "entidade": entidade,
                    "data": data,
                    "papel": papel
                }
            },
            "meta_metadados":{
                "identificador": {
                    "catalogo": catalogo,
                    "entrada": entrada
                },
                "contribuinte": {
                    "entidade": entidade1,
                    "data": data1,
                    "papel": papel1,
                },
                "esquema_de_metadados": esquema_de_metadados,
                "idioma": idioma
            },
            "metadados_tecnicos" :{
                "formato": formato,
                "tamanho": tamanho,
                "localizacao": localizacao,
                "requisitos": requisitos,
                "observacoes_de_Instalacoes": observacoes_de_Instalacoes,
                "outros_requisitos_de_sistema": outros_requisitos_de_sistema,
                "duracao": duracao
            },
            "aspectos_educacionais": {
                "tipo_de_interatividade": tipo_de_interatividade,
                "tipo_de_recurso_de_aprendizado": tipo_de_recurso_de_aprendizado,
                "nivel_de_interatividade": nivel_de_interatividade,
                "densidade_semantica": densidade_semantica,
                "usuario_final": usuario_final,
                "contexto_de_aprendizagem": contexto_de_aprendizagem,
                "idade_recomendada": idade_recomendada,
                "grau_de_dificuldade": grau_de_dificuldade,
                "tempo_de_aprendizado": tempo_de_aprendizado,
                "descricao": descricao1,
                "linguagem": linguagem
            },
            "direitos" : {
                "custo": custo,
                "direitos_autorais": direitos_autorais,
                "descricao": descricao2
            },
            "relacoes" : {
                "genero": genero,
                "recurso": {
                    "referencias": referencias,
                    "links_externos": links_externos,
                }
            },
            "classificacao" : {
                "finalidade": finalidade,
                "diretorio": diretorio,
                "descricao": descricao3,
                "keywords": '['+keywords1+']',
            },
            "conteudo" : {
                "data": data2,
                "entidade": entidade2,
                "imagens": imagens,
                "comentarios": comentarios
            }
            }

    create_one(param)
    return redirect('/')

#pega os dados de um vídeo do youtube, insere-os no banco e redireciona para a página inicial
@app.route('/video_api')
def api():
    param = request.values.get('idVideo')
    get_api(param)
    return redirect('/')

#pega o id do registro clicado e renderiza a página update passando os dados do registro
@app.route('/update')
def update():
    key = request.values.get('_id')
    result = read_many({'_id':ObjectId(key)})
    return render_template('update.html', resultados=result)

#pega os dados passados, atualiza o registro no banco e redireciona para a página inicial
@app.route('/updating', methods=['POST'])
def updating():
    key=request.values.get('cod')
    _id=request.values.get('_id')
    titulo=request.values.get('titulo')
    keywords=request.values.get('keywords')
    descricao=request.values.get('descricao')
    versao=request.values.get('versao')
    status=request.values.get('status')
    entidade=request.values.get('entidade')
    data=request.values.get('data')
    papel=request.values.get('papel')
    catalogo=request.values.get('catalogo')
    entrada=request.values.get('entrada')
    entidade1=request.values.get('entidade1')
    data1=request.values.get('data1')
    papel1=request.values.get('papel1')
    esquema_de_metadados=request.values.get('esquema_de_metadados')
    idioma=request.values.get('idioma')
    formato=request.values.get('formato')
    tamanho=request.values.get('tamanho')
    localizacao=request.values.get('localizacao')
    requisitos=request.values.get('requisitos')
    observacoes_de_Instalacoes=request.values.get('observacoes_de_Instalacoes')
    outros_requisitos_de_sistema=request.values.get('outros_requisitos_de_sistema')
    duracao=request.values.get('duracao')
    tipo_de_interatividade=request.values.get('tipo_de_interatividade')
    tipo_de_recurso_de_aprendizado=request.values.get('tipo_de_recurso_de_aprendizado')
    nivel_de_interatividade=request.values.get('nivel_de_interatividade')
    densidade_semantica=request.values.get('densidade_semantica')
    usuario_final=request.values.get('usuario_final')
    contexto_de_aprendizagem=request.values.get('contexto_de_aprendizagem')
    idade_recomendada=request.values.get('idade_recomendada')
    grau_de_dificuldade=request.values.get('grau_de_dificuldade')
    tempo_de_aprendizado=request.values.get('tempo_de_aprendizado')
    descricao1=request.values.get('descricao1')
    linguagem=request.values.get('linguagem')
    custo=request.values.get('custo')
    direitos_autorais=request.values.get('direitos_autorais')
    descricao2=request.values.get('descricao2')
    genero=request.values.get('genero')
    referencias=request.values.get('referencias')
    links_externos=request.values.get('links_externos')
    finalidade=request.values.get('finalidade')
    diretorio=request.values.get('diretorio')
    descricao3=request.values.get('descricao3')
    keywords1=request.values.get('keywords1')
    data2=request.values.get('data2')
    entidade2=request.values.get('entidade2')
    imagens=request.values.get('imagens')
    comentarios=request.values.get('comentarios')

    update_one({"_id":ObjectId(key)}, { "geral._id":_id,"geral.titulo":titulo,"geral.keywords":keywords,
                "geral.descricao":descricao,"ciclo_de_vida.versao": versao,"ciclo_de_vida.status": status,
                "ciclo_de_vida.contribuinte.entidade": entidade,"ciclo_de_vida.contribuinte.data": data,
                "ciclo_de_vida.contribuinte.papel": papel,"meta_metadados.identificador.catalogo": catalogo,
                "meta_metadados.identificador.entrada": entrada,"meta_metadados.contribuinte.entidade": entidade1,
                "meta_metadados.contribuinte.data": data1,"meta_metadados.contribuinte.papel": papel1,
                "meta_metadados.esquema_de_metadados": esquema_de_metadados,"meta_metadados.idioma": idioma,
                "metadados_tecnicos.formato": formato,"metadados_tecnicos.tamanho": tamanho,
                "metadados_tecnicos.localizacao": localizacao,"metadados_tecnicos.requisitos": requisitos,
                "metadados_tecnicos.observacoes_de_Instalacoes": observacoes_de_Instalacoes,"metadados_tecnicos.outros_requisitos_de_sistema": outros_requisitos_de_sistema,
                "metadados_tecnicos.duracao": duracao,"aspectos_educacionais.tipo_de_interatividade": tipo_de_interatividade,
                "aspectos_educacionais.tipo_de_recurso_de_aprendizado": tipo_de_recurso_de_aprendizado,
                "aspectos_educacionais.nivel_de_interatividade": nivel_de_interatividade,
                "aspectos_educacionais.densidade_semantica": densidade_semantica,
                "aspectos_educacionais.usuario_final": usuario_final,"aspectos_educacionais.contexto_de_aprendizagem": contexto_de_aprendizagem,
                "aspectos_educacionais.idade_recomendada": idade_recomendada,"aspectos_educacionais.grau_de_dificuldade": grau_de_dificuldade,
                "aspectos_educacionais.tempo_de_aprendizado": tempo_de_aprendizado,"aspectos_educacionais.descricao": descricao1,
                "aspectos_educacionais.linguagem": linguagem,"direitos.custo": custo,"direitos.direitos_autorais": direitos_autorais,
                "direitos.descricao": descricao2,"relacoes.genero": genero,"relacoes.recurso.referencias": referencias,
                "relacoes.recurso.links_externos": links_externos,"classificacao.finalidade": finalidade,
                "classificacao.diretorio": diretorio,"classificacao.descricao": descricao3,"classificacao.keywords": keywords1,
                "conteudo.data": data2,"conteudo.entidade": entidade2,"conteudo.imagens": imagens,
                "conteudo.comentarios": comentarios})
    return redirect('/')

#deleta o registro clicado
@app.route('/delete')
def delete():
    key = request.values.get('_id')
    result = delete_one({'_id':ObjectId(key)})
    return redirect('/')

#----------api--------------

#retorna todos os registros
@app.route('/api/', methods=['GET'])
def listAll():
    result = list(read_all())
    for r in result:
        r['geral']['descricao'] = r['geral']['descricao'].replace('\n', ' ')
        r['classificacao']['descricao'] = r['classificacao']['descricao'].replace('\n', ' ')
    return Response(json.dumps(result, indent=4, default=json_util.default, ensure_ascii=False), content_type = "application/json; charset=utf-8")

#pega os dados de um vídeo do youtube e insere-os no banco
@app.route('/api/post/<idVideo>', methods=['GET', 'POST'])
def insert(idVideo):
    objId = get_api(idVideo)
    result = list(read_many({'_id': ObjectId(objId)}))
    if not result:
        result = {"Status" : "Nenhum registro encontrado!"}
    else:
        for r in result:
            r['geral']['descricao'] = r['geral']['descricao'].replace('\n', ' ')
            r['classificacao']['descricao'] = r['classificacao']['descricao'].replace('\n', ' ')
    return Response(json.dumps(result, indent=4, default=json_util.default, ensure_ascii=False), content_type = "application/json; charset=utf-8")

#retorna todos os registros que cumprem o parametro
@app.route('/api/<field>=<filter>', methods=['GET'])
def listObject(field, filter):
    if field == '_id':
        filter = ObjectId(filter)

    if field == '_id.$oid':
        field = '_id'
        filter = ObjectId(filter)

    if field == 'geral.titulo' or field == 'geral.keywords':
        filter = {"$regex":filter, "$options": "i"}

    result = list(read_many({field:filter}))
    if not result:
        result = {"Status": "Nenhum registro encontrado!"}
    else:
        for r in result:
            r['geral']['descricao'] = r['geral']['descricao'].replace('\n', ' ')
            r['classificacao']['descricao'] = r['classificacao']['descricao'].replace('\n', ' ')
    return Response(json.dumps(result, indent=4, default=json_util.default, ensure_ascii=False), content_type = "application/json; charset=utf-8")

#atualiza o registro escolhido
@app.route('/api/<field>=<filter>/<attribute>=<new>', methods=['GET', 'PUT'])
def put(field, filter, attribute, new):
    if field == '_id':
        filter = ObjectId(filter)

    if field == '_id.$oid':
        field = '_id'
        filter = ObjectId(filter)

    if field == 'geral.titulo' or field == 'geral.keywords':
        filter = {"$regex":filter, "$options": "i"}
    result = list(read_many({field:filter}))
    if not result:
        result = {"Status":"Nenhum registro encontrado!"}
    else:
        update_one({field:filter}, {attribute:new})
        result = list(read_many({field:filter}))
        for r in result:
            r['geral']['descricao'] = r['geral']['descricao'].replace('\n', ' ')
            r['classificacao']['descricao'] = r['classificacao']['descricao'].replace('\n', ' ')
    return Response(json.dumps(result, indent=4, default=json_util.default, ensure_ascii=False), content_type = "application/json; charset=utf-8")

#deleta o registro passado
@app.route('/api/delete/<field>=<filter>', methods=['GET', 'DELETE'])
def deleting(field, filter):
    if field == '_id':
        filter = ObjectId(filter)

    if field == '_id.$oid':
        field = '_id'
        filter = ObjectId(filter)
    result = read_many({field:filter})
    if result.count() == 0:
        result = {"Status" : "Nenhum registro encontrado!"}
    else:
        delete_one({field:filter})
        result = {"Status" : "Registro deletado com sucesso!"}

    return Response(json.dumps(result, indent=4, default=json_util.default, ensure_ascii=False), content_type = "application/json; charset=utf-8")
