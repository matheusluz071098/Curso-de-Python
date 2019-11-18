# aula web
# web


from flask import Flask


app = Flask(__name__)

@app.route('/')

def inicio():
    return 'bem vindos ao mundo real'

app.run()
