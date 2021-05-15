import pytest
from src.engine import Atlas


@pytest.mark.parametrize(
    "platform, is_test, is_manual",
    [
        ("coinbase", True, True),
        ("coinbase", False, False),
        ("binance", True, True),
        ("binance", False, True),
        ("binance", True, True),
    ],
)
def test__atlas_str(platform, is_test, is_manual):
    atlas = Atlas(platform=platform, is_test=is_test, is_manual=is_manual)
    platform_exp = "Binance" if platform.lower() == "binance" else "Coinbase Pro"
    str_exp = (
        f"PLATFORM: {platform_exp}\nTEST MODE: {is_test}\nSKYNET MODE: {is_manual}"
    )
    assert str(atlas) == str_exp
