#!/usr/bin/env python3
from michimpris import MPRISController

class SpotifyController(MPRISController):
    def __init__(self):
        MPRISController.__init__(self, 'org.mpris.MediaPlayer2.spotify')

if __name__ == '__main__':
	SpotifyController().main()
