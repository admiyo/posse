import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
    

from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from flask import json
from flask import request
from pymysql.cursors import DictCursor

from flask_restplus import Api
from flask_restplus import Resource



app = Flask(__name__)


if True:
    dbconn = MySQL(cursorclass=DictCursor)
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'posse'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'posse'
    app.config['MYSQL_DATABASE_DB'] = 'posse'
    app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
    dbconn.init_app(app)
else:
    pass


api = Api(app, version='1.0', title='Posse',
    description='RBAC Policy Management',
)

@app.route('/ui')
def showSignUp():
    return render_template('index.html')

@api.route("/services")
@api.doc()
class Service(Resource):
    def get(self):
        conn = dbconn.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM service")
        data = cursor.fetchall() 
        if not data:
            data = dict()
        return data;


@api.route("/service/<service_id>/policy")
@api.doc()
class ServicePolicy(Resource):
    def get(self, service_id):
        conn = dbconn.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM policy_line where service_id = %s" % service_id)
        data = cursor.fetchall() 
        if not data:
            data = dict()
        return data;
    
    def put(self, service_id):
        conn = dbconn.connect()
        cursor = conn.cursor()
        if request.content_type == 'text/x-yaml':
            policies = yaml.load(request.data ,Loader=Loader)
        else:
            policies = request.json

        default = ''
        for k, v in policies.items():

            if k == 'default':
                default = v
            if v == '':
                check_string = "rule:default"
            else:
                check_string = v

            t = {'service_id': service_id,
                 'name':k,
                 'check_string':check_string }
            result = cursor.execute(" insert into policy_line  values ('%(service_id)s', '%(name)s', 'description text', 'path text', '%(check_string)s', 'methods text', 'scopes text')" % t)
        try:
            conn.commit()
            return self.get('service_id'), 201
        except Exception as e:
            print("Problem inserting into db: " + str(e))
            return "", 500



@api.route("/endpoints")
@api.doc()
class Endpoints(Resource):
    def get(self):
        conn = dbconn.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM endpoint")
        data = cursor.fetchall() 
        if not data:
            data = dict()
        return data;


@api.route("/policy")
@api.doc()
class PolicyLines(Resource):
    def get(self):
        conn = dbconn.connect()
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
        conn = dbconn.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM policy_line")
        data = cursor.fetchone()
        if not data:
            data = dict()
        return data;

    
    def put(self, id, policy):
        conn = dbconn.connect()
        cursor = conn.cursor()
        cursor.execute(" insert into policy_line  values ('service_id', 'name', 'description text', 'path text', 'check_string text', 'methods text', 'scopes text'    )")
        return create_object(), 201

if __name__ == "__main__":
    app.run()
