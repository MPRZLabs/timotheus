Icarus Analysis System
======================
This is @Michcioperz's set of not really useful programs that he uses to make himself feel more like a super secret agent spy scientist. Stuff he made when he was bored.

Programs included
-----------------

* __Icarus__ - Scientific-looking something that looks cool and would be useful for a sci-fi movie.
 * _Name's origin:_ Icarus is a pun on something. You won't figure out. It's nothing personal, you just won't, cause I'm complicated.
 * _Dependencies:_ Python 3, Espeak, Cmatrix
* __Halp__ - Launch poweroff command, but give me time to change my mind, and also be funny.
 * _Name's origin:_ I was bored so I threw `halp` at my console and it said it can't. Also, it's kind of a wrapper around `halt`.
 * _Dependencies:_ Python 3, Espeak, Tty, Poweroff
* __Ttyid__ - Welcome user to the system.
 * _Dependencies:_ Python 3, Espeak, Tty, Whoami
* __Saybday__ - Read upcoming birthdays and anniversaries out loud while listing them.
 * _Dependencies:_ Python 3, Espeak, Birthday
* __Timotheus__ - Play .mid files from chosen directory.
 * _Name's origin:_ It's a pun on TiMidity++, but also that's what I call @Puzzlem00n sometimes.
 * _Dependencies:_ Python 3, TiMidity++ (or other commandline MIDI player (requires additional parameter).
* __MichiMPRIS.py__ - A library with runnable commandline interface that uses MPRIS API (MPRIS is a thing that controls music players through DBus)
 * _Dependencies:_ Python 3, running DBus daemon, DBus lib for Python 3, running libnotify server, GObject lib for Python 3, espeak (optional: for speaking)
* __MichiSpotify.py__ - A commandline Spotify interface, MichiMPRIS wrapper that uses Spotify.
 * _Dependencies:_ Python 3, MichiMPRIS, running official Spotify app
* __MichiTomahawk.py__ - A commandline Tomahawk interface, MichiMPRIS wrapper that uses Tomahawk.
 * _Dependencies:_ Python 3, MichiMPRIS, running Tomahawk app
* __Michify8080.py__ - A webapp to control Spotify from local network, runs on port 8080.
 * _Dependencies:_ Python 3, Flask (Python webapp library), MichiSpotify
 * _Warning:_ Won't work without additional files in working directory.
 * _Required additional files_: `templates` directory, `static` directory
* __SptSH__ - A curses interface for Spotify. Kinda.
 * _Dependencies:_ Python 3, MichiSpotify, curses

Special thanks
--------------
* @Folis, who added a fix that flushes console different way and counts stars different way
