# football_analysis

This repository contains code and resources for detecting and tracking football players using YOLOv5 and YOLOv8 models. The system supports video inference, visualization, and player classification tasks.

## Project Structure

```text
football_analysis/
├── football_training_yolo_v5.ipynb      # Training notebook for YOLOv5
├── yolov5xu.pt                          # Pretrained YOLOv5 model (optional)
├── yolov8x.pt                           # Pretrained YOLOv8 model (optional)
├── yolo_inference.py                    # Script for running YOLO inference on videos
├── models.txt                           # Instructions to download the 'models' folder
├── training.txt                         # Instructions to download the 'training' folder
├── utils/
│   ├── bbox_utils.py                    # Utility functions for bounding boxes
│   └── video_utils.py                   # Helper functions for reading and saving videos
├── datasets/
│   ├── train/                           # Training images and labels
│   ├── val/                             # Validation images and labels
│   ├── test/                            # Testing images and labels
│   └── labels.cache                     # Label cache for faster loading
Note: The actual models/ and training/ directories are not uploaded due to size limits. See models.txt and training.txt for download instructions.

```
## Setup Instructions
```text
Clone the repository:

bash
Copy
Edit
git clone https://github.com/kiki101robo/football_analysis.git
cd football_analysis
Install dependencies:

Make sure Python 3.8+ is installed.

pip install -r requirements.txt
Download required folders:

Download the models/ folder as per instructions in models.txt

Download the training/ folder as per instructions in training.txt

Place both inside the root football_analysis/ directory
```
## Running Inference
```text
To run object detection and tracking on a video using YOLO:
python yolo_inference.py

Make sure to:

Update paths inside the script for the model and video

Choose between YOLOv5 and YOLOv8 models as needed

The final annotated output video will be saved in the output_videos/ directory.

```

## Training YOLOv5
```text
To train your model on the football dataset:

Open football_training_yolo_v5.ipynb in Jupyter Notebook or Google Colab

Set the dataset path and modify training parameters as needed

Ensure your dataset is placed inside the correct folder structure
```
## Notes
```text
The utils/ folder includes:

bbox_utils.py: functions for extracting player center, foot position, and width

video_utils.py: helper functions to read and save videos

You can use either YOLOv5 or YOLOv8 by changing the model path in the scripts

The tracking system is built using Supervision and ByteTrack
```


