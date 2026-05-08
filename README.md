# TE Connectivity AI Hub Intern Assignment
## Docker + Label Studio Object Detection Workflow

## Project Summary

This project demonstrates a complete local object-detection annotation workflow using Docker and Label Studio. The workflow was created using the BCCD blood cell dataset and focuses on annotating three object classes:

- RBC (Red Blood Cells)
- WBC (White Blood Cells)
- Platelets

The assignment includes:
- Docker-based Label Studio setup
- Object detection project configuration
- Bounding-box annotation workflow
- Annotation export generation
- Documentation and reproducibility setup

## Dataset Used

Dataset: BCCD Blood Cell Count and Detection Dataset

Sources:
- https://github.com/Shenggan/BCCD_Dataset
- https://public.roboflow.com/object-detection/bccd

10 sample images were selected from the dataset for this assignment.


## Repository Structure

```text
te-aihub-intern-assignment-yourname/
│
├── README.md
├── label_config.xml
├── docker_commands.md
├── docker-compose.yml
├── video_link.txt
├── screenshots/
├── exports/
├── samples/
└── scripts/



---

# SECTION 4 — Docker Setup

````markdown
## Docker Setup

Docker Desktop was used to run Label Studio locally.

### Verify Docker

```bash
docker --version


docker run -it -p 8080:8080 heartexlabs/label-studio:latest



---

# SECTION 5 — Project Creation Steps

```markdown
## Label Studio Project Creation

1. Created a new Label Studio project named:
   `BCCD Annotation Assignment`

2. Imported 10 selected BCCD images.

3. Configured object-detection labels:
   - RBC
   - WBC
   - Platelets

4. Annotated 6 images using bounding boxes.

5. Exported annotations in Label Studio JSON format.
```

---

# SECTION 6 — Label Configuration

````markdown
## Label Configuration

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



## Annotation Summary

- Total imported images: 10
- Total annotated images: 6
- Annotation type: Bounding boxes
- Export format: Label Studio JSON
- Bonus export: COCO format



## Export Files

Exported annotation files are located inside:

exports/

Main export:
- label_studio_export.json

Optional export:
- COCO export ZIP and extracted files


## Demo Video

Google Drive Video Link:
(PASTE YOUR DRIVE LINK HERE)



## Issues Faced and Solutions

### Issue 1: Docker WSL2 Error
Initially Docker Desktop failed because WSL2 and virtualization support were not fully configured.

Solution:
- Enabled Virtual Machine Platform
- Installed WSL2
- Updated WSL kernel
- Restarted the system



## AI Tools Used

The following AI tools were used for guidance and troubleshooting:
- ChatGPT
- Official Docker documentation
- Label Studio documentation

AI tools were used to:
- troubleshoot Docker and WSL setup,
- structure the repository,
- improve documentation,
- validate workflow setup,
- understand annotation best practices.

All final work and annotations were reviewed and understood before submission.


## Annotation Quality Strategy for 2,500 Images

If this workflow were scaled to 2,500 images with multiple business users, the following quality-control process would be implemented:

- Standardized annotation guidelines
- Training sessions for annotators
- Review and approval workflow
- Random quality audits
- Inter-annotator consistency checks
- Edge-case handling documentation
- Automated validation scripts
- Regular feedback cycles
- Sampling-based QA review

This would help maintain annotation consistency and reduce labeling errors across the dataset.


## Edge Case Handling

| Scenario | Handling Strategy |
|---|---|
| Overlapping cells | Annotated separately |
| Tiny platelets | Annotated only when clearly identifiable |
| Partial cells at image borders | Annotated only for visible region |
| Blurry or unclear objects | Skipped to avoid incorrect labels |


## Validation Script

A helper validation script was added:

scripts/validate_export.py

Purpose:
- verify export file exists,
- confirm annotations are present,
- validate exported task count.
