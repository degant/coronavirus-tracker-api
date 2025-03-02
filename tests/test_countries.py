import pytest

from app.utils import countries


"""
Todo:
    * Test cases for capturing of stdout/stderr
"""


@pytest.mark.parametrize(
    "country_name,expected_country_code",
    [
        ("Germany", "DE"),
        ("Bolivia, Plurinational State of", "BO"),
        ("Korea, Democratic People's Republic of", "KP"),
        ("US", "US"),
        ("BlaBla", countries.default_country_code),
        ("Others", countries.default_country_code),
    ],
)
def test_countries_country_name__country_code(country_name, expected_country_code):
    assert countries.country_code(country_name) == expected_country_code
