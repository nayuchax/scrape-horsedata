def get_url(target: str) -> str:
    url = "https://db.netkeiba.com/horse/" + target + "/"
    return url


def get_target_pattern() -> list[str]:
    url_patterns = [
        "2020103075",
        "2020102899",
        "2020103532",
        "2020102745",
        "2020103626"
    ]
    return  url_patterns