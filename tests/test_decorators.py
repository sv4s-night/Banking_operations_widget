from src.decorators import log


@log(filename="data/mylog.txt")
def my_function(x, y):
    return x + y


@log()
def test_successful_execution(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok\n" in captured.out


@log(filename="data/mylog.txt")
def my_function_1(x, y):
    return x / y


def test_retry_decorator(capsys):
    my_function_1(1, 0)
    captured = capsys.readouterr()
    assert captured.err != "my_function_2 error: ZeroDivisionError. Inputs: (1, 0), {}"
