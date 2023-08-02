# whisper-keyboard

Video demo: https://www.youtube.com/watch?v=VnFtVR72jM4&feature=youtu.be

This tool allows you to simulate keyboard typing with voice commands on your computer. It uses OpenAI's Whisper speech-to-text model. 

Keep a button pressed (by default: right ctrl) and speak. Your voice will be recoded locally. When the button is released, your command will be transcribed via Whisper and the text will be streamed to your keyboard.

You can use your voice to write anywhere. 

You will incur costs for Whisper API. Currently, it costs $0.36 for 1 hour of transcription.

## How to run 

Sign up for OpenAI and get your personal API key. 

Create a `.env` file in `bin/` with the following content:

```
OPENAI_API_KEY=<your key>
RECORD_KEY=ctrl_r
```

Change RECORD_KEY to your preferred recording key. Note that Mac and Windows might have different key codes. You can use use the `find_key` script to find the code of the key you want to use. Just run:

```shell
python find_key.py
```

And press the key you want to use. The code will be printed in the terminal.

Next, install requirements:

```shell
pip install -r requirements.txt
```

Run the script:

```shell
python listener.py
```

## Additional requirements

Requirements differ depending on your OS.

### Ubuntu

You will need to install the portaudio library. 

```shell
sudo apt-get install portaudio19-dev 
```

### Mac
You will need to authorize your terminal to use the microphone and keyboard. Go to System Settings > Privacy and Security. Then: 
* Select Microphone and authorize your terminal.
* Select Accessibility and authorize your terminal.

Restart the terminal for the changes to take effect. 

Note that this might entail security risks.

## Security risks

This script creates a recording with your microphone and sends the audio to the Whisper API. The Whisper API response will be automatically streamed to your keyboard and executed there. This might entail security risks. Use at your own risk. 