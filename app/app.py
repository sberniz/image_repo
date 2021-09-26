from flask import Flask, render_template, escape, request,jsonify
from flask_cors import CORS
from .dbsearch import search
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    CORS(app)
    @app.route('/')
    def root():
        return render_template('index.html')

    @app.route('/airplane_search',methods=['POST'])
    def airplane_search():
        airplane_info = request.values['make_model'].split(" ",1)
        if len(airplane_info) == 2:
            airplane_make = airplane_info[0]
            airplane_model = airplane_info[1]
            QUERY = """SELECT * FROM airplane_info WHERE manufacturer LIKE '{}%' AND model LIKE '{}%';
                    """.format(airplane_make, airplane_model)
        else:
            QUERY = """SELECT * FROM airplane_info WHERE manufacturer LIKE '%{}%' OR model LIKE '%{}%';
                    """.format(airplane_info[0], airplane_info[0])
        data = search(QUERY)
        json_names = []
        for item in data:
            json_dict = {
                'id':item[0],
                'img_id':item[1],
                'Manufacturer':item[2],
                'model':item[3]
            }
            json_names.append(json_dict)
        return jsonify(json_names)


    return app