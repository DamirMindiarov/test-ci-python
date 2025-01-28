from test_ci_python.my_f import func

def test_my_func():
  result = func(2, 2)
  assert result == 4
