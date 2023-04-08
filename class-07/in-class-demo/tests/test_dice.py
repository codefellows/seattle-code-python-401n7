import pytest
from dice import default_roller, play_dice


def test_exists():
    assert default_roller
    assert play_dice
