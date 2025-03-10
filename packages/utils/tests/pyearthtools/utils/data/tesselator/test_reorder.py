import numpy as np
import pytest
from pyearthtools.utils.data.tesselator._patching.reorder import setup_formats, reorder, move_to_end

def test_setup_formats():
    # Test with one fully defined format and one partially defined format.
    assert setup_formats('RPTCHW', 'RP...HW') == ('RPTCHW', 'RPTCHW')
    assert setup_formats('TCRPHW', 'RP...HW') == ('TCRPHW', 'RPTCHW')
    assert setup_formats('RP...HW', 'TCRPHW') == ('RPTCHW', 'TCRPHW')

    # Test with both formats fully defined.
    assert setup_formats('RPTCHW', 'RPTCHW') == ('RPTCHW', 'RPTCHW')
    assert setup_formats('TCRPHW', 'RPTCHW') == ('TCRPHW', 'RPTCHW')


    # Test with different combinations of characters in the formats.
    assert setup_formats('RP...HW', 'RPTCHW') == ('RPXYHW', 'RPXYHW')

def test_setup_formats_value_error():
    with pytest.raises(ValueError):
        # Test with both formats partially defined (should raise ValueError).
        setup_formats('RP...HW', 'RP...HW')

if __name__ == "__main__":
    pytest.main()