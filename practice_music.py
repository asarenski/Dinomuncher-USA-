'''
Dinomuncher USA!
Base code written by: http://people.csail.mit.edu/hubert/pyaudio/
Callback version

This file handles the music portion.
'''
import pyaudio
import wave
import time
import sys

def play_jpark():
    wf = wave.open('jpark.wav', 'rb')

    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.01)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()