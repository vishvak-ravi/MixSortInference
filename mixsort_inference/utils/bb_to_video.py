import cv2
import os
import numpy as np
import parser

def make_parser():
    

# Define a function to generate a unique color for each ID
def get_color(id):
    np.random.seed(id)
    return tuple(np.random.randint(0, 255, 3).tolist())

# Load bounding box data
bounding_boxes = np.loadtxt()

bounding_boxes = [
    "61,1,855.6,355.0,95.0,137.5,0.9700000286102295,-1,-1,-1",
    "61,2,943.6,316.2,80.5,92.6,0.9599999785423279,-1,-1,-1",
    "61,3,384.4,379.3,55.0,148.9,0.9599999785423279,-1,-1,-1",
    # Add more bounding box data here...
]

# Parse bounding box data
parsed_bboxes = []
for line in bounding_boxes:
    parts = line.strip().split(',')
    frame = int(parts[0])
    id = int(parts[1])
    bb_left = float(parts[2])
    bb_top = float(parts[3])
    bb_width = float(parts[4])
    bb_height = float(parts[5])
    parsed_bboxes.append((frame, id, bb_left, bb_top, bb_width, bb_height))

# Directory containing frames
frame_dir = "path/to/frames"

# Output video file
output_video = "output_video.avi"

# Get frame size
frame_sample = cv2.imread(os.path.join(frame_dir, "0001.jpg"))
height, width, layers = frame_sample.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video, fourcc, 20.0, (width, height))

# Process frames
frame_files = sorted([f for f in os.listdir(frame_dir) if f.endswith('.jpg')])
frame_files = [os.path.join(frame_dir, f) for f in frame_files]

# Dictionary to store bounding boxes by frame
bboxes_by_frame = {}
for bbox in parsed_bboxes:
    frame, id, bb_left, bb_top, bb_width, bb_height = bbox
    if frame not in bboxes_by_frame:
        bboxes_by_frame[frame] = []
    bboxes_by_frame[frame].append((id, bb_left, bb_top, bb_width, bb_height))

# Read each frame and draw bounding boxes
for i, frame_file in enumerate(frame_files):
    frame = cv2.imread(frame_file)
    frame_index = i + 1

    if frame_index in bboxes_by_frame:
        for bbox in bboxes_by_frame[frame_index]:
            id, bb_left, bb_top, bb_width, bb_height = bbox
            color = get_color(id)
            top_left = (int(bb_left), int(bb_top))
            bottom_right = (int(bb_left + bb_width), int(bb_top + bb_height))
            cv2.rectangle(frame, top_left, bottom_right, color, 2)
            cv2.putText(frame, str(id), (int(bb_left), int(bb_top) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    out.write(frame)

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("Video has been rendered successfully.")
