from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def func():
    name = request.args.get('name')
    message = request.args.get('message')
    if name == None or message == None:
        return 'Добавьте в адресную строку « /?name=Rekruto&message=Давай дружить! » для финального результата'
    return f"Hello {name}! {message}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)