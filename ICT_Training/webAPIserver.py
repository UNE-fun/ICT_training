from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    title = "Hello World"
    msg = "このページが見えてたら名前でも入れてね"
    return render_template('index.html', message=msg, title=title)

@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        title ="Hello"
        if request.method == 'GET':
            return request.args.get('test')

        elif request.method == 'POST':
            name = request.form['name']
            return render_template('index.html', name=name, title=title)

        else:
            return redirect(url_for('index'))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
