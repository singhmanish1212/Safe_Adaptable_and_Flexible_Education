import sys 
import os
# Takes first name and last name via command 
# line arguments and then display them 
#print("Output from Python") 
print("languageNeed:" + sys.argv[1]) 

path=sys.argv[2]
result = path.split('\\')[-1]
result1 = os.path.abspath('views/assets/video/' + result)
print("downloadedVideo:" + result1)
#print(result)
# save the script as hello.py 

video_file_name = result1
input_lang = sys.argv[1]
print('The line no 15 executed.')
import moviepy.editor as mp
#import sys
print('The line no 18 executed.')
 

# Insert Local Video File Path
try:
    clip = mp.VideoFileClip(video_file_name)
    print('The line no 24 executed.')
except:
    print('The file ' + video_file_name + ' could not be found!')

 

# Insert Local Audio File Path
try:
    clip.audio.write_audiofile(r"Audio File.wav")
    print('The line no 32 executed.')
except:
    print('The file audio could not be created!')
    #sys.exit(1)

 

#input_lang = input('Enter the language You want to convert')
print('The line no 41 executed.')
import googletrans
print('The line no 43 executed.')

 
print('The line no 46 executed.')
#print(googletrans.LANGUAGES)
lang = googletrans.LANGUAGES
print('The line no 49 executed.')

 
print('The line no 52 executed.')
# Input language query
input_lang = input_lang.lower()
#print(list(lang.keys())[list(lang.values()).index(input_lang)])
try:
    convert_lang = list(lang.keys())[list(lang.values()).index(input_lang)]
    print('The line no 57 executed.')
except:
    print('Sorry! The entered language '+input_lang+ ' is not possible to convert')

 

print('The line no 64 executed.')
import os
print('The line no 66 executed.')
from pydub import AudioSegment
print('The line no 67 executed.')
from pydub.silence import split_on_silence
print('The line no 70 executed.')
import speech_recognition as sr
print('The line no 72 executed.')
 

# initialize the recognizer
r = sr.Recognizer()
print('The line no 77 executed.')
# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    print('The line no 81 executed.')
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    print('The line no 88 executed.')
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    print('The line no 122 executed.')
    return whole_text

 
print('The line no 126 executed.')
path = "Audio File.wav"
#print("\nFull text:", get_large_audio_transcription(path))
text_audio = get_large_audio_transcription(path)
print('The line no 130 executed.')
 
print('The line no 132 executed.')
from langdetect import detect
print('The line no 134 executed.')

 

# detection of language
detect_lang = detect(text_audio)
#print(detect(text_audio))

 

# Text to diffrent language convertor
from googletrans import Translator

 

translator = Translator()

 

translated = translator.translate(text_audio, src=detect_lang, dest=convert_lang)
other_lang = translated.text
#print(translated.text)

 

# Import the required module for text
# to speech conversion
from gtts import gTTS

 

# This module is imported so that we can
# play the converted audio
import os

 

# The text that you want to convert to audio
mytext = other_lang

 

# Language in which you want to convert
language = convert_lang

 

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

 

# Saving the converted audio in a mp3 file
new_audio_file = myobj.save("converted_audio.mp3")

 

# Playing the converted file
os.system("mpg3211 converted_audio.mp3")

 


#Merging the Converted audio file and video file
video = mp.VideoFileClip(video_file_name)
outputPath = os.path.abspath('views/assets/video/' + 'output_video_file.mp4')
print('The line no 205 executed.',outputPath)
video.write_videofile(outputPath, audio="converted_audio.mp3")

 

#remove file
import os
os.remove("Audio File.wav")

 

print('The output video file is name output_video_file.mp4 in '+ input_lang+ ' language')
