from src.app import covenant_ok, version


def test_version_is_a_nonempty_string():
    assert isinstance(version(), str)
    assert version()


def test_covenant_ok_passes_at_threshold():
    assert covenant_ok(balance=100, threshold=100) is True


def test_covenant_ok_passes_above_threshold():
    assert covenant_ok(balance=150, threshold=100) is True


def test_covenant_ok_fails_below_threshold():
    assert covenant_ok(balance=99, threshold=100) is False
