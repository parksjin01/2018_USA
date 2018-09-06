def to_byte(size, unit):
    if unit == "KB" or unit == "KiB":
        return size * 1024
    elif unit == "MB" or unit == "MiB":
        return size * 1024 * 1024
    elif unit == "GB" or unit == "GiB":
        return size * 1024 * 1024 * 1024
    return 0

def from_byte(size, unit):
    if unit == "KB" or unit == "KiB":
        return size / 1024.0
    elif unit == "MB" or unit == "MiB":
        return size / 1024.0 / 1024
    elif unit == "GB" or unit == "GiB":
        return size / 1024.0 / 1024 / 1024
    return 0

print from_byte(131072, "KB")
