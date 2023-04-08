import pytest
from dice import default_roller, play_dice


def test_exists():
    assert default_roller
    assert play_dice


def test_default_roller():
    roll = default_roller()
    assert len(roll) == 2
    assert 1 <= roll[0] <= 6
    assert 1 <= roll[1] <= 6
    assert all(1 <= num <= 6 for num in roll)


# monkeypatch will override input
# capsys will capture print
def test_play_dice_quit(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda x: "q")
    print(input(""))
    play_dice(default_roller)
    captured = capsys.readouterr()
    # print("captured is:", captured)
    assert captured.out == "Enter (r) to roll or (q) to quit\nOk bye!\n"
