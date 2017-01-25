# define simple flask app
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pregunta', methods=['POST'])
def pregunta():
    valor = request.form['response_a']
    return render_template('index.html', answer=valor)



if __name__ == "__main__":
    app.run()
