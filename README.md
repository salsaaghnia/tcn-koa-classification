# tcn-koa-classification
Undergraduate thesis repository: Markerless gait analysis and TCN-based classification for medical knee osteoarthritis severity

An end-to-end computer vision and deep learning pipeline to classify Knee Osteoarthritis (KOA) severity levels based on markerless 2D human pose estimation and temporal gait kinematics from video data.

---

## 📊 Dataset Attribution
This project utilizes the publicly available dataset for knee osteoarthritis analysis:
> **Kour, N., et al. (2020).** *Gait dataset for knee osteoarthritis and parkinson’s disease analysis with severity levels.* Mendeley Data.

*(Note: Raw video files are excluded from this repository due to file size constraints. Please refer to the Mendeley Data repository linked above to access the original dataset.)*

---

## 🚀 Key Features
- **Markerless Motion Capture:** Extracts lower-limb kinematic landmarks automatically using **Google MediaPipe**.
- **Robust Preprocessing Pipeline:** Implements signal cleaning, sliding window segmentation, and Z-score normalization with strict **Subject-Wise Data Splitting** to prevent data leakage.
- **Advanced Loss & Handling:** Incorporates specialized techniques such as focal loss and oversampling strategies to address natural class imbalances in medical time-series data.
- **Temporal Modeling:** Utilizes **Temporal Convolutional Networks (TCN)** with residual blocks to capture sequential gait patterns over time.

---

## 🛠️ Tech Stack
- **Language:** Python 3.11
- **Deep Learning:** TensorFlow, Keras, Focal Loss
- **Computer Vision:** OpenCV, MediaPipe
- **Data Processing:** NumPy (v1.26.4), Pandas (v2.1.4), SciPy, Scikit-Learn
- **Visualization:** Matplotlib, Seaborn

---

## 📁 Repository Structure
```text
knee-oa-tcn-classification/
├── assets/                  # System flowchart, confusion matrix, and evaluation plots
├── data/                    # Sample extracted features and data documentation
├── models/                  # Saved TCN model weights (.h5)
├── src/                     # Core python scripts (preprocessing, training, evaluation)
├── requirements.txt         # Required Python packages and dependencies
├── .gitignore               # Git ignore configuration
└── README.md                # Project documentation
```

⚙️ How to Run the Experiments
1. Clone the repository:
```text
git clone [https://github.com/salsaaghnia/tcn-koa-classification.git](https://github.com/salsaaghnia/tcn-koa-classification.git)
cd tcn-koa-classification
```
2. Install dependencies:
```text
pip install -r requirements.txt
Run the pipeline / scripts:
Navigate through the source files or notebooks to execute preprocessing, model training, and evaluation steps.
```
📌 Notes

This repository is intended for educational and portfolio purposes.
The project demonstrates the application of advanced computer vision, signal processing, and deep learning techniques to transform raw video data into robust clinical insights.

Author: Aghnia Tias Salsabila

Tools: Python | TensorFlow | MediaPipe | OpenCV | Git
