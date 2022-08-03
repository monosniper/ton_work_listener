from flask import Flask, request, abort, Response
from flask_sslify import SSLify

BOT_TOKEN = '5581884599:AAFgpkbtGEbtfCSvj0w1L2DDL75TjSDIRnw'

app = Flask(__name__)
ssslify = SSLify(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % path, mimetype="text/html")


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
