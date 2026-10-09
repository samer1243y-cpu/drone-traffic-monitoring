"""Review-only pretrained vehicle detection; no drone control or custom training."""
import argparse,json,math
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description='Run a bounded headless pretrained vehicle detection check.')
    p.add_argument('--video',type=Path,required=True)
    p.add_argument('--model',default='yolov8n.pt')
    p.add_argument('--max-frames',type=int,default=40)
    p.add_argument('--output',type=Path,default=Path('runs/detection'))
    a=p.parse_args()
    if not a.video.is_file():p.error('Input video does not exist')
    if a.max_frames<=0:p.error('--max-frames must be positive')
    import cv2
    from ultralytics import YOLO
    cap=cv2.VideoCapture(str(a.video))
    if not cap.isOpened():p.error('Cannot decode input video')
    model=YOLO(a.model);frames=0;boxes=0
    try:
        while frames<a.max_frames:
            ok,frame=cap.read()
            if not ok:break
            result=model.predict(frame,classes=[2,3,5,7],conf=.25,verbose=False)[0]
            frames+=1;boxes+=len(result.boxes)
    finally:cap.release()
    result={'frames_processed':frames,'detected_box_observations':boxes,'model':Path(a.model).name,'checkpoint_type':'pretrained COCO, not recovered project training checkpoint','drone_footage_verified':False,'flight_control_implemented':False,'evaluation':'Execution smoke test only; no ground-truth detection accuracy measurement.'}
    a.output.mkdir(parents=True,exist_ok=True)
    (a.output/'summary.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
