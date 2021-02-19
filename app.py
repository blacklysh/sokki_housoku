from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search.html')
def search():
    return render_template('search.html')


@app.route('/', methods=['GET'])
def get():
	return render_template('search.html', \
		title = '速記法則', \
		message = '名前を入力して下さい。')

@app.route("/", methods=['POST'])
def index():
    housoku = request.form['housoku']
    return render_template('search.html', housoku=housoku)
