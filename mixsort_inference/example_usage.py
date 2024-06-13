import sys
sys.path.append('mixsort_inference/utils')
from utils.full_pipeline import inference

VIDEO_FOLDER = '/mnt/opr/vishravi/player-reidentification/sample-videos/clips/'  # Replace with the path to your input folder of videos
EXPN_NAME = 'here_we_go'

inference(VIDEO_FOLDER, EXPN_NAME) # output resides in {VIDEO_FOLDER}/{EXPN_NAME}