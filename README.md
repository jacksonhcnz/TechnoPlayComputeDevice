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

Libraries im currently testing

- python -m pip install -U pygame --user
- python -m pip install pygame-menu -U
- python -m pip install opencv-python pyzbar

What I think the game cards could look like
![Screenshot 2025-04-29 140000](https://github.com/user-attachments/assets/3bdc72e1-8232-474d-8c21-0f145ece0e2c)


What I think the applicaiton gui could look like
![01 base screen](https://github.com/user-attachments/assets/d06ecfb3-2539-4616-8d38-444df0d85c86)
![02 card inserted but not yet read](https://github.com/user-attachments/assets/e47dfbc6-29d8-45f8-9ce0-b8e7851541f8)
![03a Card has been read and game is launching (2)](https://github.com/user-attachments/assets/8798754b-98c1-4d00-8e17-0c2fad250209)
![03b Card has been read and game is launching](https://github.com/user-attachments/assets/c7ef24a7-c4f9-4384-9c05-15d6e98e20d6)
![04 console card exits the program to the console](https://github.com/user-attachments/assets/9956bdb6-5975-489e-b717-5d9f3f8094c9)
