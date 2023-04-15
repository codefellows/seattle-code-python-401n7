import pytest
from ten_thousand.game_logic import GameLogic
from ten_thousand.game import play


def extract_elements(lines, prefix, transform=lambda x: x):
    elements = []
    for line in lines:
        if line.startswith(prefix):
            element = line[len(prefix):].strip()
            elements.append(transform(element))
    return elements


def get_inputs(lines):
    return extract_elements(lines, "> ")


def get_mock_rolls(lines):
    return extract_elements(lines, "*** ", lambda x: tuple(int(num) for num in x if num.isnumeric()))


def compare_output_and_expected(captured_output, lines):
    captured_output = captured_output.split("\n")

    for actual_line, expected_line in zip(captured_output, lines):
        assert actual_line.strip() == expected_line.strip()


@pytest.mark.parametrize(
    "test_input",
    [
        ("tests/sims/bank_first_for_two_rounds.sim.txt"),
        ("tests/sims/bank_one_roll_then_quit.sim.txt"),
        ("tests/sims/cheat_and_fix.sim.txt"),
        ("tests/sims/hot_dice.sim.txt"),
        ("tests/sims/one_and_done.sim.txt"),
        ("tests/sims/quitter.sim.txt"),
        ("tests/sims/repeat_roller.sim.txt"),
        ("tests/sims/zilcher.sim.txt"),
    ],
)
def test_all(monkeypatch, capsys, test_input):
    with open(test_input, "r") as f:
        lines = f.readlines()
        inputs = get_inputs(lines)
        mock_rolls = get_mock_rolls(lines)

    def mock_input(prompt):
        response = inputs.pop(0)
        print(prompt, response, sep="")
        return response

    monkeypatch.setattr("builtins.input", mock_input)

    test_instance = GameLogic(mock_rolls)
    play(test_instance.mock_roller)

    captured_output = capsys.readouterr().out
    compare_output_and_expected(captured_output, lines)
