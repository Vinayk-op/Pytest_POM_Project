import pytest


@pytest.mark.regression
def test_regression():
    print("Regression Test")

@pytest.mark.xfail(reason="Expecting failure due to known bug")
def test_smoke():
    print("Smoke Test")

@pytest.mark.sanity
@pytest.mark.regression
def test_sanity():
    print("Sanity Test")