
from flaskext.mysql import MySQL
from flask import Flask

class DBcon():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def conexion(self):
        mysql = MySQL()
        control = Flask(__name__)
        control.config['MYSQL_DATABASE_USER'] = 'wtec'
        control.config['MYSQL_DATABASE_PASSWORD'] = 'wtec.s'
        control.config['MYSQL_DATABASE_DB'] = 'wtec_webapp'
        control.config['MYSQL_DATABASE_HOST'] = '192.168.227.1'
        mysql.init_app(control)
        return mysql