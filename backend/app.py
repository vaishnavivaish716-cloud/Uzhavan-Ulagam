from flask import Flask, send_from_directory, request, redirect, session
import os
app = Flask(__name__)
app.secret_key = 'salem2026'
BASE = os.path.dirname(os.path.abspath(__file__))
FRONT = os.path.abspath(os.path.join(BASE, '../frontend'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form.get('username')=='admin' and request.form.get('password')=='admin123':
            session['logged_in']=True
            return redirect('/admin')
        return "Thappu da! <a href='/login'>Retry</a>"
    return send_from_directory(FRONT, 'login.html')

@app.route('/admin')
def admin():
    if not session.get('logged_in'): return redirect('/login')
    return send_from_directory(FRONT, 'admin.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/')
def home(): return send_from_directory(FRONT, 'index.html')

@app.route('/<path:f>')
def files(f): return send_from_directory(FRONT, f)

if __name__=='__main__':
    print("👉 http://127.0.0.1:5000/login  admin/admin123")
    app.run(debug=True, port=5000)