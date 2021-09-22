from flask import Flask, render_template, escape, request
from .dbsearch import search
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
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
        print(data)
        return render_template('display.html',data=data)


    return app