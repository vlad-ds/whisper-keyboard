import os

from dotenv import load_dotenv
import sounddevice as sd
import numpy as np
import openai
from pynput.keyboard import Controller as KeyboardController, Key, Listener
from scipy.io import wavfile

from oa import apply_whisper
from process import process_transcript

load_dotenv()
key_label = os.environ.get("RECORD_KEY", "ctrl_r")
RECORD_KEY = Key[key_label]

# This flag determines when to record
recording = False

# This is where we'll store the audio
audio_data = []

# This is the sample rate for the audio
sample_rate = 16000

# Keyboard controller
keyboard_controller = KeyboardController()

def on_press(key):
    global recording
    global audio_data
    # When the right shift key is pressed, start recording
    if key == RECORD_KEY:
        recording = True
        audio_data = []
        print("Recording started...")

def on_release(key):
    global recording
    global audio_data
    # When the right shift key is released, stop recording
    if key == RECORD_KEY:
        recording = False
        print("Recording stopped.")
        
        try:
            audio_data_np = np.concatenate(audio_data, axis=0)
        except ValueError as e:
            print(e)
        
        audio_data_int16 = (audio_data_np * np.iinfo(np.int16).max).astype(np.int16)
        wavfile.write('recording.wav', sample_rate, audio_data_int16)

        transcript = None
        try:
            transcript = apply_whisper('recording.wav', 'transcribe')
        except openai.error.InvalidRequestError as e:
            print(e)
        
        if transcript:
            processed_transcript = process_transcript(transcript)
            print(processed_transcript)
            keyboard_controller.type(processed_transcript)


def callback(indata, frames, time, status):
    if status:
        print(status)
    if recording:
        audio_data.append(indata.copy())  # make sure to copy the indata


with Listener(on_press=on_press, on_release=on_release) as listener:
    # This is the stream callback
    with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
        # Just keep the script running
        listener.join()
