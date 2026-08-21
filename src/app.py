def version():
    return "44.0"


def value_within_limit(value, limit):
    """A generic threshold check: value must not exceed limit."""
    return value <= limit
