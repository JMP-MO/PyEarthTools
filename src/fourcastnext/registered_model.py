# Copyright Commonwealth of Australia, Bureau of Meteorology 2024.
# This software is provided under license 'as is', without warranty 
# of any kind including, but not limited to, fitness for a particular 
# purpose. The user assumes the entire risk as to the use and 
# performance of the software. In no event shall the copyright holder 
# be held liable for any claim, damages or other liability arising 
# from the use of the software.

from __future__ import annotations

from typing import Any
from pathlib import Path
import logging
import math

import edit.models

import fourcastnext


CONFIG_PATH = Path(__file__, "../configs/").resolve()
LOG = logging.getLogger("edit.models.fourcastnext")

@edit.models.register('Development/FourCastNeXt', exists='ignore')
class FourCastNeXt(edit.models.BaseForecastModel):
    """
    FourCastNeXt

    Developed by NCI

    \b
    Arguments:
        lead_time (int | str | edit.data.TimeDelta): 
            Lead time to predict to. If int will be given as hours.
            Separate delta notation by -.
        interval (int):
            Data interval in hours. Defaults to 6.
        ckpt_path (str, optional):
            Override for weights path
    """

    _name = 'Development/FourCastNeXt'
    _default_config_path = CONFIG_PATH
    _times = [0]
    _download_paths = [

    ]

    def __init__(self, pipeline: str, output: str | Path, *, lead_time: int | str, ckpt_path: str | None = None, interval: int = 6, **kwargs) -> None:
        """
        Create FourCastNeXt Model

        Args:
            pipeline (str):
                Pipeline name to use
            output (str | Path):
                Output location
            lead_time (int | str | edit.data.TimeDelta, optional):
                Lead time of forecast (hours).
            interval (int):
                Data interval in hours. Defaults to 6.
            ckpt_path (str, optional):
                Override for weights path
        """
        self.lead_time = edit.models.utils.delta_conversion(lead_time, 'hour')
        if ckpt_path:
            self._redownload_each_time = True
            self._download_paths = [(ckpt_path, "weights.ckpt")]  # type: ignore

        self.interval = interval

        super().__init__(pipeline, output, **kwargs)

    def load(self, **kwargs) -> tuple[Any, dict[str, Any]]:
        """Load model

        Returns:
            (tuple[Any, dict[str, Any]]):
                Model, index kwargs
        """
        
        model_kwargs = dict(
            data_interval = (self.interval, 'hours'), 
            prediction_function = 'recurrent',
            prediction_config=dict(
                steps=math.ceil(self.lead_time // self.interval),
                verbose=True,
            ),
            **kwargs,
        )
        import edit.training

        model = fourcastnext.FourCastNext({})
        model_wrapper = edit.training.wrapper.lightning.Predict(model, self.pipeline)
        model_wrapper.load(self.assets / "weights.ckpt")
        
        wrapper = edit.training.wrapper.predict.TimeSeriesAutoRecurrent(model_wrapper, interval= f'{self.interval} hours')
        

        return wrapper, model_kwargs
