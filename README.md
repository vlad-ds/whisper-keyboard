# whisper-keyboard

This tool allows you to simulate keyboard typing with voice commands on your computer. It uses OpenAI's Whisper speech-to-text model. 

Keep a button pressed (by default: right ctrl) and speak. Your voice will be recoded locally. When the button is released, your command will be transcribed to text via Whisper and the text will be streamed to your keyboard.

You can use your voice to write anywhere. 

You will incur costs for Whisper API. Currently, it costs $0.36 for 1 hour of transcription.

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

## Security risks

The Whisper API response will be automatically streamed to your keyboard and executed there. This might entail security risks. Use at your own risk. 