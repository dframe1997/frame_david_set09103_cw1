from flask import Flask, url_for, redirect, render_template, abort, json, request
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
jsonurl = os.path.join(app.static_folder, 'dataset.json')
jsonfile = open(jsonurl)
jsondata = json.load(jsonfile)

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

@app.route('/addgame', methods=['POST','GET'])
def addgame():
	if request.method == 'POST':
	  print request.form
	  name = request.form['name']
	  genre = request.form['genre']
          year = request.form['year']
          platform = request.form['platform']
	  developer = request.form['developer']
	  publisher = request.form['publisher']
	  series = request.form['series']
	  boxart = request.form['boxart']
	  newGame = Game(name, genre, year, platform, developer, publisher, series, boxart)
	  
	  jsondata.append({"name": name, "genre": genre, "year": year, "platform": platform, "developer": developer, "publisher":publisher, "series":series, "boxart":boxart})

	  jsonfile = open(jsonurl, 'w')
	  jsonfile.write(json.dumps(jsondata))
	  jsonfile.close()

	  gamelist = loadGames()
	  return "Game added"
	else:
	  return render_template("addgame.html")


def getFilterList(filterOption):
	gamelist = loadGames()
        optionList = []
	for game in gamelist:
		value = getattr(game, filterOption)
		if value not in optionList:
			optionList.append(value)
	return optionList
