import pytest
from src.decorators import log


@log(filename="data/mylog.txt")
def my_function(x, y):
    return x + y


@log()
def test_successful_execution(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok\n" in captured.out




#
# @log()
# def test_output_error(capsys):
    with pytest.raises(TypeError):
        my_function('a', 'b')
    captured = capsys.readouterr()
    assert "my_function error: TypeError. Inputs: ('a', 'b'), {}" in captured.out



#
# def test_decorator_functionality(capsys):
#     # Test successful execution
#     assert my_function(1, 2) == 3
#     captured = capsys.readouterr()
#     assert "my_function ok" in captured.out
#
#     # Test exception handling
#     with pytest.raises(TypeError):
#         my_function('a', 'b')
#     captured = capsys.readouterr()
#     assert "my_function error: TypeError. Inputs: ('a', 'b'), {}" in captured.out