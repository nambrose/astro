import gi
from gi.repository import GLib, Gio
import subprocess

class WatchOut:

    def __init__(self):
        someloop = GLib.MainLoop()
        self.setup_watching()
        someloop.run()

    def setup_watching(self):
        self.watchdrives = Gio.VolumeMonitor.get()
        # event to watch (see further below, "Other options")
        self.watchdrives.connect("volume_removed", self.actonchange)

    def actonchange(self, *args):
        # command to run (see further below, "Other options")
        print("USB Disconnect")
