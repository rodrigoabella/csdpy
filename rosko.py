# define simple flask app
from flask import Flask,render_template,request
from model.rosko_model import RoskoModel
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pregunta', methods=['POST'])
def pregunta():
    valor = request.form['response_a']
    rosko = RoskoModel()
    rosko.setRespuesta(valor);
    return render_template('index.html', answer=valor, result=rosko.validar())

@app.route('/pass', methods=['GET'])
def getPass():
    return render_template('index.html', result='PASS')



if __name__ == "__main__":
    app.run()
