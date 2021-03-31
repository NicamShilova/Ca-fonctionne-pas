# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--game", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def game(request):
    return request.config.getoption("--game")