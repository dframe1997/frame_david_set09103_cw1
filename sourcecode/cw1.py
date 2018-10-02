from flask import Flask, url_for, redirect, render_template
app = Flask(__name__)

class Game:
    def __init__(self, name, genre, boxart):
        self.name=name
        self.genre=genre
	self.boxart=boxart

mario = Game('mario', 'platformer', 'http://www.nag.co.za/wp-content/uploads/2014/12/doomcover.jpg')
sonic = Game('sonic', 'platformer', 'http://www.nag.co.za/wp-content/uploads/2014/12/doomcover.jpg')
civ = Game('civ', 'strategy','http://www.nag.co.za/wp-content/uploads/2014/12/doomcover.jpg')
forza = Game('forza', 'racing','http://www.nag.co.za/wp-content/uploads/2014/12/doomcover.jpg')

gamelist=[mario, sonic, civ, forza]

@app.route('/')
def noPath():
	return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('home.html', gamelist=gamelist)

@app.route('/genre')
def genres():
	return render_template('list.html', option='genre', optionlist=[{'name':"strategy"}, {'name':"rpg"}, {'name':"platformer"}, {'name':"racing"}])

@app.route('/genre/<name>')
def genre(name=None):
	genre = {'name': name}
	optionlist = list(filter(lambda x: x.genre == name, gamelist)) #https://stackoverflow.com/questions/598398/searching-a-list-of-objects-in-python
	return render_template('list.html', option='games', optionlist=optionlist)

@app.route('/games/<name>')
def game(name=None):
	game = list(filter(lambda x: x.name == name, gamelist))
	return render_template('game.html', game=game[0])

@app.route('/games')
def games():
	return render_template('list.html',option='games', optionlist=gamelist)
