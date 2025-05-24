# Pipeline API Docs

## `pipeline`

```{eval-rst}

.. autoclass:: pyearthtools.pipeline.Sampler
    :members:
.. autoclass:: pyearthtools.pipeline.Iterator
    :members:
.. autoclass:: pyearthtools.pipeline.Pipeline
    :members:
.. autoclass:: pyearthtools.pipeline.Operation
    :members:    
.. autoclass:: pyearthtools.pipeline.PipelineException
    :members:        
.. autoclass:: pyearthtools.pipeline.PipelineFilterException
    :members:        
.. autoclass:: pyearthtools.pipeline.PipelineRuntimeError
    :members:        
.. autoclass:: pyearthtools.pipeline.PipelineTypeError
    :members:
```

## `pipeline.branching`
```{eval-rst}

.. autoclass:: pyearthtools.pipeline.branching.PipelineBranchPoint
    :members:
.. autoclass:: pyearthtools.pipeline.branching.Unifier
    :members:
.. autoclass:: pyearthtools.pipeline.branching.Joiner
    :members:
.. autoclass:: pyearthtools.pipeline.branching.Spliter
    :members:
```


## `pipeline.filters`
```{eval-rst}

.. autoclass:: pyearthtools.pipeline.filters.Filter
    :members:
.. autoclass:: pyearthtools.pipeline.filters.FilterCheck
    :members:    
.. autoclass:: pyearthtools.pipeline.filters.FilterWarningContext
    :members:
.. autoclass:: pyearthtools.pipeline.filters.TypeFilter
    :members:    
```

## `pipeline.iterators`
```{eval-rst}

.. autoclass:: pyearthtools.pipeline.iterators.Iterator
    :members:
.. autoclass:: pyearthtools.pipeline.iterators.Range
    :members:    
.. autoclass:: pyearthtools.pipeline.iterators.Predefined
    :members:
.. autoclass:: pyearthtools.pipeline.iterators.File
    :members:    
.. autoclass:: pyearthtools.pipeline.iterators.DateRange
    :members:    
.. autoclass:: pyearthtools.pipeline.iterators.DateRangeLimit
    :members:    
.. autoclass:: pyearthtools.pipeline.iterators.Randomise
    :members:    
.. autoclass:: pyearthtools.pipeline.iterators.SuperIterator
    :members:    
.. autoclass:: pyearthtools.pipeline.iterators.IterateResults
    :members:                
```

## `pipeline.samplers`
```{eval-rst}

.. autoclass:: pyearthtools.pipeline.samplers.EmptyObject
    :members:
.. autoclass:: pyearthtools.pipeline.samplers.Sampler
    :members:
.. autoclass:: pyearthtools.pipeline.samplers.Default
    :members:
.. autoclass:: pyearthtools.pipeline.samplers.SuperSampler
    :members:
.. autoclass:: pyearthtools.pipeline.samplers.Random
    :members:
.. autoclass:: pyearthtools.pipeline.samplers.DropOut
    :members:
.. autoclass:: pyearthtools.pipeline.samplers.RandomDropOut
    :members:
```

## `pipeline.operations`

### `pipeline.operations.xarray`

```{eval-rst}
.. autoclass:: pyearthtools.pipeline.operations.xarray.Compute
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.Merge
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.Concatenate
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.Sort
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.Chunk
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.RecodeCalendar
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.AlignDates
    :members:    

.. autoclass:: pyearthtools.pipeline.operations.xarray.conversion.ToNumpy
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.conversion.ToDask
    :members:            

.. autoclass:: pyearthtools.pipeline.operations.xarray.filters.XarrayFilter
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.filters.DropAnyNan
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.filters.DropAllNan
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.filters.DropValue
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.filters.Shape
    :members:        

.. autoclass:: pyearthtools.pipeline.operations.xarray.reshape.Dimensions
    :members:            
.. autoclass:: pyearthtools.pipeline.operations.xarray.reshape.CoordinateFlatten
    :members:                

.. autoclass:: pyearthtools.pipeline.operations.xarray.select.SelectDataset
    :members:     
.. autoclass:: pyearthtools.pipeline.operations.xarray.select.DropDataset
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.select.SliceDataset
    :members:         

.. autoclass:: pyearthtools.pipeline.operations.xarray.split.OnVariables
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.split.OnCoordinate
    :members:        

.. autoclass:: pyearthtools.pipeline.operations.xarray.values.FillNan
    :members:        
.. autoclass:: pyearthtools.pipeline.operations.xarray.values.MaskValue
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.values.ForceNormalised
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.values.Derive
    :members:

.. autoclass:: pyearthtools.pipeline.operations.xarray.metadata.Rename
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.metadata.Encoding
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.metadata.MaintainEncoding
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.metadata.Attributes
    :members:    
.. autoclass:: pyearthtools.pipeline.operations.xarray.metadata.MaintainAttributes
    :members:

.. autoclass:: pyearthtools.pipeline.operations.xarray.normalisation.xarrayNormalisation
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.normalisation.Anomaly
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.normalisation.Deviation
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.normalisation.Division
    :members:
.. autoclass:: pyearthtools.pipeline.operations.xarray.normalisation.Evaluated
    :members:

.. autoclass:: pyearthtools.pipeline.operations.xarray.remapping.HEALPix
    :members:    
```

### `pipeline.operations.dask`

### `pipeline.operations.numpy`

### `pipeline.operations.transform`

## `pipeline.modifications`




