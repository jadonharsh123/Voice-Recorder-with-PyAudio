from recorder import record_audio
from playback import playback
from converter import save_as_mp3, save_as_flac

# Constants
WAVE_OUTPUT_FILENAME = "output.wav"
MP3_OUTPUT_FILENAME = "output.mp3"
FLAC_OUTPUT_FILENAME = "output.flac"

# Record audio
record_audio(WAVE_OUTPUT_FILENAME, record_seconds=5)

# Playback the recorded audio
playback(WAVE_OUTPUT_FILENAME)

# Save the recording in different formats
save_as_mp3(WAVE_OUTPUT_FILENAME, MP3_OUTPUT_FILENAME)
save_as_flac(WAVE_OUTPUT_FILENAME, FLAC_OUTPUT_FILENAME)
