# PyEarthTools Utils Package

This is the utils package which forms a part of the [PyEarthTools package](https://github.com/ACCESS-Community-Hub/PyEarthTools).



The rest of this page contains reference information for the components of the Data package. The entire data API docs can be viewed at [Data API](data_api.md)

|  Module             |       Purpose                        |   API Docs     |
|---------------------|--------------------------------------|----------------|
|  `utils.decorators` | Define parameters which are aliases (e.g 't2m' and '2t')  | - [alias_arguments](utils_api.md#pyearthtools.utils.decorators.alias_arguments)  |
|                     | Reverse a 1:1 dictionary mapping     | - [invert_dictionary_list](utils_api.md#pyearthtools.utils.decorators.invert_dictionary_list) |
| `utils.parameter`   |                                      | - [SingleParameter](data_api.md#pyearthtools.utils.parameter.SingleParameter) |
|                     |                                      | - [ListParameter](data_api.md#pyearthtools.utils.parameter.ListParameter) |
|                     |                                      | - [RangeParameter](data_api.md#pyearthtools.utils.parameter.RangeParameter) |
| `utils.context`     |                                      | - [ChangeValue](data_api.md#pyearthtools.utils.context.ChangeValue)
|                     |                                      | - [Catch](data_api.md#pyearthtools.utils.context.Catch)
|                     |                                      | - [PrintOnError](data_api.md#pyearthtools.utils.context.PrintOnError)
