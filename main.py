import web
import json
import urllib.request

urls = (
    '/', 'Index',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        api_url = "https://digimon-api.vercel.app/api/digimon"

        try:
            with urllib.request.urlopen(api_url) as response:
                digimons = json.loads(response.read())
        except:
            digimons = []

        return render.index(digimons)

if __name__ == "__main__":
    app.run()
