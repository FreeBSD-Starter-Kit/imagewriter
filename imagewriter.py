import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class ImageWriter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Image Writer")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        iso_label = Gtk.Label(label="Enter the path and name of the image file:")
        iso_label.set_margin_top(18)
        vbox.pack_start(iso_label, True, True, 0)

        self.iso_entry = Gtk.Entry(width_chars=50)
        vbox.pack_start(self.iso_entry, True, True, 0)

        device_label = Gtk.Label(label="Enter the device (e.g. /dev/da0):")
        device_label.set_margin_top(10)
        vbox.pack_start(device_label, True, True, 0)

        self.device_entry = Gtk.Entry(width_chars=50)
        vbox.pack_start(self.device_entry, True, True, 0)

        button = Gtk.Button(label="Write to USB")
        button.set_size_request(150, 30)
        button.set_margin_top(18) # Add top padding to the button
        button.connect("clicked", self.write_to_usb)
        button.set_margin_bottom(25) # Add bottom padding to the button
        vbox.pack_start(button, True, True, 0)

    def write_to_usb(self, widget):
        iso_path = self.entry.get_text()
        device_path = self.device_entry.get_text()
        command = f"dd if={iso_path} of={device_path} bs=1m"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            dialog = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="The image file was successfully written to the USB drive.")
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

