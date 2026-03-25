<div align="center">
  <img src="assets/gastropod.png" alt="banner" width="150" height="150">
</div>

<h1 align="center">Automated Gastropod Species Classification Using Deep Learning</h1>

<div align="center">

[![YOLOv8](https://img.shields.io/badge/YOLOv8-Instance_Segmentation-blue?logo=ultralytics)](https://docs.ultralytics.com/tasks/segment/)
[![Colab Training Notebook 1](https://img.shields.io/badge/Colab-Training_Notebook_1-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1OQhemZ8wla1PHqW3nBOknM4h3jFe_mjc)
[![Colab Training Notebook 2](https://img.shields.io/badge/Colab-Training_Notebook_2-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1kerUUC8y-leDWJzGKsLozcYbfyAshahd)
[![Roboflow](https://img.shields.io/badge/Roboflow-Dataset-6706CE?logo=roboflow&logoColor=white)](https://universe.roboflow.com/gastropoda-qaadk/gastropod-final/dataset/2)

</div>

## 📖 Project Overview

<div align="justify">

This project automates the taxonomic classification of marine gastropods using deep learning. Powered by the [Ultralytics YOLO algorithm](https://docs.ultralytics.com/models/yolov8/), the system performs real-time video classification and instance segmentation to identify 23 distinct species accurately. To enable real-world inferencing, the model is deployed as an Edge AI solution on a Raspberry Pi 4 Model B equipped with a Raspberry Pi Camera Module v2.
</div>


## ✨ Key Features

<div align="justify">

* Integrates a Deep Learning model designed for gastropod classification and instance segmentation.
* Fully optimized for edge deployment on a Raspberry Pi 4 Model B with a Raspberry Pi Camera Module v2.
* Performs live, on-device inferencing for immediate specimen identification without the need for cloud computing.
* Achieves highly robust spatial accuracy, achieving an overall mAP@50-95 of 92%–94%.
</div>


## 🚀 Deployment Guide

<div align="justify">

This guide outlines step-by-step procedures for setting up the YOLOv8-based gastropod classification environment. The system is designed for Edge AI deployment on a Raspberry Pi 4 Model B.
</div>

1. System Requirements
* **Hardware**
    * Raspberry Pi 4 Model B (4GB or 8GB recommended)
    * MicroSD (32GB+)
    * Camera Module (for live detection)
* **Operating System**
    * Raspberry Pi OS (64-bit)
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
2. Install System Dependencies
    ```bash
    sudo apt update
    sudo apt install -y \
    python3-venv python3-pip git \
    libatlas-base-dev libjpeg-dev zlib1g-dev \
    libopenblas-dev libblas-dev liblapack-dev \
    gfortran
    ```
3. Clone the Repository.
    ```bash
    git clone https://github.com/ejramirez525/automated-gastropod-species-classification-using-deep-learning.git
    cd automated-gastropod-species-classification-using-deep-learning
    ```
4. Create Virtual Environment.
    ```bash
    python3 -m venv yolov8-env
    source yolov8-env/bin/activate
    pip install --upgrade pip
    ```
5. Project Files Needed.
    * Make sure you have:
    ```
    ScientificName.pt
    Gastropod_Classification.py
    ```
    * Example structure:
    ```
    models\ScientificName.pt
    Gastropod_Classification.py
    requirements.txt
    ```
6. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```
7. Pi Camera Setup.
    * Enable camera interface:
    ```
    sudo raspi-config
    ```
    * Go to: `Interface Options` → `Camera` → `Enable`
    * Install camera library:
    ```bash
    pip install picamera2
    ```
8. Running the Application.
    ```bash
    python Gastropod_Classification.py
    ```
<br>

## 🏆 Research Output

<div align="center">

**Best in Thesis 🏅**<br>
**Department of Computer Studies Research Exhibit 2024**

<br>

<img src="assets/thesis-tarpaulin.png" alt="Research Tarpaulin" width="800">

<p align="center">
<i>Official Research Tarpaulin presented at the Department of Computer Studies, NEMSU Cantilan Research Exhibit.</i>
</p>

</div>

---