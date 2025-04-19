from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Levi Lina is een kanker homo en woont in lathum"

@app.route('/test')
def test():
    return "will it triggers"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
 