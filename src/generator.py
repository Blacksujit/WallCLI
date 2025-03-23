import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os
import uuid

# Load Stable Diffusion Model
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to(device)

def generate_image(prompt, resolution):
    print("⏳ Generating image, please wait...")

    # Generate image
    image = pipe(prompt).images[0]

    # Resize if needed
    image = image.resize((resolution, resolution))

    # Save Image
    filename = f"wallpapers/{uuid.uuid4()}.png"
    os.makedirs("wallpapers", exist_ok=True)
    image.save(filename)

    print(f"✅ Image saved at {filename}")