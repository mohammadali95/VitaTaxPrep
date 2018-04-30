import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

eventsIn = {'jandb':'Jeans and Bling', 'tt':'Turkey Trot', 'stheb':'Stuff the Bus', 'vftp':'Free Tax Preparation'}
<<<<<<< HEAD
hoursIn = {'9to10':'9to10', '10to11':'10to11', '11tonoon':'11tonoon', 'noonto1':'noonto1', '1to2':'1to2', '2to3':'2to3'}
=======
>>>>>>> origin/master

@app.route('/events')
def eventsPage():
    return render_template('events.html')

<<<<<<< HEAD
@app.route('/admin', methods = ['POST', 'GET'])
def adminPage():
    con = sqlite3.connect('VITA.db')
    c = con.cursor()
    if request.method == 'GET':
        c.execute('SELECT * FROM volunteers')
        data = c.fetchall()
        return render_template('admin.html', data = data)
    else:
        events = []
        name = request.form.get('VolName')
        if name != None:
            string = str(buildNameQuery(name))
            print(string)
            print(c.execute(string))
            c.execute(string)
            data = c.fetchall()
            return render_template('admin.html', data=data)
        for event in eventsIn:
            if request.form.get(event, False) == 'on':
                events.append(event)
        string = buildEventsQuery(events)
        if string == "SELECT * FROM volunteers WHERE event = ":
            c.execute("SELECT * FROM volunteers WHERE event = Null")
            data = c.fetchall()
            return render_template('admin.html', data=data)
        c.execute(string)
        data = c.fetchall()
        return render_template('admin.html', data=data)

def buildNameQuery(name):
    execute = 'SELECT * FROM volunteers WHERE name LIKE ' + "'" + name + "%'"
    return execute
=======
		@app.route('/admin')
		def adminPage():
			con = sqlite3.connect('VITA.db')
			c = con.cursor()
			if request.method == 'GET':
				c.execute('SELECT * FROM volunteers')
				data = c.fetchall()
				return render_template('admin.html', data = data)
			else:
				events = []
				name = request.form['VolName']
				if name != "":
					string = str(buildNameQuery(name))
					print(string)
					print(c.execute(string))
					c.execute(string)
					data = c.fetchall()
					return render_template('admin.html', data=data)
					for event in eventsIn:
						if request.form.get(event, False) == 'on':
							events.append(event)
							string = buildEventsQuery(events)
							if string == "SELECT * FROM volunteers WHERE event = ":
								c.execute("SELECT * FROM volunteers WHERE event = Null")
								data = c.fetchall()
								return render_template('admin.html', data=data)
								c.execute(string)
								data = c.fetchall()
								return render_template('admin.html', data=data)

def buildNameQuery(name):
	execute = 'SELECT * FROM volunteers WHERE name like ' + "'" + name + "%'"
	return execute
>>>>>>> origin/master

def buildEventsQuery(events):
    print(events)
    execute = 'SELECT * FROM volunteers WHERE event = '
    if len(events) > 1:
        for i in events:
            if i == events[-1]:
                execute += "'" + eventsIn[i] + "'"
            else:
                execute += "'" + eventsIn[i] + "'" + ' OR event = '
        print(execute)
        return execute
    else:
        for i in events:
            execute +=  "'" + eventsIn[i] + "'"
        print(execute)
        return execute

<<<<<<< HEAD
@app.route('/new_volunteer', methods = ['POST', 'GET'])
=======
@app.route('/new_volunteer',methods = ['POST', 'GET'])
>>>>>>> origin/master
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
         timeList = []
         for time in hoursIn:
             if request.form.get(time, False) == 'on':
                 timeList.append(time)
         print(timeList)
         language = 'English'

         with sqlite3.connect("/Users/michaelspainhour/Documents/workspace/VitaTaxPrep/VITA.db") as con:
             cur = con.cursor()
             print("INSERT INTO volunteers VALUES (?,?,?,?,?,?,?,?,?,?,?)", (name,address,city,state,zipcode,email,phone,dob,event,timeList,language) )
             cur.execute("INSERT INTO volunteers VALUES (?,?,?,?,?,?,?,?,?,?,?)", (name,address,city,state,zipcode,email,phone,dob,event,str(timeList),language) )
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
