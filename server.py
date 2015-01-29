from flask import Flask, render_template
import json
import requests
import urllib
from torrent import Torrent
from bs4 import BeautifulSoup

app = Flask(__name__)

TORRENTZ_URL = "http://torrentz.eu"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search/<term>')
def search(term):
	request = create_search_request(term)
	print "fetcihing " + request.url
	
	html = BeautifulSoup(request.text)
	results_div = html.find(lambda e: e.name == 'div' and e.has_attr('class') and e['class'] == ['results'])

	torrents = []
	for item in results_div.find_all('dl'):
		try:
			new_torrent = Torrent()
			new_torrent.name = item.dt.a.text
			new_torrent.rel_url = item.dt.a['href'].replace('/','')

			age_span = item.dd.find(lambda e: e.name == 'span' and e.has_attr('class') and e['class'] == ['a']).span
			new_torrent.date_exact = age_span['title']
			new_torrent.date_relative = age_span.text

			new_torrent.size = item.dd.find(lambda e: e.name == 'span' and e.has_attr('class') and e['class'] == ['s']).text
			new_torrent.seeders = item.dd.find(lambda e: e.name == 'span' and e.has_attr('class') and e['class'] == ['u']).text

			torrents.append(new_torrent)
	
		except Exception, e:
			print e
			continue

	return json.dumps(torrents, default=lambda o: o.__dict__)

@app.route('/magnet/<rel_url>')
def magnet(rel_url):
	""" Returns all source links from which to fetch magnet links form. """
	req_url = TORRENTZ_URL + "/" + rel_url
	print req_url
	link_list_request = requests.get(req_url)
	link_list_html = BeautifulSoup(link_list_request.text)
	downloads_div = link_list_html.find(lambda e: e.name == 'div' and e.has_attr('class') and e['class'] == ['download'])
	for link in downloads_div.find_all('a'):
		try:
			url = link['href']
			if url.startswith('http'):
				magnet = get_magnet(url)
				if magnet:
					return json.dumps({'magnet':magnet})
		except Exception:
			continue
	return json.dumps({'magnet': None})

def create_search_request(search_term, page=0):
	""" Takes in percent incoded string, e.g: foo%20bar """
	torrentz_search_url = TORRENTZ_URL + "/search?"
	params = {"q": urllib.unquote(str(search_term)), "p": page}
	return requests.get(torrentz_search_url, params=params)

def get_magnet(url):
	magnet_source_request = requests.get(url)
	magnet_source_html = BeautifulSoup(magnet_source_request.text)
	for link in magnet_source_html.find_all('a'):
		if link.has_attr('href') and link['href'].startswith('magnet:?'):
			return link['href']
	return None

if __name__ == '__main__':
	app.run(debug=True)

