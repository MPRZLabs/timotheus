#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, json
import subprocess, random, sys
import michispotify as spotify
app = Flask(__name__)
spt = spotify.SpotifyController()

password = random.randint(100000,999999)
print(password)

@app.route('/')
def homepage():
    return render_template('home.html',  artist=spt.artist().decode(), album=spt.album().decode(), track=spt.title().decode(), css=url_for('static', filename='style.css'), js=url_for('static', filename='additional.js'), linkn=url_for('apinext'), linkp=url_for('apiprev'), linkr=url_for('homepage'), linkt=url_for('apitoggle'), jsonstatusapi=url_for('apijsonstatus'))

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static',filename='favicon.ico'))

@app.route('/n')
@app.route('/next')
def nexttrack():
    spt.forward()
    return redirect(url_for('homepage'))

@app.route('/p')
@app.route('/prev')
def prevtrack():
    spt.previous()
    return redirect(url_for('homepage'))

@app.route('/t')
@app.route('/toggle')
def toggleplay():
    spt.playpause()
    return redirect(url_for('homepage'))

@app.route('/api/shortstatus')
def apishortstatus():
    return "%s - %s" % (spt.title().decode(), spt.artist().decode())

@app.route('/api/jsonstatus')
def apijsonstatus():
    return json.dumps({'artist':spt.artist().decode(),'album':spt.album().decode(),'track':spt.title().decode()})

@app.route('/api/toggle')
def apitoggle():
    spt.playpause()
    return ""

@app.route('/api/next')
def apinext():
    spt.forward()
    return ""

@app.route('/api/prev')
def apiprev():
    spt.previous()
    return ""

@app.route('/sd/<int:passcode>')
def shutdown(passcode):
    if passcode == password:
        subprocess.Popen('poweroff')
        sys.exit(0)
    return redirect(url_for('homepage'))

@app.route('/robots.txt')
def robots():
  return """User-Agent: *
Disallow: /"""

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
