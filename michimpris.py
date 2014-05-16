#!/usr/bin/env python3
from gi.repository import Notify
import time, dbus, argparse, subprocess

class MPRISController(object):
    def __init__(self, busname):
        self.bus = dbus.SessionBus()
        self.busname = busname
        self.proxy = self.bus.get_object(self.busname, '/org/mpris/MediaPlayer2')
        self.player = dbus.Interface(self.proxy, 'org.mpris.MediaPlayer2.Player')
    def play(self):
        self.player.Play()
    def pause(self):
        self.player.Pause()
    def playpause(self):
        self.player.PlayPause()
    def forward(self):
        self.player.Next()
    def previous(self):
        self.player.Previous()
    def prev(self):
        self.previous()
    def props(self):
        return dbus.Interface(self.proxy, "org.freedesktop.DBus.Properties")
    def metadata(self):
        return self.props().Get("org.mpris.MediaPlayer2.Player", "Metadata")
    def title(self):
        return self.metadata()["xesam:title"].encode('utf-8')
    def album(self):
        data = self.metadata()
        if "xesam:album" in data:
            return data["xesam:album"].encode('utf-8')
        else:
            return None
    def artist(self):
        data = self.metadata()
        if "xesam:artist" in data:
            return data["xesam:artist"][0].encode('utf-8')
        else:
            return None
    def sayable(self):
        return "You are now listening to %s by %s from album %s" % (self.title().decode(), self.artist().decode(), self.album().decode())
    def main(self):
        parser = argparse.ArgumentParser(description='Control Spotify from CLI through DBus')
        parser.add_argument('--play', '-p', action="store_true", help='Starts playing. (Warning: it\'s buggy.)')
        parser.add_argument('--pause', '-s', action="store_true", help='Stops playing.')
        parser.add_argument('--toggle', '-t', action="store_true", help='Starts playing if it\'s paused. Stops if started.')
        parser.add_argument('--forward', '--next', '-f', '-n', action="store_true", help='Skips to the next track.')
        parser.add_argument('--previous', '--prev', '-b', action="store_true", help='Skips to the previous track.')
        parser.add_argument('--print', '-v', action="store_false", help='Prints out track metadata nicely.')
        parser.add_argument('--title', action="store_true", help='Prints title.')
        parser.add_argument('--album', action="store_true", help='Prints album.')
        parser.add_argument('--artist', action="store_true", help='Prints artist.')
        parser.add_argument('--notify', action="store_true", help='Throws a libnotify notification')
        parser.add_argument('--speak', action="store_true", help='Speaks that loud through espeak')
        args = parser.parse_args()
        if args.play:
            self.play()
        if args.pause:
            self.pause()
        if args.toggle:
            self.playpause()
        if args.forward:
            self.forward()
        if args.previous:
            self.previous()
        if args.title:
            print(self.title().decode())
        if args.album:
            print(self.album().decode())
        if args.artist:
            print(self.artist().decode())
        if args.print and not args.html:
            print(self.sayable())
        if args.notify:
            Notify.init("SPT")
            Notify.Notification.new("SPT", self.sayable(), "dialog-information").show()
        if args.speak:
            subprocess.Popen(["espeak", self.sayable()])

class DummyController(MPRISController):
    def __init__(self):
        pass
    def play(self):
        pass
    def pause(self):
        pass
    def playpause(self):
        pass
    def forward(self):
        pass
    def previous(self):
        pass
    def prev(self):
        pass
    def props(self):
        return None
    def metadata(self):
        return None
    def title(self):
        return None
    def album(self):
        return None
    def artist(self):
        return None
