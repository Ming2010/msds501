import soundfile as sf    # Use this package
import sounddevice as sd  # and this one

kiss, samplerate = sf.read('Kiss.aiff')  # load Kiss.aiff into kiss variable
kiss = kiss * .1                         # Reduce amplitude to make quieter
sd.play(kiss, samplerate)                # start playing the music
sd.wait()                                # wait until music finishes before exiting
