from flask import Flask, url_for, redirect, render_template
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

mario = Game('Super Mario Odyssey', 'Platformer', '2017', 'Switch', 'Nintendo EPD', 'Nintendo', 'Super Mario', 'https://vignette.wikia.nocookie.net/nintendo/images/3/3b/Super_Mario_Odyssey_Box_art_%28EU%29.jpg/revision/latest?cb=20170909175809&path-prefix=en')

sonic = Game('Sonic the Hedgehog', 'Platformer', '1991', 'Genesis', 'Sonic Team', 'Sega', 'Sonic the Hedgehog', 'http://www.boxequalsart.com/sonic-1-md-na-big.jpg')

civ = Game('Civilization VI', 'Strategy', '2016', 'PC', 'Firaxis Games', '2K Games', 'Civilization', 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Civilization_VI_cover_art.jpg/220px-Civilization_VI_cover_art.jpg')

forza = Game('Forza Horizon 4', 'Racing', '2018', 'Xbox One', 'Playground Games', 'Microsoft Studios', 'Forza', 'https://www.gamereactor.eu/media/92/forzahorizon4_2489263b.png')

horizon = Game('Horizon Zero Dawn', 'RPG', '2017', 'PlayStation 4', 'Guerrilla Games', 'Sony Interactive Entertainment', 'Horizon', 'http://images.pushsquare.com/news/2016/06/ps4_exclusive_horizon_zero_dawns_box_art_is_predictably_beautiful/large.jpg')

gamelist=[mario, sonic, civ, forza, horizon]

@app.route('/')
def noPath():
	return redirect(url_for('games'))

@app.route('/<filterItem>')
def filterOptions(filterItem='genre'):
	return render_template('list.html', option=filterItem, title=filterItem, optionlist=getFilterList(filterItem))

@app.route('/<filterItem>/<name>')
def filterResults(filterItem='genre', name=None):
	genre = {'name': name}
	optionlist = list(filter(lambda x: getattr(x,filterItem) == name, gamelist)) 
	return render_template('list.html', option=filterItem, games='true', title=name, optionlist=optionlist)

@app.route('/games/<name>')
def game(name=None):
	game = list(filter(lambda x: x.name == name, gamelist))
	return render_template('game.html', game=game[0])


@app.route('/games')
def games():
	return render_template('list.html',option='games', games='true', title='All', optionlist=gamelist)

def getFilterList(filterOption):
	optionList = []
	for game in gamelist:
		value = getattr(game, filterOption)
		if value not in optionList:
			optionList.append(value)
	return optionList
