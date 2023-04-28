## Description

This bot is built to control presentation slides or your machine's screens (open tabs) using hand gestures.

<br />

## Easy Installation

Download and run the executable application from the releases page

https://github.com/theSEClub/slides-bot/releases

<br />

## Manual Installation

### Download

to install and run the bot first you have to clone or [download](https://github.com/theSEClub/slides-bot/archive/refs/heads/main.zip) the repository.

```
git clone https://github.com/theSEClub/slides-bot
cd slides-bot
```

<br />

### Initialize the environment

then we recommend initializing a virtual environment, but it's not necessary.

```
python -m venv /venv
```

then you need to activate the virtual environment, on Linux and MacOS:

```
source ./venv/bin/activate
```

on Windows:

```
./venv/Scripts/activate
```

<br />

### Install the dependencies

make sure to choose the right version of pip, in the virtual environment it's usually `pip3`

```
pip install -r requirements.txt
```

for apple silicon CPUs (M1, M2, ...) you will face an issue with `mediapipe` package, so you will need to remove it from the requirements file and install this package instead:

```
pip install mediapipe-silicon
```

<br />

### Run the bot

simply run the `main.py` file

```
python3 main.py
```

or

```
python main.py
```

<br /><br />

## Contributors

- Yasser Baghdadi [@YasserBaghdadi](https://github.com/YasserBaghdadi)
- Albaraa Hasan [@Null78](https://github.com/Null78)
- Mohammed Bisher [@Mohbisher](https://github.com/Mohbisher)
