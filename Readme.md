# 🎬 Quote Video Generator

A simple and customizable **quote video generator** that creates MP4 videos from configurable quote data.

[Watch an example video](example.mp4)

---

## 📌 Overview

This project generates a video based on a quote, author, and output configuration defined in `input.py`.

- Add or remove images from the `images/` folder
- Modify the **quote**
- Change the **author**
- Adjust **output settings**
- Run the program
- Automatically generate an **MP4 video**

The video is created by executing `main.py`.

---

## 🚀 Features

- Background shuffling
- Background audio

---

## 📂 Project Structure

```
project/
│
├── main.py          # Main script to generate the video
├── input.py         # Configure quote, author, and output settings here
├── audio.mp3        # Background audio used for final clip
├── requirements.txt # Required Python packages
├── fonts/           # Fonts folder
├── LICENSE
└── README.md
```

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎬 How to Use

### 1. Configure the Quote

Open `input.py` and modify:

- `quote`
- `author`
- all other options available.

---

### 2. Run the Generator

```bash
python main.py
```

After execution, the program will generate an **MP4 video file** in the specified output location.

---

## 📦 Requirements

All required packages are listed in:

```
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Output

- The program generates an **MP4 video**
- Output location can be configured inside `input.py`
- Video content is based on the configured quote and author

---

## 📄 License

See LICENSE file for info

---

## 👨‍💻 Author

Sajawal Hassan
Project: Quote Video Generator
