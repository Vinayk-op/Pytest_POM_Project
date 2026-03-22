"""
Two ways to parametrize test cases in pytest:
1. Using the @pytest.mark.parametrize decorator: This allows you to define multiple sets of input parameters for a test function.
    Each set of parameters will be used to run the test function separately.
    - there is two ways to use this decorator:
        a. Using a list of tuples: You can provide a list of tuples where each tuple contains multiple values corresponding to the testcase keys. Each tuple will be unpacked and passed as arguments to the test function.
        b. Only list of strings: You can provide a list of strings where each string corresponds to a single value for the testcase key. Each string will be passed as an argument to the test function.
2. Using fixtures: You can define a fixture that generates the necessary parameters for your test cases. The fixture can be used to set up any required data or state before running the test function.
                    This approach allows for more complex setup and teardown processes, as well as the ability to share common parameters across multiple test functions.
 - In the provided code snippet, the @pytest.mark.parametrize(scope="module", params=["-", "-"]) decorator is used to define multiple sets of input parameters for the test function.

"""
import pytest

@pytest.mark.parametrize("name, role", [("Vinay", "Tester"), ("Jacob", "Developer")])
def test_validate_parametrize(name, role):
    assert name != None
    assert role != None

@pytest.mark.parametrize("name", ["Vinay", "Jacob"])
def test_validate_parametrize_single(name):
    assert name != None

@pytest.fixture(scope="module", params=["google.com", "yahoo.com"])
def url(request):
    return request.param

def test_validate_url(url):
    assert url != None