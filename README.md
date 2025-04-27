# TechnoPlayComputeDevice

Goal
Create a tv console that plays a game when a "game card" is inserted.
the hardware will be based on raspberry pi with a camera.
the game cards, which will just be a 3d printed cartrage with a barcode stuck to them, will get inserted then the program will launch the corosponding game.
I will have all the games pre-loaded onto the system.
Games could be native, roms, or via moonlight.
The UI which will launch at startup (or a kiosk mode app) will be writen in python to try and give good hardware compadability.




Enviroment setup
Windows
- winget install Python.python.3.13
- winget install VSCodium.VSCodium
- winget install git.git


python -m pip install -U pygame --user
python -m pip install pygame-menu -U
python -m pip install opencv-python pyzbar