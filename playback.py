import pyaudio
import wave

def playback(filename, chunk=1024):
    # Open the sound file
    wf = wave.open(filename, 'rb')

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

    # Read data in chunks and play it
    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Close the file
    wf.close()
