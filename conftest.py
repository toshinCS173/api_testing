import pytest
from datetime import datetime
import json
import os
# this is special configuration file used by pytest
# it allows you to define
# Fixtures that are shared across multiple test
# Hooks to custimize pytest default behaviour


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("setup: Initilizing resources")
    yield
    print("Teardown: Releasing Resources")


@pytest.fixture
def load_test_data():
    file_path = os.path.join(os.path.dirname(
        __file__), 'data', 'test_data.json')
    with open(file_path) as file:
        return json.load(file)