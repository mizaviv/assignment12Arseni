import os
from flask import Flask, request, jsonify
from dbActions import json_query
import requests
import json
import mysql.connector

app = Flask(__name__)


@app.route('/assignment12/restapi_users', defaults={'user_id': 1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def assignment12_user(user_id):
    query = "select * from users where user_id = %s"
    query_result = json_query(query=query, query_params= (user_id, ))
    if query_result == {}:
        return jsonify({"error": "no data found"})
    else:
        return jsonify(query_result)

if __name__ == '__main__':
    #   Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.secret_key = '123'
    app.run(host='127.0.0.1', port=port)

