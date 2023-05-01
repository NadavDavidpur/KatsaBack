from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, after_this_request
from flask_cors import CORS, cross_origin
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json
import mysql.connector
import create_db

# from create_db import *

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="NadavD3203",
    database="Katsa",
    auth_plugin='mysql_native_password'
)

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'secret key'
db = SQLAlchemy(app)
Session(app)





# jsonify(create_db.projects_query(mydb))
@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    response = request.json

    # response.headers.add('Access-Control-Allow-Origin', '*')mydb,

    users_login = create_db.users_login(response['username'], response['id'])

    if len(users_login) == 1:

        user_in = 'True'
        return {'userIn': user_in, 'avatar': users_login[0]['avatar'], "isManager": users_login[0]['isManager'],
                "isActive": users_login[0]['isActive']}
    else:
        user_in = 'False'
        return {'userIn': user_in}


@app.route('/deleteRisk', methods=['POST'])
@cross_origin()
def deleteRisk():
    response = request.json
    create_db.delete_project_risk(response['id'])
    # response.headers.add('Access-Control-Allow-Origin', '*')mydb,
    return "uu"


@app.route('/newRiskProject', methods=['POST'])
@cross_origin()
def newRiskProject():
    response = request.json
    create_db.insert_riskProject(response['projectId'], response['RiskName'])
    response = jsonify(create_db.project_risk_query()[-1])
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(1)

    return response


# mydb,
@app.route('/newRisk', methods=['POST'])
@cross_origin()
def newRisk():
    response = request.json
    create_db.newRisk(response['RiskName'])
    return '1'


@app.route('/delete', methods=['GET'])
def delete():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if request.method == 'GET':
        # print('post app')
        # req = request.json
        # print(req)
        # # mission = request.json['projectname']
        # mission = request.json['deleting']
        # print(mission)
        return jsonify(name="nas")


@app.route('/workers', methods=['GET'])
# @cross_origin()mydb
def workers():
    response = jsonify(create_db.workers_query())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/workers', methods=['GET'])
# def workers():
#     if request.method == 'GET':
#         # print('post app')
#         # req = request.json
#         # print(req)
#         # # mission = request.json['projectname']
#         # mission = request.json['deleting']
#         # print(mission)mydb
#         print((create_db.workers_query()))
#         return jsonify((create_db.workers_query()))


# @app.route('/userId', methods=['GET'])
# def UserId():
#     if request.method == 'GET':
#         # print(session.get('id'))
#         return jsonify({'id': session.get('id'), 'user': session.get('user')})


# @app.route('/logout', methods=['GET'])
# def logout():
#     if request.method == 'GET':
#         # print('post app')
#         # req = request.json
#         session.pop('user', None)
#         session.pop('id', None)
#         # print(req)
#         # # mission = request.json['projectname']
#         # mission = request.json['deleting']
#         # print(mission)mydb
#         return 'logout'


@app.route('/projects', methods=['GET'])
# @cross_origin()mydb
def projects():
    response = jsonify(create_db.projects_query())
    # print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/newProject', methods=['POST'])
@cross_origin()
def newProject():
    # @after_this_request
    # def add_header(response):
    #     response.headers['Access-Control-Allow-Origin'] = '*'
    #     return response

    # if request.method == 'POST':
    req = request.json
    # print(req['projectname'] + " " + req['contractorname'] + " " + req['inspectorname'] + " " + req[
    # 'location_project'])mydb,
    create_db.insert_newProject(req['projectname'], req['contractorname'], req['inspectorname'],
                                req['location_project'], req['description'], req['Tool'])
    # req.headers.add('Access-Control-Allow-Origin', '*')
    return req




@app.route('/risks', methods=['GET'])
# @cross_origin()mydb
def risks():
    response = jsonify(create_db.risks_query())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/ProjectRisk', methods=['GET'])
# @cross_origin()mydb
def project_risk():
    response = jsonify(create_db.project_risk_query())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/video')
def video():
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # app.headers.add('Access-Control-Allow-Origin', '*')
    # return jsonify({'text': 'ffff'}), 200


@app.route('/comments', methods=['GET'])
# @cross_origin()mydb
def comment():
    response = jsonify(create_db.comment())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/newComment', methods=['POST'])
@cross_origin()
def newComment():
    response = request.json
    # projectRiskId, description, workerName
    # print(response['workerName'])
    create_db.insert_comment(response['ProjectRiskId'], response['description'], response['workerName'])
    response = jsonify(create_db.project_risk_query()[-1])
    response.headers.add('Access-Control-Allow-Origin', '*')
    # print(1)

    return response


@app.route('/updateCommon', methods=['POST'])
@cross_origin()
def updateCommon():
    response = request.json
    print(response)
    # projectRiskId, description, workerName
    # print(response['workerName'])
    create_db.update_comment(response['body'], response['id'])
    # response = jsonify(create_db.project_risk_query()[-1])
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # print(1)

    return "update"


@app.route('/DeleteCommon', methods=['POST'])
@cross_origin()
def DeleteCommon():
    response = request.json
    print(response)
    # projectRiskId, description, workerName
    # print(response['workerName'])
    create_db.Delete_comment(response['id'])

    # print(1)

    return "delete"


@app.route('/DeleteWorker', methods=['POST'])
@cross_origin()
def DeleteWorker():
    response = request.json
    # print(response)
    # projectRiskId, description, workerName
    # print(response['workerName'])
    create_db.Delete_worker(response['id'])
    response = create_db.workers_query()
    # print(1)
    # print(response)
    return jsonify(response)


@app.route('/newWorker', methods=['POST'])
@cross_origin()
def new_worker():
    response = request.json
    # print(response)
    create_db.insert_worker(response['name'], response['Id'], response['PhoneNumber'], response['class'],
                            response['img'], response['manager'])
    return "successes"


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
