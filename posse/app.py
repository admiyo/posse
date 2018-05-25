from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from flask import json
from flask import request
from pymysql.cursors import DictCursor

from flask_restplus import Api
from flask_restplus import Resource


app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'keystone'
app.config['MYSQL_DATABASE_PASSWORD'] = 'keystone'
app.config['MYSQL_DATABASE_DB'] = 'keystone'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

api = Api(app, version='1.0', title='Posse',
    description='RBAC Policy Management',
)

@app.route('/ui')
def showSignUp():
    return render_template('index.html')

@api.route("/services")
@api.doc()
class Services(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM service")
        data = cursor.fetchall() 
        return data;
    

@api.route("/endpoints")
@api.doc()
class Endpoints(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM endpoint")
        data = cursor.fetchall() 
        return data;


@api.route("/policy_lines")
@api.doc()
class PolicyLines(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM policy_line")
        data = cursor.fetchall()
        if not data:
            data = dict()
        return data;
    

@api.route("/policy_line/<id>")
@api.doc()
class PolicyLine(Resource):
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM policy_line")
        data = cursor.fetchone()
        if not data:
            data = dict()
        return data;

    
    def put(self, id, policy):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(" insert into policy_line  values ('service_id', 'name', 'description text', 'path text', 'check_string text', 'methods text', 'scopes text'    )")
        return create_object(), 201

if __name__ == "__main__":
    app.run()
