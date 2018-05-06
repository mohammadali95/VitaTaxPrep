import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

eventsIn = {'jandb':'Jeans and Bling', 'tt':'Turkey Trot', 'stheb':'Stuff the Bus', 'vftp':'Free Tax Preparation'}
hoursIn = {'9to10':'9to10', '10to11':'10to11', '11tonoon':'11tonoon', 'noonto1':'noonto1', '1to2':'1to2', '2to3':'2to3'}


@app.route('/events')
def eventsPage():
    with sqlite3.connect("VITA.db") as con:
        cur = con.cursor()
        cur.execute("SELECT name, image, description FROM events")
        events = cur.fetchall()
        return render_template("events.html", events=events)

@app.route('/admin', methods = ['POST', 'GET'])
def adminPage():
	con = sqlite3.connect('VITA.db')
	c = con.cursor()
	if request.method == 'GET':
		c.execute("SELECT DISTINCT * FROM volunteers JOIN hours ON volunteers.email = hours.email")
		data = c.fetchall()
		print(data)
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
		if string == "SELECT * FROM volunteers JOIN hours ON volunteers.email = hours.email WHERE hours.eventName = ":
			c.execute("SELECT * FROM volunteers JOIN hours ON volunteers.email = hours.email WHERE hours.eventName = Null")
			data = c.fetchall()
			return render_template('admin.html', data=data)
		c.execute(string)
		data = c.fetchall()
		return render_template('admin.html', data=data)

def buildNameQuery(name):
	execute = 'SELECT DISTINCT * FROM volunteers JOIN hours ON volunteers.email = hours.email WHERE volunteers.name like ' + "'" + name + "%'"
	return execute

def buildEventsQuery(events):
    print(events)
    execute = 'SELECT * FROM volunteers JOIN hours ON volunteers.email = hours.email WHERE eventName = '
    if len(events) > 1:
        for i in events:
            if i == events[-1]:
                execute += "'" + eventsIn[i] + "'"
            else:
                execute += "'" + eventsIn[i] + "'" + ' OR hours.eventName = '
        print(execute)
        return execute
    else:
        for i in events:
            execute +=  "'" + eventsIn[i] + "'"
        print(execute)
        return execute
		
@app.route('/new_volunteer',methods = ['POST', 'GET'])
def new_volunteer():
	if request.method == 'POST':
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
		timeList = []
		for time in hoursIn:
			if request.form.get(time, False) == 'on':
				timeList.append(time)
		print(timeList)
		timeStr = ','.join(timeList)
		con = sqlite3.connect("VITA.db")
		cur = con.cursor()
		cur.execute("INSERT INTO volunteers VALUES (?,?,?,?,?,?,?,?,?)", (str(name), str(address), str(city), str(state), str(zipcode), str(email), str(phone), str(dob), str(language)))
		cur.execute("INSERT INTO hours VALUES (?,?,?)", (str(email), str(event), str(timeStr)))
		con.commit()
		msg = "Record successfully added"
		con.close()
		return render_template("results.html", msg=msg)
			
					
if __name__ == '__main__':
    app.run(debug=True)