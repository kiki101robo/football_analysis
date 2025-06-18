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
