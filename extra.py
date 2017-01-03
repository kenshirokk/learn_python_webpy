import web
import urllib2
import get_movie as gm
import time

db = web.database(dbn="sqlite", db="MovieSite.db")


ids = db.select("failed_ids")

for id in ids:
	try:
		response = urllib2.urlopen("https://api.douban.com/v2/movie/subject/"+id)
		data = response.read()
		gm.save(data)
	except:
		db.insert("bak", id="id")
	time.sleep(3)