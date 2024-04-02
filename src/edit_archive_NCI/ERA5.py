# Copyright Commonwealth of Australia, Bureau of Meteorology 2024.
# This software is provided under license 'as is', without warranty 
# of any kind including, but not limited to, fitness for a particular 
# purpose. The user assumes the entire risk as to the use and 
# performance of the software. In no event shall the copyright holder 
# be held liable for any claim, damages or other liability arising 
# from the use of the software.

"""
ECWMF ReAnalysis v5
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal


from edit.data import EDITDatetime, transform
from edit.data.exceptions import DataNotFoundError
from edit.data.indexes import ArchiveIndex, decorators
from edit.data.transform import Transform, TransformCollection
from edit.data.archive import register_archive

from edit_archive_NCI.utilities import check_project
from edit_archive_NCI.ancilliary.ERA5 import ERA5_SINGLE_VARIABLES, ERA5_PRESSURE_VARIABLES

ERA_PROD = ["monthly-averaged", "monthly-averaged-by-hour", "reanalysis"]
ERA_RES_RESOLUTION = [(1, "month"), (1, "month"), (1, "hour")]

ERA5_RENAME = {"t2m": "2t", "u10": "10u", "v10": "10v"}


@register_archive("ERA5", sample_kwargs=dict(variable = '2t'))
class ERA5(ArchiveIndex):
    """ECWMF ReAnalysis v5"""

    @property
    def _desc_(self):
        return {
            "singleline": "ECWMF ReAnalysis v5",
            "range": "1970-current",
            "Documentation": "https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation",
        }

    @decorators.alias_arguments(
        level_value=["pressure"],
        variable=["variables"],
        product=["resolution"],
    )
    @decorators.check_arguments(
        struc="edit_archive_NCI.structure.ERA5.struc",
    )
    @decorators.deprecated_arguments(
        level="`level` is deprecated in the ERA5 index. Simply provide the variables, `level` will be autofound."
    )
    def __init__(
        self,
        variable: list[str] | str,
        *,
        product: Literal["monthly-averaged", "monthly-averaged-by-hour", "reanalysis"] = "reanalysis",
        level_value: int | float | list[int | float] | tuple[list | int, ...] | None = None,
        transforms: Transform | TransformCollection = TransformCollection(),
    ):
        """
        Setup ERA5 Indexer

        Args:
            variables (list[str] | str):
                Data variables to retrieve
            resolution (Literal[ERA_RES], optional):
                Resolution of data, must be one of 'monthly-averaged','monthly-averaged-by-hour', 'reanalysis'.
                Defaults to 'reanalysis'.
            level_value: (int, optional):
                Level value to select if data contains levels. Defaults to None.
            transforms (Transform | TransformCollection, optional):
                Base Transforms to apply.
                Defaults to TransformCollection().
        """
        self.make_catalog()
        check_project(project_code="rt52")

        variables = [variable] if isinstance(variable, str) else variable

        self.resolution = product

        self.variables = variables
        base_transform = TransformCollection()

        base_transform += transform.variables.rename_variables(ERA5_RENAME)
        # base_transform += transform.variables.variable_trim(variables)

        self.level_value = level_value

        if level_value:
            base_transform += transform.coordinates.select(
                {coord: level_value for coord in ["level"]}, ignore_missing=True
            )

        super().__init__(
            transforms=base_transform + transforms,
            data_interval=ERA_RES_RESOLUTION[ERA_PROD.index(product)],
        )

    def filesystem(
        self,
        querytime: str | EDITDatetime,
    ) -> Path | dict[str, str | Path]:
        ERA5_HOME = self.ROOT_DIRECTORIES["ERA5"]

        paths = {}
        querytime = EDITDatetime(querytime)

        for variable in self.variables:
            if variable in ERA5_SINGLE_VARIABLES:
                level = "single"
            elif variable in ERA5_PRESSURE_VARIABLES:
                level = "pressure"
            else:
                raise ValueError(f"Cannot identify level type of variable: {variable!r}.")

            var_path = Path(ERA5_HOME.format(level=level, resolution=self.resolution)) / variable / str(querytime.year)

            files_in_dir = var_path.iterdir()
            start_of_month_string = querytime.replace(day=1).strftime("%Y%m%d")

            relevant_path = None
            for filename in files_in_dir:
                if start_of_month_string in str(filename):
                    relevant_path = filename

            if relevant_path is not None:
                relevant_path = var_path / relevant_path

                if relevant_path.exists():
                    paths[variable] = relevant_path
                    continue

            raise DataNotFoundError(
                f"Unable to find data for: basetime: {querytime}, variables: {variable} at {var_path}"
            )
        return paths
