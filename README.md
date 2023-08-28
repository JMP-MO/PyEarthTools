# `edit.archive`'s for National Computing Infrastructure

This package contains the `edit.Index`'s for the NCI, which consists of

| Name        | Description |
| :---        |       ----: |
| ERA5                | ECWMF ReAnalysis v5       |
| ACCESS              | Australian Community Climate and Earth-System Simulator       |
| AGCD                | Australian Gridded Climate Data        |
| BRAN                | Bluelink ReANalysis        |
| OceanMaps           | Ocean Modelling and Analysis Prediction System        |
| MODIS               | MODerate resolution Imaging Spectroradiometer       |
| Himiwari            | Himiwari 8/9 satellite data       |
| BARRA               | Bureau of meteorology Atmospheric high-resolution Regional Reanalysis for Australia       |

If installed, this package will automatically be imported when `edit.data` is if the user is on NCI.

It can also be explicitly imported if installed by,

```py
import edit_archive_NCI
```

## Usage

Once imported all archives are accesible underneath `edit.data.archive`

```python

import edit.data

edit.data.archive.BRAN

```
