import web

urls = (
    '/','Index',
    '/imc','Imc'
)

app = web.application(urls,globals())
render = web.template.render('views')

class Index:
    def GET (self):
        return render.index()
    
class Imc:
    def GET(self):
        return render.imc()
    
if __name__ == "__main__":
    app.run()