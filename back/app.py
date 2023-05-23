from flask import Flask
import numpy as np
# from flask_cors import CORS
import json

app = Flask(__name__)
# CORS(app)


@app.route('/')
def main():
    labels = ["January", "February", "March", "April", "May", "June"]
    l = {
        'labels': labels,
        'datasets': [
            {
                'label': "My First dataset",
                'backgroundColor': "rgb(255, 99, 132)",
                'borderColor': "rgb(255, 99, 132)",
                'data': [50, 5, 2, 7, 30, 20, 45],
            },
        ],
    }
    res = json.dumps(l)
    return res


if __name__ == '__main__':
    app.run()
