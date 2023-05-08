from tests.app.conftest import REAL_AO3_URL
from app.loaders import load_story

import pytest


@pytest.mark.vcr()
def test_ao3_load(
    snapshot,  # type: ignore
):
    result = load_story(REAL_AO3_URL)
    assert result
    assert snapshot("json") == result.json()