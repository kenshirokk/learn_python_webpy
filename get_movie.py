# coding=utf-8
import urllib, urllib2
import json
import time
import web

baseurl = "https://api.douban.com/"
top250 = "/v2/movie/top250"
subject = "/v2/movie/subject/"

db = web.database(dbn="sqlite", db="MovieSite.db")

#response = urllib2.urlopen(baseurl+top250)
#data = response.read()
#json_data = json.loads(data)
#movies = json_data["subjects"]

#获得top250的电影id  然后根据id一个一个取电影,保存到数据库
movie_ids = []
for i in range(0, 250, 50):
	response = urllib2.urlopen(baseurl+top250+"?start=%d&count=50" % i)
	data = response.read()
	json_data = json.loads(data)
	movies50 = json_data["subjects"]
	for m in movies50:
		movie_ids.append(m["id"])
	time.sleep(3)

def save(movie):
	movie = json.loads(movie)

	db.insert("movie", 
		id 			= int(movie["id"]), 
		title 		= movie["title"], 
		original_title 		= movie["original_title"], 
		alt 		= movie["alt"], 
		image		= movie["images"]["large"], 
		directors	= ",".join(d["name"] for d in movie["directors"]), 
		casts		= ",".join(c["name"] for c in movie["casts"]), 
		year		= movie["year"])

failed_ids = []
for id in movie_ids:
	try:
		response = urllib2.urlopen(baseurl+subject+id)
		data = response.read()
		save(data)
	except:
		failed_ids.append(id)
		db.insert("failed_ids", id = id)

	time.sleep(2)