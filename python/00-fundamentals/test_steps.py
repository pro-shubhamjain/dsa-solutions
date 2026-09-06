from steps import steps, steps_rtl, steps_ltr, down_to_top
import io
import contextlib

def captured_lines(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*args)
    return buf.getvalue().splitlines()

def test_steps():
    assert captured_lines(steps, 3) == ['#  ', '## ', '###']

def test_steps_rtl():
    assert captured_lines(steps_rtl, 3) == ['  #', ' ##', '###']

def test_steps_ltr():
    assert captured_lines(steps_ltr, 3) == ['#', '##', '###']

def test_down_to_top():
    assert captured_lines(down_to_top, 3) == ['###', '##', '#']
