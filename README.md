# DMET M102 - Computer Vision

## Assignment 2

This project consists of a Python script that takes an image and applies the following operations:

- Corner Detection using:
    - Harris Corner Detector
    - Moravec Corner Detector

and saves the results of each into the `./results` folder.

## Prerequisites

- Python (>=3.10.4)
- Install Python Modules
    - matplotlib
    - numpy
    - opencv-python
    - scikit-image

Install required modules by running:
```bash
pip install -r requirements.txt
```

## How To Run
The script performs all operations on any image named `original.jpg` in the root directory. However, if you'd like to use a different image with a different name, simply change the value of `originalFileName` in line 7 of `main.py`.

```bash
python ./main.py
```