import gradio as gr
from diffusers import StableDiffusionPipeline
import torch

# Load model
model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")


def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image


interface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your image prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="AI Image Generator",
    description="Generate images using Stable Diffusion and Gradio"
)

interface.launch();