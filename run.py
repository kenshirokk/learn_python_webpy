import web

movies = [
	{
		"title":"Forrent Gump",
		"year":1994
	},
	{
		"title":"Titanic",
		"year":1997
	}
]

render = web.template.render("html/")
db = web.database(dbn="sqlite", db="MovieSite.db")

urls = (
    "/", "hello"
    )

app = web.application(urls, globals())

class hello:
    def GET(sekf):
    	page = ""
    	for m in movies:
    		page += "%s(%d)\n" % (m["title"], m["year"])

    	dbmovies = db.select("movie")
    	return render.index(dbmovies)
    	#return render.index(movies)
        #return page

if __name__ == "__main__":
    app.run()
