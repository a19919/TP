import pymysql
from TP.app import app
from TP.config import mysql
from flask import jsonify
from flask import request
from flask import render_template

@app.route('/')
def index():
    return "TP de Complementos de Programacao"
        
@app.route('/')
@app.route('/alerta')
def alerta_web():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM alerta")
        result = cursor.fetchall()
        things = result
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return render_template('alerta.html', title='TP Comp Prog', things = things)    
        
@app.route('/')        
@app.route('/elemento')
def elemento_web():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM elemento")
    result = cursor.fetchall()
    things = result
    cursor.close()
    conn.close()
    return render_template('elemento.html', title='TP Comp Prog', things = things)
    
@app.route('/')
@app.route('/estacao')
def estacao_web():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT id, nome, latitude, longitude, elevacao, Local_id FROM estacao")
    result = cursor.fetchall()
    things = result
    cursor.close()
    conn.close()
    return render_template('estacao.html', title='TP Comp Prog', things = things)
    
@app.route('/')
@app.route('/local')
def local_web():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT id, nome FROM local")
    result = cursor.fetchall()
    things = result
    cursor.close()
    conn.close()
    return render_template('local.html', title='TP Comp Prog', things=things)
    
@app.route('/')
@app.route('/observacao')
def obs_web():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT id, data, valor, Estacao_id, Alerta_id, Elemento_id FROM observacao")
    result = cursor.fetchall()
    things = result
    cursor.close()
    conn.close()
    return render_template('observacao.html', title='TP Comp Prog', things = things)

@app.route('/observacao/c', methods=['POST']) #CREATE Observacao
def add_observacao():
	conn = mysql.connect()
	cursor = conn.cursor()
	try:
		_json = request.json
		_id = _json['id']
		_data = _json['data']
		_valor = _json['valor']
		_Estacao_id = _json['Estacao_id']
		_Alerta_id = _json['Alerta_id']
		_Elemento_id = _json['Elemento_id']
		if _id and _data and _valor and _Estacao_id and _Alerta_id and _Elemento_id and request.method == 'POST':
			sqlQuery = "INSERT INTO observacao(id, data, valor, Estacao_id, Alerta_id, Elemento_id) VALUES(%s, %s, %s, %s, %s, %s)"
			data = (_id, _data, _valor, _Estacao_id, _Alerta_id, _Elemento_id)
			cursor.execute(sqlQuery, data)
			conn.commit()
			resposta = jsonify('Observacao Adicionada com sucesso!')
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		return 'Sucesso'

@app.route('/alerta/c', methods=['POST']) #CREATE Alerta
def add_alerta():
	conn = mysql.connect()
	cursor = conn.cursor()
	try:
		_json = request.json
		_id = _json['id']
		_tipo = _json['tipo']
		_descricao = _json['descricao']
		if _id and _tipo and _descricao and request.method == 'POST':
			sqlQuery = "INSERT INTO alerta(id, tipo, descricao) VALUES(%s, %s, %s)"
			data = (_id, _tipo, _descricao)
			cursor.execute(sqlQuery, data)
			conn.commit()
			resposta = jsonify('Alerta Adicionado com sucesso!')
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		return 'Sucesso'

@app.route('/elemento/c', methods=['POST']) #CREATE Elemento
def add_elemento():
	conn = mysql.connect()
	cursor = conn.cursor()
	try:
		_json = request.json
		_id = _json['id']
		_tipo = _json['tipo']
		if _id and _tipo and request.method == 'POST':
			sqlQuery = "INSERT INTO elemento(id, tipo) VALUES(%s, %s)"
			data = (_id, _tipo)
			cursor.execute(sqlQuery, data)
			conn.commit()
			resposta = jsonify('Elemento adicionado com sucesso!')
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		return 'Sucesso'

@app.route('/estacao/c', methods=['POST']) #CREATE Estacao
def add_estacao():
	conn = mysql.connect()
	cursor = conn.cursor()
	try:
		_json = request.json
		_id = _json['id']
		_nome = _json['nome']
		_latitude = _json['latitude']
		_longitude = _json['longitude']
		_elevacao = _json['elevacao']
		_Local_id = _json['Local_id']
		if _id and _nome and _latitude and _longitude  and _elevacao and _Local_id and request.method == 'POST':
			sqlQuery = "INSERT INTO estacao(id, nome, latitude, longitude, elevacao, Local_id) VALUES(%s, %s, %s, %s, %s, %s)"
			data = (_id, _nome, _latitude, _longitude, _elevacao, _Local_id)
			cursor.execute(sqlQuery, data)
			conn.commit()
			resposta = jsonify('Estacao adicionada com sucesso!')
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		return 'Sucesso'

@app.route('/local/c', methods=['POST']) #CREATE Local
def add_local():
	conn = mysql.connect()
	cursor = conn.cursor()
	try:
		_json = request.json
		_id = _json['id']
		_nome = _json['nome']
		if _id and _nome and request.method == 'POST':
			sqlQuery = "INSERT INTO local(id, nome) VALUES(%s, %s)"
			data = (_id, _nome)
			cursor.execute(sqlQuery, data)
			conn.commit()
			resposta = jsonify('Local adicionado com sucesso!')
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		return 'Sucesso'
		
@app.route('/alerta/r') #READ Alerta
def alerta():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		cursor.execute("SELECT id, tipo, descricao FROM alerta")
		result = cursor.fetchall()
		resposta = jsonify(result)
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/estacao/r') #READ Estacao
def estacao():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		cursor.execute("SELECT id, nome, latitude, longitude, elevacao, Local_id FROM estacao")
		result = cursor.fetchall()
		resposta = jsonify(result)
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/elemento/r') #READ Elemento
def elemento():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		cursor.execute("SELECT id, tipo FROM elemento")
		result = cursor.fetchall()
		resposta = jsonify(result)
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/local/r') #READ Local
def local():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		cursor.execute("SELECT id, nome FROM local")
		result = cursor.fetchall()
		resposta = jsonify(result)
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/observacao/r') #READ Observacao
def observacao():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		cursor.execute("SELECT id, data, valor, Estacao_id, Alerta_id, Elemento_id FROM observacao")
		result = cursor.fetchall()
		resposta = jsonify(result)
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/alerta/u', methods=['PUT']) #UPDATE Alerta
def up_alerta():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id = _json['id']
        _tipo = _json['tipo']
        _descricao = _json['descricao']
        if _id and _tipo and _descricao and request.method == 'PUT':			
            sqlQuery = "UPDATE alerta SET tipo=%s, descricao=%s WHERE id=%s"
            data = (_tipo, _descricao, _id,)
            cursor.execute(sqlQuery, data)
            conn.commit()
            resposta = jsonify('Update com sucesso!')
            resposta.status_code = 200
            return resposta
        else:
            return not_found()	
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/elemento/u', methods=['PUT']) #UPDATE Elemento
def up_elemento():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id = _json['id']
        _tipo = _json['tipo']
        if _id and _tipo and request.method == 'PUT':			
            sqlQuery = "UPDATE elemento SET tipo=%s WHERE id=%s"
            data = (_tipo, _id,)
            cursor.execute(sqlQuery, data)
            conn.commit()
            resposta = jsonify('Update com sucesso!')
            resposta.status_code = 200
            return resposta
        else:
            return not_found()	
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/estacao/u', methods=['PUT']) #UPDATE Estacao
def up_estacao():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id = _json['id']
        _nome = _json['nome']
        _latitude = _json['latitude']
        _longitude = _json['longitude']
        _elevacao = _json['elevacao']
        _Local_id = _json['Local_id']
        if _id and _nome and _latitude and _longitude and _elevacao and _Local_id and request.method == 'PUT':			
            sqlQuery = "UPDATE estacao SET nome=%s, latitude=%s, longitude=%s, elevacao=%s, Local_id=%s WHERE id=%s"
            data = (_nome, _latitude, _longitude, _elevacao, _Local_id, _id,)
            cursor.execute(sqlQuery, data)
            conn.commit()
            resposta = jsonify('Update com sucesso!')
            resposta.status_code = 200
            return resposta
        else:
            return not_found()	
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/local/u', methods=['PUT']) #UPDATE Local
def up_local():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id = _json['id']
        _nome = _json['nome']
        if _id and _nome and request.method == 'PUT':			
            sqlQuery = "UPDATE local SET nome=%s WHERE id=%s"
            data = (_nome, _id,)
            cursor.execute(sqlQuery, data)
            conn.commit()
            resposta = jsonify('Update com sucesso!')
            resposta.status_code = 200
            return resposta
        else:
            return not_found()	
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/observacao/u', methods=['PUT']) #UPDATE Observacao
def up_observacao():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id = _json['id']
        _data = _json['data']
        _valor = _json['valor']
        _Estacao_id = _json['Estacao_id']
        _Alerta_id = _json['Alerta_id']
        _Elemento_id = _json['Elemento_id']
        if _id and _data and _valor and _Estacao_id and _Alerta_id and _Elemento_id and request.method == 'PUT':			
            sqlQuery = "UPDATE observacao SET data=%s, valor=%s, Estacao_id=%s, Alerta_id=%s, Elemento_id=%s WHERE id=%s"
            data = (_data, _valor, _Estacao_id, _Alerta_id, _Elemento_id, _id,)
            cursor.execute(sqlQuery, data)
            conn.commit()
            resposta = jsonify('Update com sucesso!')
            resposta.status_code = 200
            return resposta
            return jsonify(result={"status": 200})
        else:
            return not_found()	
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/alerta/d', methods=['DELETE']) #DELETE Alerta
def del_alerta():
    conn = mysql.connect()
    cursor = conn.cursor()
    sqlQuery = "SET FOREIGN_KEY_CHECKS=0"
    cursor.execute(sqlQuery)
    conn.commit()
    try:
        _json = request.json
        _id = _json['id']
        if _id and request.method == 'DELETE':
                    
            sqlQuery = "DELETE FROM alerta WHERE id=%s"
            data = (_id)
            cursor.execute(sqlQuery,data)
            conn.commit()
            resposta = jsonify('Delete com sucesso!')
            resposta.status_code = 200
            return resposta
            return jsonify(result={"status": 200})
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/elemento/d', methods=['DELETE']) #DELETE Elemento
def del_elemento():
    conn = mysql.connect()
    cursor = conn.cursor()
    sqlQuery = "SET FOREIGN_KEY_CHECKS=0"
    cursor.execute(sqlQuery)
    conn.commit()
    try:
        _json = request.json
        _id = _json['id']
        if _id and request.method == 'DELETE':
            sqlQuery = "DELETE FROM elemento WHERE id=%s"
            data = (_id)
            cursor.execute(sqlQuery,data)
            conn.commit()
            resposta = jsonify('Delete com sucesso!')
            resposta.status_code = 200
            return resposta
            return jsonify(result={"status": 200})
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/estacao/d', methods=['DELETE']) #DELETE Estacao
def del_estacao():
    conn = mysql.connect()
    cursor = conn.cursor()
    sqlQuery = "SET FOREIGN_KEY_CHECKS=0"
    cursor.execute(sqlQuery)
    conn.commit()
    try:
        _json = request.json
        _id = _json['id']
        if _id and request.method == 'DELETE':
            sqlQuery = "DELETE FROM estacao WHERE id=%s"
            data = (_id)
            cursor.execute(sqlQuery,data)
            conn.commit()
            resposta = jsonify('Delete com sucesso!')
            resposta.status_code = 200
            return resposta
            return jsonify(result={"status": 200})
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/local/d', methods=['DELETE']) #DELETE Local
def del_local():
    conn = mysql.connect()
    cursor = conn.cursor()
    sqlQuery = "SET FOREIGN_KEY_CHECKS=0"
    cursor.execute(sqlQuery)
    conn.commit()
    try:
        _json = request.json
        _id = _json['id']
        if _id and request.method == 'DELETE':
            sqlQuery = "DELETE FROM local WHERE id=%s"
            data = (_id)
            cursor.execute(sqlQuery,data)
            conn.commit()
            resposta = jsonify('Delete com sucesso!')
            resposta.status_code = 200
            return resposta
            return jsonify(result={"status": 200})
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/observacao/d', methods=['DELETE']) #DELETE Observacao
def del_observacao():
    conn = mysql.connect()
    cursor = conn.cursor()
    sqlQuery = "SET FOREIGN_KEY_CHECKS=0"
    cursor.execute(sqlQuery)
    conn.commit()
    try:
        _json = request.json
        _id = _json['id']
        if _id and request.method == 'DELETE':
            sqlQuery = "DELETE FROM observacao WHERE id=%s"
            data = (_id)
            cursor.execute(sqlQuery,data)
            conn.commit()
            resposta = jsonify('Delete com sucesso!')
            resposta.status_code = 200
            return resposta
            return jsonify(result={"status": 200})
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Resultado nao encontrado: ' + request.url,
    }
    resposta = jsonify(message)
    resposta.status_code = 404
    return resposta