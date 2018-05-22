from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/main')
def hello_ssti():
	person = {'name':"world", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	template = '''<h2>Hello %s!</h2>''' % person['name']
	return render_template_string(template, person=person)

####
# Private function if the user has local files.
###
def get_user_file(f_name):
	with open(f_name) as f:
		return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file # Allows for use in Jinja2 templates

if __name__ == "__main__":
	app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

