from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


import csv
import os
import base64
from datetime import datetime

app = Flask(__name__)




def start():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': 3306,
        'database': 'chat'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT  City from Persons')
    results = cursor.fetchall() 
    cursor.close()
    connection.close()
    return results
# def start():
#    db =  mysql.connector.connect(
#    host="localhost",
#    port=32000,
#    user="root",
#    password="root",

# )
#    cursor = db.cursor(buffered=True)
#    results = cursor.execute('SELECT LastName FROM Persons')
#    cursor.close()
#    db.close()
   
#    return results


# # יצירת חיבור והגדרת SSL
# connection = mysql.connector.connect(
#    host="localhost",
#    port=32000,
#    user="root",
#    password="root",
#    ssl_disabled = False,  # הפעל חיבור מאובטח
#    ssl_version = "TLSv1.2"  # בחר TLSv1.2 או גרסה גבוהה יותר
# )


app.secret_key = '1234' 
# app.config['SESSION_COOKIE_SECURE'] = False 
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

def encode_password(password):
    encoded_bytes = base64.b64encode(password.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def decode_password(encoded_password):
    decoded_bytes = base64.b64decode(encoded_password.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == username:
                     return redirect("/login") 
        encode_pass=encode_password(password)        
        with open('users.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, encode_pass])

        session['username']=username    
        return redirect("/lobby") 

    return render_template('register.html')


def verify(username,password):
     with open('users.csv', 'r', newline='') as f: 
         reader = csv.reader(f)
         for row in reader:
                if row[0] == username and decode_password(row[1]) == password:
                    return True
     return False            


@app.route('/login', methods=['GET', 'POST'])
def login():
    
     if request.method== 'POST':
      username= request.form['username']
      password=request.form['password']
      if verify(username,password):
          session['username']=username
          return redirect('/lobby')
     return render_template('login.html') 
    

def room_is_exists(new_room):
    if os.path.exists(str(new_room) +".txt"):
       return True
    return False

@app.route('/lobby', methods=['GET','POST'])
def lobby():
 if session.get('username'):
    if request.method== 'POST':
        new_room = request.form['new_room']
        new_room = start()
        new_room = new_room[0]
        print(new_room)
        if room_is_exists(new_room):
           print("the room is already exists")
           return redirect('/lobby')   
        else:
         f= open("rooms/"+str(new_room) +".txt","w+")
    rooms =os.listdir('rooms')    
    for i in range(len(rooms)):
      rooms[i] = rooms[i][:-4]
    return render_template('lobby.html', rooms=rooms)
 else:

        return redirect('/')

    
@app.route('/api/chat/<room>', methods=['GET', 'POST'])
def render_chat(room):
    path=os.getenv('ROOMS_FILES_PATH')+room+".txt"
    if request.method == "POST":
        msg = request.form['msg']
        current_user = session['username']
        current_d_t = datetime.now()
        with open(path, "a") as file:
            file.write(f'[{current_d_t:%Y-%m-%d %H:%M:%S}] {current_user}: {msg} \n')
    with open(path, "r") as file:
        file.seek(0)
        lines = file.read()
    return lines


@app.route('/chat/<room>', methods=['GET', 'POST'])
def chat(room):
    if 'username' in session:
        return render_template('chat.html', room=room)
    else:
        return redirect('/')


@app.route('/api/chat_clear/<room>', methods=['POST'])
def clear_chat(room):
    path=os.getenv('ROOMS_FILES_PATH')+room+".txt"
    if request.method == 'POST':
         current_user = session['username']
         with open(path, "r") as file:
             file.seek(0)
             lines = file.readlines()
            #  for line in lines:
            #      if current_user in line:
            #          lines.
             lines_without_user = [line for line in lines if current_user not in line]
              
             with open(path, "w") as file:
               file.writelines(lines_without_user)
    
        
@app.route('/health')
def health():
    return "OK", 200
        


if __name__ == '__main__':
     app.debug = True
     app.run(host='0.0.0.0', port='5000', debug='True')