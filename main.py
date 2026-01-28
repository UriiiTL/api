import web
import json
import urllib.request

urls = (
    '/', 'Index',
    '/avatar', 'Avatar'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index("", "")

class Avatar:
    def POST(self):
        data = web.input(usuario="")
        usuario = data.usuario

        api_url = f"https://digimon-api.vercel.app/api/digimon/name/{usuario.lower()}"

        try:
            with urllib.request.urlopen(api_url) as response:
                result = json.loads(response.read())
                avatar_url = result[0]['img']
        except:
            avatar_url = ""

        return render.index(usuario, avatar_url)

if __name__ == "__main__":
    app.run()
