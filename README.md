# AI Image Generator using Stable Diffusion & Gradio

## Project Overview

The **AI Image Generator** is a web-based application that generates images from text prompts using **Stable Diffusion**, a powerful deep learning model for text-to-image synthesis. The application provides an interactive interface built with **Gradio**, allowing users to input a description and instantly generate AI-created images.

This project demonstrates the integration of **Generative AI, Deep Learning, and Web Interfaces** using Python.

---

## Project Demo

Below is an example of the application interface and generated output.

<img width="1927" height="1027" alt="image" src="https://github.com/user-attachments/assets/ca918022-5a22-4115-af37-f26918523a04" />


The user enters a text prompt such as **"nature"**, and the model generates a corresponding AI-generated image.

---

## Features

* Text-to-image generation using **Stable Diffusion**
* Interactive **Gradio web interface**
* Real-time AI image generation
* Simple and easy-to-use UI
* Runs locally on your system
* Supports custom prompts for creative image generation

---

## Technologies Used

* **Python**
* **Gradio**
* **Hugging Face Diffusers**
* **PyTorch**
* **Transformers**
* **Accelerate**
* **Pillow**

---

## Project Structure

```
image_generator_gradio
│
├── app.py
├── requirements.txt
├── README.md
├── assets
│   └── output.png
└── .gitignore
```

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/shivam-9s/ai-image-generator-gradio.git
```

```
cd ai-image-generator-gradio
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate the environment:

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the application by running:

```
python app.py
```

After running the command, the terminal will display:

```
Running on http://127.0.0.1:7860
```

Open this link in your browser to use the application.

---

## How It Works

1. The user enters a **text prompt** in the input box.
2. The prompt is passed to the **Stable Diffusion model**.
3. The model processes the text and generates a corresponding image.
4. The generated image is displayed in the Gradio interface.

---

## Example Prompts

You can try prompts like:

```
A futuristic city at sunset
A robot playing guitar in space
A dragon flying over a castle
A cute panda astronaut
A cyberpunk street at night
```

---

## Future Improvements

Possible enhancements for the project include:

* Multiple image generation
* Image download option
* Style selection for images
* Prompt history
* GPU acceleration for faster generation
* Cloud deployment (HuggingFace / Streamlit / Render)

---

## Author

**Shivam Kumar**

GitHub:
https://github.com/shivam-9s

---

## License

This project is open-source and available for educational and research purposes.
