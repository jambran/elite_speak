from flask import Flask, render_template
import os
import main_script
import defs
import textToSpeech

app = Flask(__name__)


@app.route('/record', methods=['POST'])
def main():
    definitions = main_script.main()
    return render_template('list.html', definitions=definitions)


@app.route('/')
def hello_word():
    return render_template('index.html')


