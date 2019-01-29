from flask import Flask, render_template
app = Flask(__name__)

forum_posts = [
	{
	'title':'New Updates & Discussions!',
	'text':'Talk about new updates from the Picroma Team here!',
	},
	{
	'title':'Original Content',
	'text':'Talk about new updates from the Picroma Team here!',
	},
	{
	'title':'Tips & Tricks/Game Guides!',
	'text':'Talk about new updates from the Picroma Team here!',
	},
	{
	'title':'Off Topic Discussions!',
	'text':'Talk about new updates from the Picroma Team here!',
	}
]


@app.route("/")
def hello():
	return render_template("home.html", posts=forum_posts)

@app.route("/info")
def info():
	return "<h1> Information </h1>"




if __name__ == '__main__':
	app.run(debug=True)


