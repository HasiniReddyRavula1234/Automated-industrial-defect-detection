

from anomalib.data import MVTecAD
from anomalib.models import Patchcore
from anomalib.engine import Engine


def main():
    CATEGORY = "bottle"

    datamodule = MVTecAD(
        root="dataset",
        category=CATEGORY,
        train_batch_size=8,
        eval_batch_size=8,
        num_workers=0,
)

    model = Patchcore()

    
    engine = Engine()

    
    engine.fit(
        model=model,
        datamodule=datamodule,
    )


if __name__ == "__main__":
    main()