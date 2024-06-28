from pydub import AudioSegment

def save_as_mp3(input_file, output_file):
    # Convert WAV to MP3
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format="mp3")

def save_as_flac(input_file, output_file):
    # Convert WAV to FLAC
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format="flac")
