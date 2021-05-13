import pytest
from src.Atlas import Atlas


@pytest.mark.parametrize("platform, is_test", [
    ("coinbase", True),
    ("coinbase", False),
    ("binance", True),
    ("binance", False),
    ("binance", True),
])
def test__atlas_str(platform, is_test):
    atlas = Atlas(platform=platform, is_test=is_test)
    platform_exp = "Binance" if platform.lower() == "binance" else "Coinbase Pro"
    str_exp = f"PLATFORM: {platform_exp}\nTEST MODE: {is_test}"
    assert str(atlas) == str_exp
