'''
Dinomuncher USA!
Base code written by: http://people.csail.mit.edu/hubert/pyaudio/
Play version

This file handles the music portion.
'''
#!usr/bin/env python
#coding=utf-8

import pyaudio
import wave

def play_jpark():
    #define stream chunk
    chunk = 1024

    #open a wav format music
    f = wave.open(r"jpark.wav","rb")
    #instantiate PyAudio
    p = pyaudio.PyAudio()
    #open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    #read data
    data = f.readframes(chunk)
    print data

    #play stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    p.terminate()