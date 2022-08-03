from flask import Flask, request, abort
from flask_sslify import SSLify

BOT_TOKEN = '5581884599:AAFgpkbtGEbtfCSvj0w1L2DDL75TjSDIRnw'

app = Flask(__name__)
ssslify = SSLify(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()