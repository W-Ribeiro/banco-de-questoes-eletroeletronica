from flask import Flask, render_template
import mysql.connector

db_connection = mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='univesp',
                                        database='bdquestoes')

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Eletricidade')
def elet():
    cursor = db_connection.cursor()

    sql = ('SELECT enunciado, gabarito FROM questoes')
    cursor.execute(sql)

    for enunciado, gabarito in cursor:
        print('Enunciado: {} \nGabarito: {}\n'.format(enunciado, gabarito))
    return(enunciado, gabarito)