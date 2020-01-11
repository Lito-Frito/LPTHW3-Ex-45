# LPTHW3-Ex-45

This is exercise 45 from LPTHW3. It's a choose-your-own-adventure style game. I used the game I made in ex36 and switched it from function-based to OOP-based.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for your enjoyment. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You'll need these things to run the game:

```
Python 3.x, PlaySound, .WAV files for the game (in Game Files)
```

### Installing

#### Python

Go here to get Python up and running on your machine:
https://tutorial.djangogirls.org/en/installation/#pythonanywhere\

Click on 'Install Python' for whatever your operating system is. Example:

```
Install Python: Windows
```
#### PlaySound

Go here to install PlaySound (this is a simple library that plays audio for the game):
https://pypi.org/project/playsound/

It'll tell you to run this command in your terminal:

```
pip3 install playsound
```

Or, download Game Files and then type the following command:

```
pip install -r requirements.txt
```

That will install PlaySound for you in either a global or virtual environment

If you download this library in your global environment, this game will work just fine.

If you do it in a virtual environment, you'll get an error that there's no 'gi' module. This has to do with where gi in installed in your global environment (usually usr/lib/python3/dist-packages/gi) compared to the particular python version you're using. When you create a virtual environment, you don't get all the packages in usr/lib/python3/dist-packages/. To fix this, just type the following command in your terminal when in your virtual envronment:

```
ln -s /usr/lib/python3/dist-packages/gi /home/'your user name'/'the game files you downloaded'/'your virtual environment'/lib/python3.6/site-packages/
```

It should work after that. See these two links below if you need more help or reach out to me if you need to:
https://github.com/TaylorSMarks/playsound/issues/24
https://stackoverflow.com/questions/37526026/how-to-install-gi-module-for-anaconda-python3

#### .WAV Files

All .wav files are in the Game Files folder. Download it with all of its contents so the game can run smoothly. Read on in the deployment section to get the game going.

## Deployment

When you download everything from above, open the folder 'Game Files' on your computer. Then open a terminal from that directory. Then type the following:

```
python3 ex45.py
```
And that's it! The game should run. Have fun and feel free to reach out if there's any bugs.
