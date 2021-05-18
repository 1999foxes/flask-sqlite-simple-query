import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<string:database>/<string:query>")
def index(database, query):
    try:
        con = sqlite3.connect(database)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(query)
        result = list(map(lambda row: dict(row), cur.fetchall()))
        # con.commit()
        con.close()
        return jsonify(result)
    except Exception as e:
        return str(e)
