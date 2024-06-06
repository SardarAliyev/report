# conftest.py

import pytest
from py.xml import html # type: ignore

def pytest_html_report_title(report):
    report.title = "Test Hesabatı"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata["Proje"] = "Test Projesi"
    config._metadata["Versiya"] = "1.0.0"

def pytest_itemcollected(item):
    docstring = item.function.__doc__
    if docstring:
        item._nodeid += ' - ' + docstring

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.pop()

@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.nodeid.split(' - ', 1)[1] if ' - ' in report.nodeid else ''))
    cells.pop()
