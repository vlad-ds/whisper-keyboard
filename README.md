# whisper-keyboard

This Python script allows you to completement keyboard typing with voice commands. It uses OpenAI's Whisper speech-to-text model. 

The user keeps a button pressed (by default: right ctrl) and speaks. When the button is released, the user's command is transcribed to text and streamed to the cursor. You can use your voice to write anywhere. 

You will costs for Whisper API. Currently, it costs $0.36 for 1 hour of transcription.

## How to run 

Sign up for OpenAI and get your personal API key. 

Create a `.env` file in `bin/` with the following content:

```
OPENAI_API_KEY=<your key>
```

Install requirements:

```shell
pip install -r requirements.txt
```

Run the script:

```shell
python listener.py
```

## Additional requirements

I've only tested this on Ubuntu. If you want to use it on Windows or Mac, you might have to install additional libraries. 

### Ubuntu
You will need to install the portaudio library. 

```shell
sudo apt-get install portaudio19-dev 
```

## Change the recording key
The recording key is set to right ctrl by default. You can change it by changing the `RECORDING_KEY` variable in `listener.py`.

You can use use the `find_key` script to find the code of the key you want to use. Just run:

```shell
python find_key.py
```

And press the key you want to use. The code will be printed in the terminal.
