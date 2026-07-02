import sys

from anomalib.data import PredictDataset
from anomalib.models import Patchcore
from anomalib.engine import Engine


def predict(image_path):
    dataset = PredictDataset(path=image_path)

    model = Patchcore()

    engine = Engine()

    predictions = engine.predict(
        model=model,
        dataset=dataset,
        ckpt_path="results/Patchcore/MVTecAD/bottle/v2/weights/lightning/model.ckpt",
        return_predictions=True,
    )

    prediction = predictions[0]

    label = "Defective" if prediction.pred_label.item() else "Good"

    print(f"Image      : {image_path}")
    print(f"Prediction : {label}")
    print(f"Score      : {prediction.pred_score.item():.4f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py <image_path>")
    else:
        predict(sys.argv[1])