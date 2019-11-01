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
	    width=320,
	    height=240,
	    fps=15.,
	    verbose=True,
	    enable_audio=True) as videostream:

	frame = np.zeros((240, 320, 3))

	while True:
	    if videostream.get_video_frame_buffer_state() < 15:
	        frame = np.random.rand(240, 320, 3)
	        videostream.send_video_frame(frame)

	    if videostream.get_audio_buffer_state() < 15:
	        left_audio = np.random.randn(2940)
	        right_audio = np.random.randn(2940)
	        videostream.send_audio(left_audio, right_audio)
