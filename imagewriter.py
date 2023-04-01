import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class IMGWriter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Image Writer")
        self.set_default_size(400, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        label = Gtk.Label("Enter the path to the ISO image:")
        vbox.pack_start(label, True, True, 0)

        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)

        button = Gtk.Button(label="Write to USB")
        button.connect("clicked", self.write_to_usb)
        vbox.pack_start(button, True, True, 0)

    def write_to_usb(self, widget):
        iso_path = self.entry.get_text()
        command = "dd if={} of=/dev/da0 bs=1M".format(iso_path)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "The ISO image was successfully written to the USB drive.")
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "An error occurred while writing the ISO image to the USB drive.")
        dialog.run()
        dialog.destroy()

    def on_delete_event(self, widget, event):
        Gtk.main_quit()

if __name__ == "__main__":
    window = IMGWriter()
    window.connect("delete-event", window.on_delete_event)
    window.show_all()
    Gtk.main()

