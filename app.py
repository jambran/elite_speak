from flask import Flask
import main_script

app = Flask(__name__)


@app.route('/')
def hello_word():
    main_script.main()