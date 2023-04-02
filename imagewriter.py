import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class ImageWriter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Image Writer")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        label = Gtk.Label(label="Enter the path to the ISO image:")
        vbox.pack_start(label, True, True, 0)

        self.entry = Gtk.Entry(width_chars=50)
        vbox.pack_start(self.entry, True, True, 0)

        device_label = Gtk.Label(label="Enter the device (e.g. /dev/da0):")
        vbox.pack_start(device_label, True, True, 0)

        self.device_entry = Gtk.Entry(width_chars=50)
        vbox.pack_start(self.device_entry, True, True, 0)

        button = Gtk.Button(label="Write to USB")
        button.connect("clicked", self.write_to_usb)
        vbox.pack_start(button, True, True, 0)

    def write_to_usb(self, widget):
        iso_path = self.entry.get_text()
        device_path = self.device_entry.get_text()
        command = f"dd if={iso_path} of={device_path} bs=1m"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            dialog = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="The ISO image was successfully written to the USB drive.")
        else:
            dialog = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.ERROR, buttons=Gtk.ButtonsType.OK, text="An error occurred while writing the ISO image to the USB drive.")
        dialog.run()
        dialog.destroy()

    def on_delete_event(self, widget, event):
        Gtk.main_quit()

if __name__ == "__main__":
    window = ImageWriter()
    window.connect("delete-event", window.on_delete_event)
    window.show_all()
    Gtk.main()
