# CameraTablet

Using CameraTablet you can move mouse cursor by moving an index finger. The typical usage of the software: you work  text files (programming, writing, etc.) and do not want to move constantly your hand from keyboard to mouse and back.
Then you press hotkey to switch CameraTablet on, move the mouse cursor by index finger, emulate mouse click by other hotkey, then switch CameraTablet off.

## Needed hardware

USB-Camera

## How to use

1. Install python and external modules(see below)
2. in Config.py set hotkeys and the path to template images
3. call python main.py to call the app
4. Press the button  "Set camera properties". In the window prove that the camera films the keyboard. Calibrate the camera. Press Esc after finish
5. Press the button "Save Template s+s" to  the template image of your fingernail (the fingernail image will be used to track the position of the finger, moving the mouse). Put your finger on the keyboard so that you see it in window. Press 's', you will see  the photo of your finger in the new window. Click on the left upper part of your finger nail(small red button should appear) and then on the right lower part of the nail (a rectangle should appear). Press "s" to save the image and close the window. If everything works ok, the image will be written in the file with name TEMPLATE_FILE_FULL (defined in Config.py).
6. Press the button "Set tablet corners". In the new window click consequently on the upper left, upper right, lower right and lower left corners of your virtual tablet.
7. Press the button "Show tablet". In the new window you will see the yellow quadrangle (this is  your virtual tablet) and the position of your finger (blue rectangle). If your finger is inside the tablet region, the mouse should move in the correspondent position.  To switch on/off the tablet and emulate left/right mouse click, use hotkeys, defined in Config.py
8. To finish the software, press button "Quit" or press Esc.

## Known limitations:
- only one monitor is supported
- tested only in Windows
- no emulation of holding the mouse button down and moving the mouse to select something

## External Scripts
- Mouse: http://stackoverflow.com/users/117092/luc (author-site http://www.apidev.fr)
## External Modules
- opencv  '3.1.0' (3-clause BSD License) http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
- keyboard (0.9.12)  https://github.com/boppreh/keyboard
- TkInter (8.5)

## Python version
2.7.10

