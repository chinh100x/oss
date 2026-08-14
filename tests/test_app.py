from src.app import value_within_limit, version


def test_version_is_a_nonempty_string():
    assert isinstance(version(), str)
    assert version()


def test_value_within_limit_passes_at_limit():
    assert value_within_limit(value=100, limit=100) is True


def test_value_within_limit_passes_below_limit():
    assert value_within_limit(value=50, limit=100) is True


def test_value_within_limit_fails_above_limit():
    assert value_within_limit(value=101, limit=100) is False
