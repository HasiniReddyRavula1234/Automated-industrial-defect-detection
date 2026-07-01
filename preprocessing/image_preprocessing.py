import os
from PIL import Image

# Dataset folder
dataset = "../mvtec_anomaly_detection"

# Output folder
output = "../processed_dataset"

# Resize size
width = 224
height = 224

# Go through all folders
for foldername, subfolders, filenames in os.walk(dataset):

    for file in filenames:

        if file.endswith(".png"):

            image_path = os.path.join(foldername, file)

            # Open image
            img = Image.open(image_path)

            # Convert image into RGB
            img = img.convert("RGB")

            # Resize image
            img = img.resize((width, height))

            # Create same folder structure
            new_folder = foldername.replace(dataset, output)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            # Save image
            save_path = os.path.join(new_folder, file)
            img.save(save_path)

print("All images are resized and saved successfully.")