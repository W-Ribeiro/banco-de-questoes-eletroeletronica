from flask import Flask, render_template, request
from db import db_connection

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questoes')
def questoes():
    dificuldade = request.args.get('dificuldade')
    modulo = request.args.get('modulo')

    cursor = db_connection.cursor()
    
    sql = f"SELECT * FROM questoesdb WHERE dificuldade = '{dificuldade}' and modulo = '{modulo}'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    return render_template('questoes.html', rows=rows)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)