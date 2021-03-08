from sanic import Sanic
from sanic.response import json
from sanic import response
import socket
import json as jsonIP
import urllib.request

app = Sanic(name="name")

HTML_FORM = '''

<p>{}</p>
<form action="/test" method="POST">
  <input class="url" id="url" name="url"
    placeholder="Url" type="text" value="">
  <input id="submit" name="submit" type="submit" value="Launch">
</form>'''
def getSiteLocation(site):
    ipSite = socket.gethostbyname(site)
    return jsonIP.load(urllib.request.urlopen('http://ipinfo.io/' + ipSite))


@app.route('/test', methods=['GET', 'POST'])
async def test(request):
    message = ''
    if request.method == "POST":
        data = getSiteLocation(request.form.get('url'))
        message = data['region']
        #return response.json({'ip':data['ip'], 'hostname': data['hostname'], "city": data['city'], "region": data['region'], 'country': data['country'], "location": data['loc'], "organization": data['org'], 'postal': data['postal'], 'timezone': data['timezone']})
    return response.html(HTML_FORM.format(message))

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

