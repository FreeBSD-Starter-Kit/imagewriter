import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess


class IMGWriter(Gtk.Window):

    def __init__(self):
        super().__init__()

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.vbox)

        label = Gtk.Label(label="Enter the path to the ISO image:")
        self.vbox.pack_start(label, True, True, 0)

        self.entry = Gtk.Entry()
        self.vbox.pack_start(self.entry, True, True, 0)

        button = Gtk.Button(label="Write to USB")
        button.connect("clicked", self.write_to_usb)
        self.vbox.pack_start(button, True, True, 0)

        self.connect("delete-event", Gtk.main_quit)

    def write_to_usb(self, widget):
        iso_path = self.entry.get_text()
        command = f"dd if={iso_path} of=/dev/da0 bs=1M"
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            message = "The ISO image was successfully written to the USB drive."
            message_type = Gtk.MessageType.INFO
        else:
            message = "An error occurred while writing the ISO image to the USB drive."
            message_type = Gtk.MessageType.ERROR
        with Gtk.MessageDialog(parent=self, flags=0, message_type=message_type,
                               buttons=Gtk.ButtonsType.OK, text=message) as dialog:
            dialog.run()

if __name__ == "__main__":
    window = IMGWriter()
    window.show_all()
    Gtk.main()
