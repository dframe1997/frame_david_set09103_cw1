from flask import Flask, url_for, redirect, render_template, abort, json
import os
app = Flask(__name__)


class Game:
    def __init__(self, name, genre, year, platform, developer, publisher, series, boxart):
        self.name=name
        self.genre=genre
        self.year=year
        self.platform=platform
        self.developer=developer
        self.publisher=publisher
        self.series=series
	self.boxart=boxart


gamelist = []
jsonfile = jsonfile = os.path.join(app.static_folder, 'dataset.json')
jsondata = json.load(open(jsonfile))

def loadGames():
    jsonfile = os.path.join(app.static_folder, 'dataset.json')
    jsondata = json.load(open(jsonfile))

    newgamelist = []
    for item in jsondata:
        newgamelist.append(Game(item['name'], item['genre'], item['year'], item['platform'], item['developer'], item['publisher'], item['series'], item['boxart']))
    return newgamelist

gamelist = loadGames()

@app.route('/')
def noPath():
	return redirect(url_for('games'))

@app.route('/<filterItem>')
def filterOptions(filterItem='genre'):
	gamelist = loadGames()
	try: 
		return render_template('list.html', option=filterItem, title=filterItem, optionlist=getFilterList(filterItem))
	except: 
		abort(404)

@app.route('/<filterItem>/<name>')
def filterResults(filterItem='genre', name=None):
	gamelist = loadGames()
	try: 
		optionlist = list(filter(lambda x: getattr(x,filterItem) == name, gamelist)) 
		return render_template('list.html', option=filterItem, games='true', title=name, optionlist=optionlist)
	except:
		abort(404)


@app.route('/force404')
def error():
	abort(404)

@app.route('/games/<name>')
def game(name=None):
        gamelist = loadGames()
	game = list(filter(lambda x: x.name == name, gamelist))
	try: 
		return render_template('game.html', game=game[0])
	except:
		abort(404)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html')

@app.route('/games')
def games():
	gamelist = loadGames()
	return render_template('list.html',option='games', games='true', title='All', optionlist=gamelist)

@app.route('/jsontest')
def jsontest():
	return str(jsondata);

def getFilterList(filterOption):
	gamelist = loadGames()
        optionList = []
	for game in gamelist:
		value = getattr(game, filterOption)
		if value not in optionList:
			optionList.append(value)
	return optionList
