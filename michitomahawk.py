#!/usr/bin/env python3
from michimpris import MPRISController
import time, dbus, argparse, subprocess

class TomahawkController(MPRISController):
    def __init__(self):
        MPRISController.__init__(self, 'org.mpris.MediaPlayer2.tomahawk')

if __name__ == '__main__':
	TomahawkController().main()
