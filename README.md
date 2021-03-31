# LPTHW3-Ex-45
[![Run on Repl.it](https://repl.it/badge/github/crc8109/LPTHW3-Ex-45)](https://repl.it/github/crc8109/LPTHW3-Ex-45)

This is exercise 45 from LPTHW3. It's a choose-your-own-adventure style game. I used the game I made in ex36 and switched it from function-based to OOP-based.

## Getting Started

### Prerequisites

You'll need these things to run the game:

```
Python 3.x
PlaySound
.WAV files for the game
```

### Quick Start
Go to my [repl](https://repl.it/@crc8109/LPTHW3-Ex-45). Then just hit the button up top that says Run with the forward arrow and the app will start up.

### Starting from Scratch

Clone this repo. Then set your environment set up by running the following command in your terminal:
```
pip install -r requirements.txt
```
Run ```python3 ex45.py``` to start the game

If you download this library in your global environment, this game will work just fine.

If you do it in a virtual environment, you'll get an error that there's no 'gi' module. This has to do with where gi in installed in your global environment (usually usr/lib/python3/dist-packages/gi) compared to the particular python version you're using. When you create a virtual environment, you don't get all the packages in usr/lib/python3/dist-packages/. To fix this, just type the following command in your terminal when in your virtual envronment:

```
ln -s /usr/lib/python3/dist-packages/gi /home/'your user name'/'the game files you downloaded'/'your virtual environment'/lib/python3.6/site-packages/
```

It should work after that. See these two links below if you need more help or reach out to me if you need to:
https://github.com/TaylorSMarks/playsound/issues/24

https://stackoverflow.com/questions/37526026/how-to-install-gi-module-for-anaconda-python3

## Acknowledgments

@TaylorSMarks for the PlaySound library; you're a real one
@jovalle for helping fix a bug with using PlaySound in a dir whose name has spaces in it
Zed Shaw for making LPTHW; you're 60% of why I'll get a job as an engineer one day
