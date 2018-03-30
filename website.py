import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/events')
def eventsPage():
    return render_template('events.html')

@app.route('/admin')
def adminPage():
    return render_template('admin.html')

@app.route('/new_volunteer',methods = ['POST', 'GET'])
def new_volunteer():
   if request.method == 'POST':
      try:
         name = request.form['name']
         address = request.form['address']
         city = request.form['city']
         state = request.form['state']
         zipcode = request.form['zip']
         email = request.form['email']
         phone = request.form['phone']
         dob = request.form['date']
         event = request.form['event']
         language = 'English'
         print(name, address, city, state, zipcode, email, dob, event, language)

         with sqlite3.connect("/Users/michaelspainhour/Documents/workspace/VitaTaxPrep/VITA.db") as con:
             cur = con.cursor()
             cur.execute("INSERT INTO volunteers VALUES (?,?,?,?,?,?,?,?,?,?)", (name,address,city,state,zipcode,email,phone,dob,event,language) )

             con.commit()
             msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("results.html",msg = msg)
         con.close()

if __name__ == '__main__':
    app.run(debug=True)
