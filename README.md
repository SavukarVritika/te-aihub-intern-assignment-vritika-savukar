# TE Connectivity AI Hub Intern Assignment

## Docker + Label Studio Object Detection Workflow

---

# Project Summary

This project demonstrates a complete local object-detection annotation workflow using Docker and Label Studio. The workflow was created using the BCCD Blood Cell Count and Detection dataset and focuses on annotating three object classes:

* RBC (Red Blood Cells)
* WBC (White Blood Cells)
* Platelets

The assignment includes:

* Docker-based Label Studio setup
* Object detection project configuration
* Bounding-box annotation workflow
* Annotation export generation
* Documentation and reproducibility setup

The final exported annotations can be used as structured training data for future computer vision and machine learning workflows.

---

# Dataset Used

Dataset: BCCD Blood Cell Count and Detection Dataset

## Sources

* https://github.com/Shenggan/BCCD_Dataset

10 sample images were selected from the dataset for this assignment.

---

# Repository Structure

```text
te-aihub-intern-assignment-vritika-savukar/
│
├── README.md
├── label_config.xml
├── docker_commands.md
├── docker-compose.yml
├── video_link.txt
│
├── screenshots/
│   ├── annotation.png
│   ├── label_studio_dashboard.png
│   ├── docker_dashboard.png
│   ├── validate_exports_json.png
│   ├── docker_running.png
│   └── github_push.png
│
├── exports/
│   ├── label_studio_export_json.json
│   ├── label_studio_export_coco.zip
│   └── label_studio_export_yolo.zip
│
├── samples/
│   ├── image_01.jpg
│   ├── image_02.jpg
│   ├── image_03.jpg
│   ├── image_04.jpg
│   ├── image_05.jpg
│   ├── image_06.jpg
│   ├── image_07.jpg
│   ├── image_08.jpg
│   ├── image_09.jpg
│   └── image_10.jpg
│
├── scripts/
│   └── validate_export.py
│
└── selected_10_images_or_download_instructions.txt
```

---

# Docker Setup

Install Docker Desktop from:

https://docs.docker.com/desktop/setup/install/windows-install/

Docker Desktop was used to run Label Studio locally.

## Verify Docker

```bash
docker --version
```

## Run Label Studio

```bash
docker run -it -p 8080:8080 heartexlabs/label-studio:latest
```

## Open Label Studio

Open in browser:

```text
http://localhost:8080
```

---

# Label Studio Project Creation

1. Created a new Label Studio project named:

   `BCCD Annotation Assignment`

2. Imported 10 selected BCCD images.

3. Configured object-detection labels:

   * RBC
   * WBC
   * Platelets

4. Annotated all 10 imported images using bounding boxes.

5. Exported annotations in Label Studio JSON format.

---

# Label Configuration

```xml
<View>
  <Image name="image" value="$image"/>

  <RectangleLabels name="label" toName="image">
    <Label value="RBC" background="red"/>
    <Label value="WBC" background="blue"/>
    <Label value="Platelets" background="green"/>
  </RectangleLabels>
</View>
```

---

# Annotation Summary

* Total imported images: 10
* Total annotated images: 10
* Annotation type: Bounding boxes
* Export format: Label Studio JSON
* Bonus export: COCO format and YOLO format

## Validation Script Output

```text
Total tasks: 10
Annotated tasks: 10

Label counts:
  RBC: 135
  Platelets: 22
  WBC: 10
```

---

# Export Files

Exported annotation files are located inside:

```text
exports/
```

## Main Export

* `label_studio_export_json.json`

## Optional Exports

* `label_studio_export_coco.zip`
* `label_studio_export_yolo.zip`

---

# Screenshots

The repository includes the following screenshots:

* `screenshots/annotation.png`
* `screenshots/label_studio_dashboard.png`
* `screenshots/docker_dashboard.png`
* `screenshots/validate_exports_json.png`
* `screenshots/docker_running.png`
* `screenshots/github_push.png`

---

# Demo Video

## Google Drive Video Link

PASTE_YOUR_GOOGLE_DRIVE_LINK_HERE

---

# Issues Faced and Solutions

## Issue 1: Docker WSL2 Error

Initially Docker Desktop failed because WSL2 and virtualization support were not fully configured.

## Solution

* Enabled Virtual Machine Platform
* Installed WSL2
* Updated WSL kernel
* Restarted the system

---

# AI Tools Used

The following AI tools and resources were used for guidance and troubleshooting:

* ChatGPT
* GitHub Copilot

## AI Tools Were Used To

1. Troubleshoot Docker and WSL setup
2. Understand the workflow
3. Improve documentation
4. Validate workflow setup
5. Understand annotation best practices

All final work and annotations were reviewed and understood before submission.

---

# Annotation Quality Strategy for 2,500 Images

If this workflow were scaled to 2,500 images with multiple business users, the following quality-control process would be implemented:

1. Clearly defined annotation guidelines with examples for RBCs, WBCs, Platelets, overlapping cells, partial objects, and unclear regions.
2. Initial onboarding and training sessions for annotators to ensure consistent labeling practices.
3. Multi-level review and approval workflows.
4. Periodic sampling-based QA checks to identify inconsistencies or annotation drift.
5. Inter-annotator consistency checks to compare labeling agreement across multiple annotators.
6. Edge-case documentation for handling overlapping cells, tiny platelets, blurry objects, and partial cells at image boundaries.
7. Automated validation scripts to verify annotation completeness, label distribution, and export integrity.
8. Continuous feedback cycles and review meetings to improve annotation quality over time.
9. Version-controlled exports and reproducible workflows for traceability and future model-training pipelines.

This would help maintain annotation consistency and reduce labeling errors across the dataset.

---

# Edge Case Handling

| Scenario                       | Handling Strategy                        |
| ------------------------------ | ---------------------------------------- |
| Overlapping cells              | Annotated separately                     |
| Tiny platelets                 | Annotated only when clearly identifiable |
| Partial cells at image borders | Annotated only for visible region        |
| Blurry or unclear objects      | Skipped to avoid incorrect labels        |

---

# Validation Script

A helper validation script was added.

## Purpose

* Verify export file exists
* Confirm annotations are present
* Validate exported task count
* Summarize label distribution

## Run Using

```bash
python validate_export.py
```

---

# Project Outcome

This project demonstrates a reproducible annotation workflow for object detection using Docker and Label Studio.

The generated annotations can be used as structured training data for future machine learning or computer vision models designed to detect and classify RBCs, WBCs, and Platelets in blood smear images.

---
