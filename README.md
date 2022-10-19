## Description
this bot is built to control presentation slides using hand gestures

<br />

## Manual Installation

### Download
to install and run the bot first you have to clone or [download](https://github.com/theSEClub/slides-bot/archive/refs/heads/main.zip) the reposotory.
```
git clone https://github.com/theSEClub/slides-bot
cd slides-bot
```

<br />

### Initialize the enviroment
then we recomment initilazing a virtual enviroment, but it's not necessary.
```
python -m venv /venv
```
then you need to activate the virtual enviroment, on Linux and MacOS:
```
source ./venv/bin/activate
```
on Windows:
```
./venv/Scripts/activate
```
<br />

### Install the dependencies
make sure to choose the right version of pip, in the virtual enviroment it's usually `pip3`
```
pip install -r requirements.txt
```

for apple silicon CPUs (M1, M2, ...) you will face an issue with `mediapipe` package, so you will need to remove it from the requirements file and install this package insted
```
pip install mediapipe-silicon
```

<br />

### Run the bot
simply run the `main.py` file
```
python main.py
```

<br /><br />

## Contributers
- Yasser Baghdadi [@YasserBaghdadi](https://github.com/YasserBaghdadi)
- Albaraa Hasan [@Null78](https://github.com/Null78)