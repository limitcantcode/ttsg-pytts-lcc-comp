'''
Class implementing TTS generation using old-school speech synthesis.
This may require espeak for Linux. Voices available will differ between OS,
and available voices for your OS can be found using get_available_voices
'''

import pyttsx3
import logging
import os
import wave

class OldTTSModel():
    TEMP_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),'temp','output.wav')
    def __init__(self, voice_name, gender):
        self.engine = pyttsx3.init()
        
        voices = self.engine.getProperty('voices')
        logging.debug("Available voices are: {}".format(list(map(lambda x: x.id, voices))))

        self.engine.setProperty('voice', voice_name)
        self.engine.setProperty('gender', gender)


    def __call__(self, content: str):
        logging.debug(f"Generating speech from text: {content}.")
        self.engine.save_to_file(content, self.TEMP_FILE)
        self.engine.runAndWait()
        with wave.open(self.TEMP_FILE, 'r') as f:
            return f.readframes(f.getnframes()), f.getframerate(), f.getsampwidth(), f.getnchannels()
