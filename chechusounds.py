import random

def pick_random_voice():
    voices = ['voices/meperdonas.mp3', 'voices/joder.mp3']
    voice = random.choice(voices)
    return voice
