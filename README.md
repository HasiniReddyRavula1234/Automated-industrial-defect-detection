# 🏭 Automated Industrial Defect Detection using PatchCore

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.5-orange)
![Anomalib](https://img.shields.io/badge/Anomalib-2.5-green)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

# 📌 Overview

Automated Industrial Defect Detection is an AI-based quality inspection system that helps identify defective industrial products automatically.

Instead of checking every product manually, this project uses the **PatchCore anomaly detection algorithm** to determine whether a product is **Good** or **Defective**. The model is trained using the **MVTec Anomaly Detection Dataset** and implemented with the **Anomalib** framework.

The current implementation demonstrates the complete workflow for the **Bottle** category, including training, testing, and single-image prediction.

---

# 🚀 Problem Statement

In manufacturing industries, maintaining product quality is very important because even a small defect can affect the performance of the product and reduce customer satisfaction. Traditionally, products are inspected manually by workers to identify defects such as cracks, scratches, dents, contamination, or other damages.

However, manual inspection is not always reliable. It takes a lot of time, requires continuous human effort, and mistakes can happen due to fatigue or lack of consistency. As production increases, inspecting every product accurately becomes even more difficult. This can result in defective products reaching customers or good products being rejected unnecessarily.

Another challenge is that collecting a large number of defective product images for training AI models is difficult because defects occur less frequently than normal products.

The main objective of this project is to build an automated defect detection system that can identify defective products accurately by learning only from normal product images. This helps reduce manual effort, improve inspection accuracy, and makes the quality checking process faster and more efficient.

---

# 💡 Solution

To solve this problem, we developed an automated industrial defect detection system using the **PatchCore** algorithm with the **Anomalib** framework.

The model is trained using only normal images from the **MVTec Anomaly Detection Dataset**. During training, it learns the important features of defect-free products instead of memorizing specific defects. Since the model understands what a normal product looks like, it can easily recognize images that are different from the learned patterns.

For testing, an input image is passed to the trained model. The model compares its features with the normal features learned during training and generates an anomaly score. If the score is low, the product is classified as **Good**. If the score is high, it is classified as **Defective**.

In this project, we implemented the complete workflow for the **Bottle** category of the MVTec AD dataset, including training, testing, and single-image prediction. The model successfully identified both normal and defective bottle images, showing that PatchCore is an effective solution for industrial quality inspection without requiring defective images during training.

---

# 📂 Dataset

**Dataset Used:** MVTec Anomaly Detection Dataset

**Dataset Source:**

https://www.mvtec.com/company/research/datasets/mvtec-ad

The dataset contains **15 industrial object categories**:

- Bottle
- Cable
- Capsule
- Carpet
- Grid
- Hazelnut
- Leather
- Metal Nut
- Pill
- Screw
- Tile
- Toothbrush
- Transistor
- Wood
- Zipper

> **Current implementation is demonstrated using the Bottle category.**

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.10

## Frameworks

- PyTorch
- Anomalib
- Lightning

## Libraries

- NumPy
- Pandas
- Pillow
- OpenCV

## Development Tools

- VS Code
- Git
- GitLab

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd automated-industrial-defect-detection
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment (Windows):

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# 📁 Project Structure

```text
Automated_Industrial_Defect_Detection/
│
├── dataset/
├── preprocessing/
│   ├── dataset_summary.py
│   ├── image_validation.py
│   └── resize_images.py
│
├── training/
│   └── train.py
│
├── testing/
│   ├── test.py
│   └── predict.py
│
├── reports/
├── results/
├── templates/
├── screenshots/
├── README.md
└── .gitignore
```

---

# 🔄 Workflow

```text
            MVTec AD Dataset
                    │
                    ▼
      Dataset Analysis & Validation
                    │
                    ▼
         PatchCore Model Training
                    │
                    ▼
      Trained Model (model.ckpt)
                    │
                    ▼
      Testing & Single Image Prediction
                    │
                    ▼
        Good / Defective Classification
```

---

# 🧠 Model

## Algorithm Used

**PatchCore**

### Why PatchCore?

- Learns using only normal images
- Does not require defective images for training
- Uses Coreset Selection to reduce memory usage
- Generates anomaly scores for each test image
- Well suited for industrial quality inspection tasks

---

# 📊 Training

Run the following command:

```bash
python training/train.py
```

The training pipeline:

- Loads the Bottle dataset
- Extracts image features
- Performs Coreset Selection
- Trains the PatchCore model
- Saves the trained checkpoint

The trained model is stored in:

```text
results/
└── Patchcore/
    └── MVTecAD/
        └── bottle/
            └── latest/
                └── weights/
                    └── lightning/
                        └── model.ckpt
```

---

# 🧪 Testing

Run:

```bash
python testing/test.py
```

The trained model evaluates unseen images and predicts whether they are **Good** or **Defective**.

---

# 🔍 Single Image Prediction

Predict a normal image:

```bash
python testing/predict.py dataset/bottle/test/good/000.png
```

Example Output

```text
Image      : dataset/bottle/test/good/000.png

Prediction : Good

Score      : 0.2450
```

Predict a defective image:

```bash
python testing/predict.py dataset/bottle/test/broken_large/000.png
```

Example Output

```text
Image      : dataset/bottle/test/broken_large/000.png

Prediction : Defective

Score      : 0.9606
```

> A higher anomaly score indicates a higher probability that the product is defective.

---
# 📸 Sample Predictions

## Good Bottle

| Input Image | Prediction |
|-------------|------------|
| <img src="https://gitlab.com/kotagirinehakumari/automated-industrial-defect-detection/-/raw/feature/hasini-training-testing/screenshots/good_input.png" width="220" alt="Good Bottle"> | **Good** ✅<br>**Score:** 0.2450 |

---

## Defective Bottle

| Input Image | Prediction |
|-------------|------------|
| <img src="https://gitlab.com/kotagirinehakumari/automated-industrial-defect-detection/-/raw/feature/hasini-training-testing/screenshots/broken_input.png" width="220" alt="Defective Bottle"> | **Defective** ❌<br>**Score:** 0.9606 |

---

# 📈 Results

The project successfully demonstrates the complete anomaly detection workflow for the Bottle category.

The implemented system can:

- Load the MVTec AD dataset
- Train a PatchCore model using normal images
- Generate a trained model checkpoint
- Predict whether unseen images are Good or Defective
- Produce anomaly scores for individual images
- Perform single-image prediction through a simple Python script

---

# 🔮 Future Scope

Some possible improvements for this project include:

- Training models for all 15 MVTec AD categories
- Generating anomaly heatmaps for defect localization
- Developing a user-friendly web interface
- Supporting real-time camera-based inspection
- Deploying the system for industrial production environments

---

# 👥 Team Contributions

| Team Member | Contribution |
|-------------|--------------|
| **Ravula Hasini Reddy** | Implemented the PatchCore model training pipeline, testing module, single-image prediction module, model validation, Git version control, and project documentation. |
| **Kotagiri Neha** | Developed the frontend interface (HTML) and created and managed the GitLab repository. |
| **Mula Nikitha** | Implemented dataset preprocessing, image validation, dataset analysis, and preprocessing utilities. |

---

# 📚 References

- MVTec Anomaly Detection Dataset
- Anomalib Documentation
- PyTorch Documentation
- PatchCore Research Paper

---

# 📄 License

This project was developed as part of a Computer Science Engineering academic group project for learning and educational purposes.