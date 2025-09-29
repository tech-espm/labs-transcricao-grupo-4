from flask import Flask, render_template
import config

app = Flask(__name__)

#rotas flask


@app.get('/')
def index():
    return render_template('index/Landing.html', titulo='Landing Page')

@app.get('/transcription')
def index():
    return render_template('index/Transcription.html', titulo='Transcription Page')






if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
