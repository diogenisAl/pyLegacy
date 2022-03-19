from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def yolo():

    # the initial dictionary with members' attributes
    legacy_dictionary = {"20eeee": {"youtube_url": "https://di.ionio.gr", "source_code_url": "https://di.ionio.gr"} };

    return jsonify(legacy_dictionary)


if __name__ == '__main__':
    app.run()
