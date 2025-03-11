import numpy as np
import pytest
from pyearthtools.utils.data.tesselator._patching.subset import cut_center, center
from pyearthtools.utils.exceptions import TesselatorException

def test_cut_center():
    x = np.zeros((10, 10))
    assert cut_center(x, 5).shape == (5, 5)
    assert cut_center(x, (6, 4)).shape == (6, 4)

def test_cut_center_square():
    x = np.zeros((10, 10))
    result = cut_center(x, 5)
    assert result.shape == (5, 5)

def test_cut_center_rectangle():
    x = np.zeros((10, 10))
    result = cut_center(x, (6, 4))
    assert result.shape == (6, 4)
