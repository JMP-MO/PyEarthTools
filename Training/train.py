import logging

import hydra
from hydra.utils import instantiate

from omegaconf import OmegaConf

from pathlib import Path


import sys

sys.path.append(str((Path(__file__).parent / "./../src").resolve()))

logger = logging.getLogger(__name__)
logging.getLogger("cfgrib").setLevel(logging.ERROR)
logging.getLogger("matplotlib").setLevel(logging.ERROR)


@hydra.main(config_path="./configs", config_name="config", version_base=None)
def train(cfg):
    print(OmegaConf.to_yaml(cfg))

    import edit.training
    import edit.pipeline

    splits = {
        "train_split": edit.pipeline.iterators.DateRange(*cfg.data.splits.train),
        "valid_split": edit.pipeline.iterators.DateRange(*cfg.data.splits.valid),
    }

    if cfg.data.splits.random:
        seed = cfg.data.splits.get("random_seed", 42)
        splits = {
            "train_split": edit.pipeline.iterators.Randomise(splits["train_split"], seed),
            "valid_split": edit.pipeline.iterators.Randomise(splits["valid_split"], None),
        }

    pipelines = None
    try:
        pipelines = OmegaConf.to_object(cfg.data.pipelines)
    except ValueError:
        pipelines = cfg.data.pipelines
        
    datamodule = edit.training.data.lightning.PipelineLightningDataModule(
        pipelines,  # type: ignore
        **splits,
        **cfg.data.module,
    )
    print(datamodule)

    # cfg.model.model_params.update(cfg.data.model_updates)
    model = instantiate(cfg.model)

    trainer = edit.training.lightning.Train(
        model,
        datamodule,
        path=cfg.path,
        **OmegaConf.to_object(cfg.trainer),  # type: ignore
    )

    if cfg.fit or input("Fit? (y/n): ").lower() == "y":
        trainer.fit()


if __name__ == "__main__":
    train()
