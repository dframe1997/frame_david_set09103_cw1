from flask import Flask, url_for, redirect, render_template, abort
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

#json_data = open(url_for('static', filename="dataset.json"))
#gamelist = json.load(json_data)


mario = Game('Super Mario Odyssey', 'Platformer', '2017', 'Nintendo Switch', 'Nintendo EPD', 'Nintendo', 'Super Mario', 'https://vignette.wikia.nocookie.net/nintendo/images/3/3b/Super_Mario_Odyssey_Box_art_%28EU%29.jpg/revision/latest?cb=20170909175809&path-prefix=en')

sonic = Game('Sonic the Hedgehog', 'Platformer', '1991', 'Genesis', 'Sonic Team', 'Sega', 'Sonic the Hedgehog', 'http://www.boxequalsart.com/sonic-1-md-na-big.jpg')

civ = Game('Civilization VI', 'Strategy', '2016', 'PC', 'Firaxis Games', '2K Games', 'Civilization', 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Civilization_VI_cover_art.jpg/220px-Civilization_VI_cover_art.jpg')

forza = Game('Forza Horizon 4', 'Racing', '2018', 'Xbox One', 'Playground Games', 'Microsoft Studios', 'Forza', 'https://www.gamereactor.eu/media/92/forzahorizon4_2489263b.png')

horizon = Game('Horizon Zero Dawn', 'Action-Adventure', '2017', 'PlayStation 4', 'Guerrilla Games', 'Sony Interactive Entertainment', 'Horizon', 'http://images.pushsquare.com/news/2016/06/ps4_exclusive_horizon_zero_dawns_box_art_is_predictably_beautiful/large.jpg')

botw = Game('Breath of the Wild', 'Action-Adventure', '2017', 'Nintendo Switch', 'Nintendo EPD', 'Nintendo', 'The Legend of Zelda', 'https://vignette.wikia.nocookie.net/nintendo/images/5/50/The_Legend_of_Zelda_Breath_of_the_Wild_Switch_Boxart.jpg/revision/latest?cb=20170710030736&path-prefix=en')

drake = Game('Uncharted 4', 'Action-Adventure', '2016', 'PlayStation 4', 'Naughty Dog', 'Sony Interactive Entertainment', 'Uncharted', 'https://static1.gamespot.com/uploads/original/43/434805/2876987-uncharted4amazon.jpg')

cup = Game('Cuphead', 'Run and gun', '2017', 'Xbox One', 'StudioMDHR', 'StudioMDHR', 'Cuphead', 'https://www.mobygames.com/images/covers/l/429819-cuphead-windows-apps-front-cover.jpg')

gordon = Game('Half-Life 2', 'FPS', '2004', 'PC', 'Valve Corporation', 'Valve Corporation', 'Half-Life', 'https://upload.wikimedia.org/wikipedia/en/thumb/2/25/Half-Life_2_cover.jpg/220px-Half-Life_2_cover.jpg')

smash = Game('Super Smash Bros. Ultimate', 'Fighting', '2018', 'Nintendo Switch', 'Bandai Namco Studios', 'Nintendo', 'Super Smash Bros.', 'https://pre00.deviantart.net/17fb/th/pre/f/2018/176/d/b/super_smash_bros__ultimate_official_key_art_by_leafpenguins-dcfecah.png')

gamelist=[mario, sonic, civ, forza, horizon, botw, drake, cup, gordon, smash]

@app.route('/')
def noPath():
	return redirect(url_for('games'))

@app.route('/<filterItem>')
def filterOptions(filterItem='genre'):
	try: 
		return render_template('list.html', option=filterItem, title=filterItem, optionlist=getFilterList(filterItem))
	except: 
		abort(404)

@app.route('/<filterItem>/<name>')
def filterResults(filterItem='genre', name=None):
	genre = {'name': name}
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
	return render_template('list.html',option='games', games='true', title='All', optionlist=gamelist)

def getFilterList(filterOption):
	optionList = []
	for game in gamelist:
		value = getattr(game, filterOption)
		if value not in optionList:
			optionList.append(value)
	return optionList
