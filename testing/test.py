from anomalib.data import MVTecAD
from anomalib.models import Patchcore
from anomalib.engine import Engine


def main():
    datamodule = MVTecAD(
        root="dataset",
        category="bottle",
        train_batch_size=8,
        eval_batch_size=8,
        num_workers=0,
    )

    model = Patchcore()

    engine = Engine()

    predictions = engine.predict(
        model=model,
        datamodule=datamodule,
        ckpt_path="results/Patchcore/MVTecAD/bottle/v2/weights/lightning/model.ckpt",
        return_predictions=True,
    )

    print(predictions)


if __name__ == "__main__":
    main()