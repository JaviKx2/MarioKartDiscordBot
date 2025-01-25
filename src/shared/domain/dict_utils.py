def dict_get(_dict, key, default=None):
    value = _dict.get(key, default)
    return default if value is None else value