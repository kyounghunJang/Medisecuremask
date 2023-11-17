import pymysql
from flask import Flask, render_template, request, session, send_file
from jinja2 import Template
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__, static_folder='./static')
# MySQL에 연결
connection = pymysql.connect(
    host='ec2-43-201-91-32.ap-northeast-2.compute.amazonaws.com',
    user='jang',
    password='jang',
    database='mydb',
    port=3306   
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM img_url limit 3")
db=cursor.fetchall()
db=list(db)
new_db=[]
for url in db:
    url=str(url)
    url=url.replace('(','').replace(')','').replace(',','').replace("'","")
    new_db.append(url)
app.secret_key = 'jang'
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/post", methods=['POST'])
def post():
    value= request.form['input']
    session['value']=value
    cursor.execute("SELECT url FROM img_url WHERE category=%s", value)
    db= cursor.fetchall()
    db=list(db)
    new_db=[]
    for url in db:
        url=str(url)
        url=url.replace('(','').replace(')','').replace(',','').replace("'","")
        new_db.append(url)
    limit3=new_db[0:3]
    print(new_db)
    print(limit3)
    return render_template("post.html", db=new_db, limit3=limit3,value=value)

@app.route('/download', methods=['GET','POST'])
def download():
    value= session.pop('value', None)
    print(value)
    path = '/home/ubuntu/'+str(value)+'.zip'
    return send_file(path, as_attachment=True) 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)