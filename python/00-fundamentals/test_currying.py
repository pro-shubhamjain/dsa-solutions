from currying import calc, FluentCalculator, closure_bug, closure_fixed
import io
import contextlib

def test_calc_curried():
    assert calc()(10)(5)(20)(2)() == 50.0

def test_fluent_calculator():
    result = FluentCalculator().add(5).sub(2).multiply(10).divided(2).get_result()
    assert result == 15.0

def test_closure_bug_prints_final_value_three_times():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        closure_bug()
    assert buf.getvalue().splitlines() == ['2', '2', '2']

def test_closure_fixed_prints_correct_sequence():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        closure_fixed()
    assert buf.getvalue().splitlines() == ['0', '1', '2']
