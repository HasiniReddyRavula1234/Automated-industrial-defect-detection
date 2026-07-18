# 🏭 Automated Industrial Defect Detection using PatchCore

## 📌 Overview

Automated Industrial Defect Detection is an AI-based quality inspection system that identifies defective industrial products using deep learning.

Instead of manually inspecting products, this system uses the **PatchCore anomaly detection algorithm** to classify products as **Good** or **Defective**.

The project is built using the **MVTec Anomaly Detection Dataset** and the **Anomalib** framework.

---

# 🚀 Problem Statement

In manufacturing industries, manual inspection of products is:

- Time-consuming
- Expensive
- Error-prone
- Difficult to scale

This project automates defect detection using Artificial Intelligence, helping industries improve quality control and reduce inspection time.

---

# 💡 Solution

The system learns the characteristics of **normal products** during training.

During testing:

- If a test image is similar to normal images → **Good**
- If a test image is significantly different → **Defective**

PatchCore does not require a large number of defective training samples, making it suitable for real-world industrial applications.

---

# 📂 Dataset

Dataset Used:

**MVTec Anomaly Detection Dataset**

Categories include:

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

Current implementation demonstrates the complete pipeline using the **Bottle** category.

---

# 🛠 Tech Stack

## Programming Language

- Python 3.10

## Frameworks

- Anomalib
- PyTorch
- Lightning

## Libraries

- OpenCV
- Pillow
- Pandas
- NumPy

## Development Tools

- VS Code
- Git
- GitLab

---

# 📁 Project Structure

```
Automated_Industrial_Defect_Detection/
│
├── configs/
├── dataset/
│
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
│   ├── predict.py
│   └── check_prediction.py
│
├── reports/
├── results/
├── templates/
├── models/
└── README.md
```

---

# ⚙️ Workflow

```
MVTec Dataset
      │
      ▼
Dataset Validation & Analysis
      │
      ▼
PatchCore Training
      │
      ▼
Model Checkpoint (.ckpt)
      │
      ▼
Testing
      │
      ▼
Prediction
      │
      ▼
Good / Defective
```

---

# 🧠 Model

Algorithm Used:

**PatchCore**

Why PatchCore?

- State-of-the-art anomaly detection algorithm
- Learns only from normal images
- High accuracy
- Memory-efficient using Coreset Selection
- Suitable when defective samples are limited

---

# 📊 Training

Run:

```bash
python training/train.py
```

The model automatically:

- Loads the Bottle dataset
- Extracts feature embeddings
- Performs Coreset Selection
- Saves the trained checkpoint

Output:

```
results/
└── Patchcore/
    └── MVTecAD/
        └── bottle/
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

The trained model evaluates unseen test images and predicts whether they are normal or defective.

---

# 🔍 Single Image Prediction

Run:

```bash
python testing/predict.py dataset/bottle/test/good/000.png
```

Example Output

```
Image      : dataset/bottle/test/good/000.png

Prediction : Good

Score      : 0.2450
```

Another example

```bash
python testing/predict.py dataset/bottle/test/broken_large/000.png
```

Output

```
Prediction : Defective

Score      : 0.9606
```

Higher anomaly score indicates a higher probability of defect.

---

# 📈 Results

Successfully completed:

- Dataset loading
- PatchCore model training
- Model checkpoint generation
- Testing on unseen images
- Single image prediction
- Good vs Defective classification

---

# 🔮 Future Work

- Train all 15 MVTec categories
- Add heatmap visualization
- Real-time webcam inspection
- Deploy as a web application
- Industrial production line integration

---

# 👩‍💻 Team Members

| Name | Contribution |
|------|--------------|
| Ravula Hasini Reddy | PatchCore model training, testing, prediction module, Git version control |
| Mula Nikitha | Dataset preprocessing, validation, dataset preparation |
| Kotagiri Neha | Frontend development (HTML) |

---

# 📚 References

- MVTec Anomaly Detection Dataset
- Anomalib Documentation
- PyTorch Documentation
- PatchCore Research Paper

---

# 📜 License

This project was developed for academic purposes as part of a Computer Science Engineering coursework.