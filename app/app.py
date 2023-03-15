from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

bootstrap = Bootstrap5(app)

with open('metadata.jsonl', 'r') as json_file:
    json_list = list(json_file)


movies = {}

for json_str in json_list:
    movie = json.loads(json_str)
    movies[str(movie['id'])] = movie

print("loaded movies metadata")

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trending')
def trending():
    items = metarank('trending', {'count': 96 })
    return render_template('trending.html', movies=items)

@app.route('/rec/<int:movie>')
def rec(movie):
    request = {'count': 6, 'items':[str(movie)]}
    recs = {'ALS Matrix Factorization': metarank('similar', request), 'MiniLM-v2-L6': metarank('minilm', request), 'Cohere.ai': metarank('cohere', request)}
    return render_template('rec.html', movie=movies[str(movie)], recs=recs)


def metarank(handle, request):
    items = []
    for item in json.loads(requests.post('http://localhost:8080/recommend/'+handle, json=request).content)['items']:
        id = str(item['item'])
        movie = movies[id]
        items.append(movie)
    return items


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
