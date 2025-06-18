from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict(
    source="input_videos/15sec_input_720p.mp4",
    save=True,
    project="runs",  
    name="predict",                    
    exist_ok=True                    
)

print(results[0])

for box in results[0].boxes:
    print(box)
