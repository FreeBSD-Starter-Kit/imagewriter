# Image Writer

A simple GUI utility for writing an ISO or IMG file to a USB drive.

### Dependencies
* FreeBSD or FreeBSD-based OS
* Python 3.9 or later
* Gtk 3.0 or later
* Git

### Setup
```
git clone https://github.com/FreeBSD-Starter-Kit/imagewriter
cd imagewriter
chmod o+x imagewrite.py
```

### Usage

```
python ./imagewriter.py
```

Here is an image of the initial screen.

![Initial screen](images/ImageWriter-1.png)

- Enter the path and name of the ISO or IMG file.
- Enter the USB device name.
- Select "Write to USB."

![Enter path to ISO image](images/ImageWriter-2.png)

Once completed, the following message will appear.

![Successfully written](images/ImageWriter-3.png)
