from flask import Flask, render_template
import requests

app = Flask(__name__)
JOKE_API_URL = 'https://backend-omega-seven.vercel.app/api/getjoke'


@app.route('/ready', methods=['GET'])
def ready():
    return 'Application is ready'


@app.route('/healthy', methods=['GET'])
def healthy():
    return 'Application is healthy'


@app.route('/', methods=['GET'])
def index():
    try:
        joke = requests.get(JOKE_API_URL).json()[0]
        question, punchline = joke.values()
        return render_template('index.html', question=question, punchline=punchline)
    except Exception as e:
        return f'Error: {str(e)}', 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
