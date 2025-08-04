# 🌟 ResoGAN - Resolution Enhancement with Deep Learning

## 🚀 Overview

**ResoGAN** is an AI-powered application that enhances the resolution of low-quality images using a deep learning model known as a **Generative Adversarial Network (GAN)**. Built with **TensorFlow** and wrapped in an intuitive **Streamlit** interface, this tool empowers users to upscale and refine image details in real time. Whether you're dealing with blurred, pixelated, or compressed photos, ResoGAN makes it easy to restore visual clarity with a single click.

## 🔥 Features

* ✅ **Deep Learning-Powered Enhancement**
  Utilizes a trained GAN architecture to significantly enhance low-resolution images, restoring finer details and textures.

* ✅ **User-Friendly Interface**
  Simple and clean front-end built with Streamlit that allows image uploads and displays enhancements instantly.

* ✅ **Fast and Efficient Inference**
  With a pre-trained generator model, image processing is fast and does not require re-training or fine-tuning.

* ✅ **Format Flexibility**
  Supports popular image formats including **JPG**, **JPEG**, and **PNG** for seamless usage.

## 🛠️ Tech Stack

* **Python** 🐍 - Core language for development
* **TensorFlow / Keras** 🔥 - Deep learning framework for building and loading GAN models
* **NumPy** 📊 - Numerical operations and image array handling
* **Streamlit** 🎨 - Interactive web app framework for deploying ML models
* **PIL (Pillow)** 🖼️ - Image loading and manipulation

## 📂 Project Structure

```
ResoGAN/
├── generator_model.h5       # Pre-trained GAN generator model
├── gan.py                   # Streamlit script for inference and UI
├── requirements.txt         # Python dependencies and libraries
├── README.md                # Project documentation
└── assets/                  # Media directory for images, icons, etc.
```

## 💻 Installation & Usage

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/ResoGAN.git
cd ResoGAN
```

### 🔹 2. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 🔹 3. Run the Streamlit App

```bash
streamlit run gan.py
```

Then upload a low-resolution image using the UI. ResoGAN will enhance it and display the result in real time.

## 📷 Example Results

| Input (Low-Resolution)         | Output (Enhanced)                |
| ------------------------------ | -------------------------------- |
| ![Low-Res](assets/low_res.jpg) | ![High-Res](assets/high_res.jpg) |

## 📌 Future Improvements

* ✅ **Train on a Larger and More Diverse Dataset** to enhance model generalization.
* ✅ **Add Higher Resolution Support** to allow for 2x or 4x upscaling options.
* ✅ **Mobile and Web Deployment** via Flask, FastAPI, or even containerization (Docker).
* ✅ **Edge Device Compatibility** for lightweight models that can run on mobile or Raspberry Pi.

## 🤝 Contributing

Contributions are highly appreciated! Feel free to fork the repository, create a new branch, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

## 📜 License

This project is released under the **MIT License**. You are free to use, modify, and distribute it as long as the license file is included in your distribution.

---

Made with ❤️ by **Tanveer Singh** and **Sehajdeep Singh**.
