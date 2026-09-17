import subprocess


def run_atm(inputs):
    result = subprocess.run(
        ["python", "ATM.py"],
        input=inputs,
        text=True,
        capture_output=True
    )
    return result.stdout


def test_check_balance():
    output = run_atm("1\n4\n")

    assert "Balance: 10000" in output


def test_deposit():
    output = run_atm("2\n5000\n1\n4\n")

    assert "Amount deposited successfully." in output
    assert "Balance: 15000" in output


def test_withdraw():
    output = run_atm("3\n2000\n1\n4\n")

    assert "Please collect your cash." in output
    assert "Balance: 8000" in output


def test_insufficient_balance():
    output = run_atm("3\n20000\n4\n")

    assert "Insufficient balance." in output


def test_invalid_choice():
    output = run_atm("5\n4\n")

    assert "Invalid choice." in output