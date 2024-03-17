from gtts import gTTS
import os

def text_to_speech(text, language='en', file_name='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(file_name)

    # Play the generated audio file
    os.system(f'start {file_name}')  # for Windows

if __name__ == '__main__':
    input_text = input('Enter the text to convert to speech: ')
    text_to_speech(input_text)