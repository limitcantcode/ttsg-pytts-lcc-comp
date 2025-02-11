# PyTTS Gen Component by LCC

## What is this for?
Uses [pytts](https://pypi.org/project/pyttsx3/) to convert text to speech using classical speech-synthesis methods (like [SAPI](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms723627(v=vs.85)) for Windows or [espeak](https://github.com/espeak-ng/espeak-ng) for for Linux).

## Setup
SAPI comes with Windows OS, but if on Linux, make sure you have [espeak](https://github.com/espeak-ng/espeak-ng) installed and working on your machine.

Windows
```
conda create -n jaison-comp-ttsg-pytts python=3.12
conda activate jaison-comp-ttsg-pytts
pip install -r requirements.txt
```

Unix
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing
Assuming you are in the right virtual environment and are in the root directory:
```
python ./src/main.py --port=5000
```
If it runs, it should be fine.

## Configuration
Inside of `config.json`, adjust `voice` and `gender` (`male` or `female`) to your liking. Available voices are shown when running the command under [Testing](#testing).

## Related stuff
Project J.A.I.son: https://github.com/limitcantcode/jaison-core

Join the community Discord: https://discord.gg/Z8yyEzHsYM
