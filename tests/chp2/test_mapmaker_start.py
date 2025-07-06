import pytest

from scripts.chp2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("delhi", 1.09, 1.08)
    assert p1.get_location() == (1.09, 1.08)


def test_expection_for_long():
    with pytest.raises(ValueError, match="Longitude must be between -180 and 180"):
        Point("delhi", 500.09, 1.08)

def test_expection_for_lat():
    with pytest.raises(ValueError, match="Latitude must be between -180 and 180"):
        Point("delhi", 1.09, 500.08)

def test_expection_for_name():
    with pytest.raises(TypeError, match="name must be a string"):
        Point(1, 1.09, 1.08)