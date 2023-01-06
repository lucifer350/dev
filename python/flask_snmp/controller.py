from flask import (
    Flask,request,
    jsonify,
    render_template,
    redirect
)
import asyncio
from services import get_snmp, get_bulk
app=Flask(__name__)
@app.route('/bulk/<target>/<mib>/')
def bulk(target, mib):
    try :
  
        results = get_bulk(target, mib)
    except Exception as e :
        return e

    return results
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/get/<target>/<mib>/<var>')
def get(target, mib, var):
    try :
        results = get_snmp(target, mib, var)
    except Exception as e :
        return e

    return {
        results.split('=')[0] : results.split('=')[1]
    }, 201

@app.errorhandler(Exception)
def error(e):
    return {
        'client' : request.remote_addr,
        'method' : request.method,
        'error' : 'error in parameters'
    }

if __name__=='__main__':
    app.run(host='0.0.0.0')