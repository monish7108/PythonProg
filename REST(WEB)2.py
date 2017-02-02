import web

urls = (

    '/SomePageHello','SomePageHello',
    '/SomePageGoodbye','SomePageGoodbye',


    )

app = web.application(urls, globals())

class SomePageHello:
    def GET(self):
        user_data = web.input(name="no data")
        return "<h1> Hello " + user_data.name + "</h1>"

class SomePageGoodbye:
    def GET(self):
        user_data = web.input(name="no data")
        return "<h1> Goodbye " + user_data.name + "</h1>"



if __name__ == "__main__":
    app.run()