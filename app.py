from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return " wil toch wat anders proberen"

@app.route('/test')
def test():
    return "will it triggers"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
 