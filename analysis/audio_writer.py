import keyboard
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd

from reporter.ai_reporter import ai_assistant
from analysis.trenscribe_assembly import get_url, get_transcribe_id, get_text


def record_while_key_pressed(filename='output.wav', key='caps lock', samplerate=16000, channels=1):
    print(f"Удерживайте клавишу {key} для записи...")
    while True:
        keyboard.wait(key)
        print("Запись...")
        frames = []
        with sd.InputStream(samplerate=samplerate, channels=channels, dtype='int16') as stream:
            while keyboard.is_pressed(key):
                data, _ = stream.read(1024)
                frames.append(data)
        print("Сохранение...")
        audio = np.concatenate(frames, axis=0)
        wav.write(filename, samplerate, audio)
        print(f"Аудио сохранено в {filename}")
        with open(filename, 'rb') as f:
            file_url = get_url(f)
        transcribe_id = get_transcribe_id(file_url)
        result = get_text(transcribe_id)
        print("Распознано: ", result.get("text"))
        ai_report = ai_assistant(result.get("text"))
        print("AI ответ:\n",ai_report)
