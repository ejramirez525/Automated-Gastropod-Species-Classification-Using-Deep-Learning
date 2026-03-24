# 🐚 Marine Gastropods Dataset

![Classes](https://img.shields.io/badge/Classes-23_Species-orange)
![Raw Images](https://img.shields.io/badge/Raw_Images-636-blue)
![Augmented Images](https://img.shields.io/badge/Augmented_Images-1%2C528-success)
![Format](https://img.shields.io/badge/Format-YOLOv8_Instance_Segmentation-brightgreen)

High-definition image datasets of 23 marine gastropod species collected from the intertidal zones of Cantilan, Surigao del Sur, Philippines. Annotated with precision polygon instance segmentation for computer vision classification tasks.

## 🔗 Dataset Links

The data is available in two distinct labeling formats to support different classification levels:
* **[Gastropod Scientific Name Dataset](https://app.roboflow.com/gastropoda-mqq7h/gastropod-final-nrqi6/1)** (Mapped directly to biological taxonomy, e.g., *Angaria delphinus*)
* **[Gastropod Common Name Dataset](https://app.roboflow.com/gastropoda-mqq7h/gastropod-commonname-final-9rv5b/1)** (Mapped to local or widely accepted common names)

## 📊 Dataset Specifications

* **Hardware:** Image acquisition for both datasets was conducted using a **Raspberry Pi Camera Module v2**.
* **Resolution:** 8.05 megapixels (median aspect ratio 3280x2464).
* **Dataset Split:** 88% Training | 8% Validation | 4% Testing.
* **Preprocessing:** `Auto-Orient` was applied and resize images to `640x640`.
* **Augmentation:** Outputs per training example was multiplied by 3. `Mosaic augmentation` was applied.