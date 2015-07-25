from gi.repository import Gtk

class Handler: #Handler for window elements
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

def windowStart(): #Creates main window, runs at startup
    builder = Gtk.Builder()
    builder.add_from_file("interface.glade")
    builder.connect_signals(Handler())

    mainWindow = builder.get_object("window1")
    mainWindow.maximize()
    mainWindow.show_all()
