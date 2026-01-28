import web

urls = (
    '/', 'Index',
    '/avatar', 'Avatar'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        # Página inicial sin avatar
        return render.index("", "")

class Avatar:
    def POST(self):
        data = web.input(usuario="")
        usuario = data.usuario

        avatar_url = f"https://api.dicebear.com/9.x/avataaars-neutral/svg?seed={usuario}"

        return render.index(usuario, avatar_url)

if __name__ == "__main__":
    app.run()
