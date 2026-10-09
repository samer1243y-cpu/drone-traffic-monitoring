# Drone Traffic Monitoring — Early Detection Prototype

An academic team project presented in **Samer Weryam's** portfolio. The recovered `FlyRobo` notebook contains an early object-detection training experiment. It does **not** establish a completed autonomous-drone traffic system.

## Recovered evidence

- Google Drive notebook: `FlyRobo`, recovered on 2026-10-09.
- Actual model in this notebook: **YOLOv8n**.
- Actual training data referenced: **COCO128**, with a problematic custom six-class configuration.
- Saved notebook outputs show a training run, missing-file errors and ignored labels. Its train and validation configuration uses the same images. Historical metrics are not accepted as generalization results.
- The notebook references sample traffic-video downloads, but saved execution does not establish successful end-to-end video inference.

VisDrone, EPFL, YOLOv8s, autonomous flight control, congestion detection and illegal-parking detection are project directions from the earlier description; they are **not implemented or demonstrated in the recovered notebook**.

## Contribution

Samer's previously described role includes coordination, solution design, task allocation and integration planning. These are reported roles, not proof that he implemented all components. Samer confirmed team permission to publish this code on 2026-10-09. Other team members' preferred attribution and specific code contributions have not yet been provided.

## Review copy

`notebooks/FlyRobo_recovered.ipynb` preserves recovered code for inspection. Outputs, execution counters, external metadata and generated assistant commentary were removed in this copy; the downloaded original remains unchanged. The archived notebook's training configuration is intentionally identified as flawed and should not be used as a benchmark.

`detect.py` is a small reproducible inference entry point added during portfolio preparation. It uses a pretrained COCO checkpoint and vehicle classes 2, 3, 5 and 7. This is a review utility, not evidence of drone deployment or a trained team checkpoint.

```bash
python -m venv .venv
# Windows: .\.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python detect.py --video path/to/authorized-video.mp4 --model path/to/yolov8n.pt --max-frames 40
```

The output is a JSON summary in `runs/detection/`. Model weights, data and footage are excluded. See [review findings](docs/REVIEW.md) and [execution metadata](docs/validation-summary.json).

## What needs to happen before stronger claims

1. Complete contributor attribution; team code publication permission has been confirmed.
2. Recover the intended drone dataset/version and any trained checkpoint.
3. Correct class IDs and labels before training. COCO labels cannot be relabeled by simply changing their names in YAML.
4. Create a genuinely separate validation/test split and report measured results.
5. Demonstrate inference on authorized drone footage.
6. Implement and independently test traffic objectives and any flight-control integration.

No project reuse license has been selected. This review package does not grant rights to datasets or third-party models. It records a recovered early experiment and its limitations, without inventing completed functionality.
