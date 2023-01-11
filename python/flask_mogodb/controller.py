from flask import(
    Flask,
    request,
    render_template,
    redirect,
    session,
    url_for
)
from dal import dao
import hashlib

app=Flask(__name__)
def generate_key(login):
    return hashlib.sha512(str(login).encode('utf-8')).hexdigest()

dao_departement=dao('school','depart')

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login',methods=['POST'])
def login():
    login=request.form['login']
    pwd=request.form['password']
    if login=='esisa' and pwd=='1234':
        app.secret_key=generate_key(login)
        session['user_id']=login
        return render_template('app.html')
    else:
        return render_template('login.html',error_auth='login or password incorrect')
@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('index'))
@app.route('/add',methods=['POST'])
def add():
    if 'user_id' in session :
        try:   
            object=dao_departement.add(request.get_json())
        except Exception as e:
            return e
        return 'add ok ',201
    else :
        return redirect('/')
@app.route('/departements')
def list():
    if 'user_id' in session :
        return dao_departement.list()
    else :
        return redirect('/')
@app.errorhandler(Exception)
def error(exception):
    return render_template('error.html',error=
     {
        "ip":request.remote_addr,
        "method":request.method,
        "error" :'sorry '
    })
if __name__=='__main__':
    app.run()