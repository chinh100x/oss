def version():
    return "20.0"


def covenant_ok(balance, threshold):
    """Business rule: balance must stay at or above the covenant threshold."""
    return balance >= threshold
