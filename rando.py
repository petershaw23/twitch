from __future__ import print_function
from twitchstream.outputvideo import TwitchBufferedOutputStream
import argparse
import numpy as np



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--streamkey',
	                  help='twitch streamkey',
	                  required=True)
    args = parser.parse_args()

 
with TwitchBufferedOutputStream(
	    twitch_stream_key=args.streamkey,
	    width=8,
	    height=6,
	    fps=60.,
	    verbose=True,
	    enable_audio=True) as videostream:

	frame = np.zeros((6, 8, 3))
	frequency = 115
        last_phase = 0

	while True:
	    if videostream.get_video_frame_buffer_state() < 60:
	        frame = np.random.rand(1, 1, 3)
	        videostream.send_video_frame(frame)

	    #if videostream.get_audio_buffer_state() < 10:
	     #   left_audio = np.random.randn(2940)
	      #  right_audio = np.random.randn(2940)
	       # videostream.send_audio(left_audio, right_audio)
            elif videostream.get_audio_buffer_state() < 60:
                x = np.linspace(last_phase,
                                last_phase +
                                frequency*2*np.pi/videostream.fps,
                                int(44100 / videostream.fps) + 1)
                last_phase = x[-1]
                audio = np.sin(x[:-1])
                videostream.send_audio(audio, audio)
