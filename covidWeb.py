#final project
#flask webpage

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello from Flask!'
    return render_template('home.html')

if(__name__) == '__main__':
    app.run(debug=True, port=5001)

