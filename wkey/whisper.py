import os

from dotenv import load_dotenv
import openai

load_dotenv()
WHISPER_MODEL = "whisper-1"
openai.api_key = os.environ["OPENAI_API_KEY"]


def apply_whisper(filepath: str, mode: str) -> str:

    if mode not in ("translate", "transcribe"):
        raise ValueError(f"Invalid mode: {mode}")

    prompt = "Hello, this is a properly structured message. GPT, ChatGPT."
    
    with open(filepath, "rb") as audio_file:
        if mode == "translate":
            response = openai.Audio.translate(WHISPER_MODEL, audio_file, prompt=prompt)
        elif mode == "transcribe":
            response = openai.Audio.transcribe(WHISPER_MODEL, audio_file, prompt=prompt)

    transcript = response["text"]
    return transcript

