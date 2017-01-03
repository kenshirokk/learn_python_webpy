# coding=utf-8
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
    "/", "hello",
    "/movie/(\d+)", "movie"
    )

app = web.application(urls, globals())

class hello:
    def GET(self):
    	page = ""
    	for m in movies:
    		page += "%s(%d)\n" % (m["title"], m["year"])

    	dbmovies = db.select("movie")
    	return render.index(dbmovies)
    	#return render.index(movies)
        #return page

    def POST(self):
        data = web.input()
        condition = "title like '%" + data.title + "%'";
        dbmovies = db.select("movie", where = condition)
        return render.index(dbmovies)

class movie:
    def GET(self, movie_id):
        movie_id = int(movie_id)
        dbmovie = db.select('movie', where = 'id=$movie_id', vars = locals())[0]
        return render.movie(dbmovie)

if __name__ == "__main__":
    app.run()
