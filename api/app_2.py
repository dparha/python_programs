from flask import Flask, request, jsonify
app = Flask(__name__)  # Flask constructor

# A decorator used to tell the app
# which URL is associated function


@app.route('/')
def hello():
    return 'HELLO'


@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def hello_name(name):
    if request.method == 'GET':
        return 'Hello %s!\n' % name

    elif request.method == 'POST':
        return jsonify({'name from post': request.form['name'],
                        'name from url': name})
    else:
        return request.statuscode(404)


if __name__ == '__main__':
    app.run(debug=True)
