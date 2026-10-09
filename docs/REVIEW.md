# Recovery review — 2026-10-09

`FlyRobo` was downloaded through the signed-in Google Drive interface as part of the Colab Notebooks folder. Its original content is preserved in the downloaded archive and in a local working copy. The notebook contains 37 cells. Source and saved execution output were reviewed; embedded model-output images were not used as proof of accurate detection.

## Blocking findings in the training experiment

- `data.yaml` describes six classes but COCO128 retains its original 80-class label IDs. Saved training output reports labels outside the expected class range and ignored images/labels.
- Names 4 and 5 are changed to bus and truck without remapping actual labels. This does not produce a correct vehicle dataset.
- Both train and validation point to `images/train2017`; evaluation is contaminated by overlap.
- One saved training attempt failed because `data.yaml` was missing.
- Sample-video downloads are repeated; success of the video input was not established.
- Model checkpoints, `results.csv` and a trained project artifact were not recovered from local files or this notebook download.

The saved generated narrative mentions metrics, but it is not an independent source of truth. No historic metric is presented as verified model quality. Training was not rerun with the flawed configuration.

## Scope proven by this review

An early YOLOv8n/COCO128 experiment exists. No code for VisDrone, EPFL, autonomous flight, congestion classification or illegal-parking detection exists in this recovered source. These goals remain unverified. The small `detect.py` added during preparation verifies only that a pretrained detector can process local video; it does not validate the original training.

The package has English review documentation, dependencies, a gitignore, a sanitized notebook for inspection and a bounded inference utility. Samer confirmed team code publication permission on 2026-10-09. It is released as an early prototype with these limitations retained; a completed drone-system claim would be unsupported. Specific contributor attribution is still to be supplied.
