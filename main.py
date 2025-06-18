from utils.video_utils import read_video, save_video
from trackers.tracker import Tracker
import os

def main():
    video_path = 'input_videos/15sec_input_720p.mp4'
    stub_path = 'stubs/tracks_15sec_input_720p.pkl'
    output_path = 'output_videos/output_video.avi'

    # Read video
    video_frames = read_video(video_path)

    # Initialize tracker
    tracker = Tracker('models/best.pt')

    # Get tracks (load from stub if it exists, otherwise compute and save)
    tracks = tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,
        stub_path=stub_path
    )

    # Annotate frames
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save output
    save_video(output_video_frames, output_path)

if __name__ == '__main__':
    os.makedirs("stubs", exist_ok=True)
    os.makedirs("output_videos", exist_ok=True)
    main()
