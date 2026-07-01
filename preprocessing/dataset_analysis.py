import os
import pandas as pd

# Dataset path
dataset = "../mvtec_anomaly_detection"

data = []

for category in os.listdir(dataset):

    category_path = os.path.join(dataset, category)

    if os.path.isdir(category_path):

        train_count = 0
        test_count = 0
        defect_list = []

        # Train folder
        train_folder = os.path.join(category_path, "train")

        if os.path.exists(train_folder):

            for folder in os.listdir(train_folder):

                folder_path = os.path.join(train_folder, folder)

                if os.path.isdir(folder_path):

                    files = os.listdir(folder_path)

                    for file in files:

                        if file.endswith(".png"):
                            train_count = train_count + 1

        # Test folder
        test_folder = os.path.join(category_path, "test")

        if os.path.exists(test_folder):

            for folder in os.listdir(test_folder):

                folder_path = os.path.join(test_folder, folder)

                if os.path.isdir(folder_path):

                    files = os.listdir(folder_path)

                    for file in files:

                        if file.endswith(".png"):
                            test_count = test_count + 1

        # Ground Truth Folder
        gt_folder = os.path.join(category_path, "ground_truth")

        if os.path.exists(gt_folder):

            for folder in os.listdir(gt_folder):

                folder_path = os.path.join(gt_folder, folder)

                if os.path.isdir(folder_path):
                    defect_list.append(folder)

        data.append([
            category,
            train_count,
            test_count,
            len(defect_list),
            ", ".join(defect_list)
        ])

# Create dataframe
df = pd.DataFrame(data, columns=[
    "Category",
    "Train Images",
    "Test Images",
    "No. of Defect Types",
    "Defect Types"
])

print("========== Dataset Summary ==========")
print(df)

# Create reports folder
if not os.path.exists("../reports"):
    os.makedirs("../reports")

# Save csv file
df.to_csv("../reports/dataset_report.csv", index=False)

print("\nDataset report generated successfully.")
print("File saved in reports folder.")
