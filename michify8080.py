#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, json
import subprocess, random, sys
import michispotify as spotify
from alsaaudio import Mixer
app = Flask(__name__)
spt = spotify.SpotifyController()
mxr = Mixer()

volumes = [0,0,0,0,0,0]
volumes[0] = 0
volumes[1] = 80
volumes[2] = 85
volumes[3] = 90
volumes[4] = 95
volumes[5] = 100


password = random.randint(100000,999999)
print(password)

@app.route('/')
def homepage():
    return render_template('home.html', artist=spt.artist().decode(), album=spt.album().decode(), track=spt.title().decode(), css=url_for('static', filename='style.css'), js=url_for('static', filename='additional.js'), linkn=url_for('apinext'), linkp=url_for('prevtrack'), linkr=url_for('homepage'), linkt=url_for('toggleplay'), vol1=url_for('volume', volume=volumes[1]), vol2=url_for('volume', volume=volumes[2]), vol3=url_for('volume', volume=volumes[3]), vol4=url_for('volume', volume=volumes[4]), vol5=url_for('volume', volume=volumes[5]), volm=url_for('volume', volume=volumes[0]), jsonstatusapi=url_for('apijsonstatus'), volume=mxr.getvolume('playback')[0])

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

@app.route('/v/<int:volume>')
@app.route('/volume/<int:volume>')
def volume(volume):
    if volume <= 100 and volume >= 0:
        mxr.setvolume(volume)
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

@app.route('/api/volume/<int:volume>')
def apivolume(volume):
    if volume <= 5 and volume >= 0:
        mxr.setvolume(volumes[0])
    return ""

@app.route('/sd/<int:passcode>')
def shutdown(passcode):
    if passcode == password:
        subprocess.Popen('poweroff')
        sys.exit(0)
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
