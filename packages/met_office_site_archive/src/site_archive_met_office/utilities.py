# Copyright Commonwealth of Australia, Bureau of Meteorology 2024.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities for Met Office indexes"""

from __future__ import annotations

import functools
from pathlib import Path


@functools.lru_cache()
def cached_iterdir(path: Path) -> list[Path]:
    """Run iterdir but cached"""
    return list(path.iterdir())


@functools.lru_cache()
def cached_exists(path: Path) -> bool:
    """Run exits but cached"""
    return path.exists()


def postprocess_dataset(ds: xr.Dataset) -> xr.Dataset:
    """
    Interpolate all staggered grid variables (latitude_0, longitude_0)
    onto the centered grid (latitude, longitude).
    """
    
    # Store the original dimensions sizes
    original_dims = {dim: ds[dim].size for dim in ds.dims if dim in ds.coords}
    
    # Interpolate staggered grid variables to centered grid if they exist
    for var in ds.data_vars:
        arr = ds[var]
        dims = arr.dims
        # Slicing and renaming for latitude
        if 'latitude_0' in dims and 'latitude' in ds.dims:
            arr = arr.isel(latitude_0=slice(0, ds.sizes['latitude']))
            arr = arr.rename({'latitude_0': 'latitude'})
            arr = arr.assign_coords(latitude=ds['latitude'])
        if 'grid_latitude_0' in dims and 'latitude' in ds.dims:
            arr = arr.isel(grid_latitude_0=slice(0, ds.sizes['latitude']))
            arr = arr.rename({'grid_latitude_0': 'latitude'})
            arr = arr.assign_coords(latitude=ds['latitude'])
        # Slicing and renaming for longitude
        if 'longitude_0' in dims and 'longitude' in ds.dims:
            arr = arr.isel(longitude_0=slice(0, ds.sizes['longitude']))
            arr = arr.rename({'longitude_0': 'longitude'})
            arr = arr.assign_coords(longitude=ds['longitude'])
        if 'grid_longitude_0' in dims and 'longitude' in ds.dims:
            arr = arr.isel(grid_longitude_0=slice(0, ds.sizes['longitude']))
            arr = arr.rename({'grid_longitude_0': 'longitude'})
            arr = arr.assign_coords(longitude=ds['longitude'])
        ds[var] = arr
        
        
        # if 'latitude_0' in dims:
        #     interp_kwargs['latitude_0'] = ds.latitude
        # if 'longitude_0' in dims:
        #     interp_kwargs['longitude_0'] = ds.longitude
        # if 'grid_latitude_0' in dims:
        #     interp_kwargs['grid_latitude_0'] = ds.latitude
        # if 'grid_longitude_0' in dims:
        #     interp_kwargs['grid_longitude_0'] = ds.longitude
        
        # if interp_kwargs:
        #     ds[var] = ds[var].interp(**interp_kwargs)
                
        # # Now slice to ensure the original dimensions are maintained.
        # for dim in ['latitude', 'longitude']:
        #     if dim in dims and dim in original_dims:
        #         ds[var] = ds[var].isel({dim: slice(0, original_dims[dim])})
                
    # Keep only latitude, longitude, and time as coordinates
    keep_coords = {'latitude', 'longitude', 'time'}
    coords_to_drop = [c for c in ds.coords if c not in keep_coords]
    if coords_to_drop:
        ds = ds.drop_vars(coords_to_drop)
            
    return ds
