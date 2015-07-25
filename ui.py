from gi.repository import Gtk

def windowStart():
    builder = Gtk.Builder()
    builder.add_from_file("interface.glade")
    mainWindow = builder.get_object("window1")
    mainWindow.show_all()
    mainWindow.connect("delete-event", Gtk.main_quit)
