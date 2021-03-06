from flask import Flask, render_template
import main_script
import threading

app = Flask(__name__)


@app.route('/record', methods=['POST'])
def main():
    # definitions = []
    # thread = threading.Thread(target=main_script.main, args=[])
    # thread.start()
    definitions = main_script.main()
    return render_template('recording.html', definitions=definitions)


@app.route('/')
def hello_word():
    return render_template('index.html')


