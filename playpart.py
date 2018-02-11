import pyaudio
import wave


class PlayPart:
    def __init__(self, filename):
        # open wave file
        self.wav = wave.open(filename, 'rb')
        # initialize audio
        self.py_audio = pyaudio.PyAudio()
        self.stream = self.py_audio.open(format=self.py_audio.get_format_from_width(
                       self.wav.getsampwidth()),
                       channels=self.wav.getnchannels(),
                       rate=self.wav.getframerate(),
                       output=True)

    def Play(self, start, length):
        # skip unwanted frames
        n_frames = int(start * self.wav.getframerate())
        self.wav.setpos(n_frames)

        # write desired frames to audio buffer
        n_frames = int(length * self.wav.getframerate())
        frames = self.wav.readframes(n_frames)
        self.stream.write(frames)

    def Close(self):
        # close and terminate everything properly
        self.wav.close()
        self.stream.close()
        self.py_audio.terminate()

if __name__ == '__main__':
    # set desired values
    start = 2.85
    length = 3.45 - start
    pp = PlayPart('я2.wav')
    pp.Play(start, length)
    pp.Close()
