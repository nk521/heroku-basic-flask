from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def hello_ssti():
	person = {'name':"null", 'secret':"nullctf{}"}
	if request.args.get('name'):
		person['name'] = request.args.get('name')
	#template = '''<h2>Hello %s!</h2>''' % person['name']
	template = "<h2>Hello" + person['name'] +"!</h2>"
	return render_template_string(template, person=person)

if __name__ == "__main__":
	app.run(debug=True)
