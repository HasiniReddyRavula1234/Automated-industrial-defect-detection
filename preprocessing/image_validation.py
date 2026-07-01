import os
from PIL import Image
import pandas as pd

# Dataset path
dataset = "../mvtec_anomaly_detection"

data = []

valid = 0
corrupted = 0

# Read all categories
for category in os.listdir(dataset):

    category_path = os.path.join(dataset, category)

    if os.path.isdir(category_path):

        # Read all folders and images
        for foldername, subfolders, filenames in os.walk(category_path):

            for file in filenames:

                if file.endswith(".png"):

                    image_path = os.path.join(foldername, file)

                    try:

                        img = Image.open(image_path)
                        img.verify()

                        data.append([image_path, "Valid"])
                        valid = valid + 1

                    except:

                        data.append([image_path, "Corrupted"])
                        corrupted = corrupted + 1

# Create DataFrame
df = pd.DataFrame(data, columns=["Image Path", "Status"])

# Create reports folder
if not os.path.exists("../reports"):
    os.makedirs("../reports")

# Save report
df.to_csv("../reports/image_validation_report.csv", index=False)

print("--------------------------------")
print("Image Validation Completed")
print("Valid Images      :", valid)
print("Corrupted Images :", corrupted)
print("--------------------------------")