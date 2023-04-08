import pytest
from dice import default_roller, play_dice, mock_roller


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
    play_dice(default_roller)
    captured = capsys.readouterr()
    # print("captured is:", captured)
    assert captured.out == "Enter (r) to roll or (q) to quit\nOk bye!\n"


def test_play_dice_mock_roller(monkeypatch, capsys):
    rolls = [(5, 6), (6, 1)]

    # def mock_roller():
    #     """
    #     Returns 2 pre-determined 6 sided dice
    #     :return: a tuple of 2 dice
    #     """
    #     if rolls:
    #         return rolls.pop(0)
    #     else:
    #         return default_roller()

    # if there are tuples inside of rolls, then input returns r, if there isn't it returns q
    monkeypatch.setattr("builtins.input", lambda x: "q" if not rolls else "r")
    play_dice(mock_roller)
    captured = capsys.readouterr()
    print(captured)
    output_lines = captured.out.strip().split("\n")
    print(output_lines)
    assert len(output_lines) == 6
    assert output_lines[0] == "Enter (r) to roll or (q) to quit"
    assert output_lines[1] == "(5, 6)"
    assert output_lines[2] == "Enter (r) to roll or (q) to quit"
    assert output_lines[3] == "(6, 1)"
    assert output_lines[4] == "Enter (r) to roll or (q) to quit"
    assert output_lines[5] == "Ok bye!"
