import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/events')
def eventsPage():
    return render_template('events.html')

@app.route('/admin')
def adminPage():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
