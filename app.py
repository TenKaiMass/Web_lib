import json
from flask import Flask, render_template, request
import random
app = Flask(__name__)

title_site = 'Issy la Bibli'


# @app.route('/')
# def home():
#     return render_template('home.html', title=title_site)


@app.route('/', methods=["POST", "GET"])
def getBooks():
    with open("./books.json", "r") as read_file:
        data = json.load(read_file)
    # aleaBook = random.randint(0, len(data))
    # data = json.dumps(data[aleaBook])
    if request.method == "POST":
        livre = request.form["idortitle"]
        for i in range(0, len(data)):
            if data[i]['isbn'] == livre or data[i]['title'] == livre:
                return render_template('item.html', title=title_site, data=data[i], name=data[i]['title'])
            else:
                return render_template('erreur.html', title=title_site)

                # return jsonify(data)
    else:
        return render_template('home.html', title=title_site)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
