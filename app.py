from flask import Flask, render_template, request
import mysql.connector

app = Flask('__name__')

def connect_to_db():
    db_connection = mysql.connector.connect(host='us-cdbr-east-04.cleardb.com',
                                            user='b3f5faf814bd93',
                                            password='1f0b1ae4',
                                            database='heroku_54813b828b4da3c')
    return db_connection    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questoes')
def questoes():
    dificuldade = request.args.get('dificuldade')
    modulo = request.args.get('modulo')

    cnx = connect_to_db();
    cursor = cnx.cursor()
    
    sql = f"SELECT * FROM questoesdb WHERE dificuldade = '{dificuldade}' and modulo = '{modulo}'"
    cursor.execute(sql)
    row = cursor.fetchone()
    questoes = []

    while row:
        enunciado = row[3]
        gabarito = row[4]

        print(enunciado)

        questoes.append((enunciado, gabarito))
        row = cursor.fetchone()

    return render_template('questoes.html', questoes=questoes, dificuldade=dificuldade, modulo=modulo )

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)