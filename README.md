# HCaptchaSolver

An automated solution for solving **hCaptcha image challenges** using advanced deep learning vision models.

## 📖 Project Overview

Image-based Captcha services such as hCaptcha are widely used to protect websites from bot attacks. This project demonstrates the efficacy of vision models in successfully addressing hCaptcha challenges.  

It leverages **Florence 2**, an advanced vision foundation model capable of image captioning, object detection, and more, to process and solve standard hCaptcha image challenges. The solver achieves good accuracy across three types of challenges and has been tested on over 500 images, achieving an **F1-based success rate of 0.80**.  

The entire automated solution, including API integration and models, was deployed on **Google Colab**, using free GPU resources for accessible and efficient computation. The solver is also time-efficient, taking an average of **3 seconds per challenge**.  


## 🚀 Features

- **Automated hCaptcha Solving** using deep learning vision models  
- **Supports Multiple Challenge Types** with high accuracy  
- **Colab-Ready** for GPU-accelerated computation without dedicated hardware  
- **Time-Efficient**: ~3 seconds per challenge  
- **Extensible Architecture**: modular design for integrating new models or handlers  

## 🛠️ Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Irodavlas/HCaptchaSolver.git
   cd HCaptchaSolver


**Fine-Tuned BERT Model**

The fine-tuned BERT model can be downloaded from:  
[Google Drive Link](https://drive.google.com/drive/folders/1YJLlzqwiStLhyjTKkOwYXzma3JZWuYlL?usp=drive_link)

> **Instructions:**  
> Copy and paste the entire contents of the directory into the repository root folder as:  
> `tuned/bert-yesno-model`
