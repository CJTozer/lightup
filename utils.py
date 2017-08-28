def merge_dicts(defaults, overrides):
    if isinstance(defaults, dict) and isinstance(overrides, dict):
        for k,v in overrides.items():
            if k not in defaults:
                defaults[k] = v
            else:
                defaults[k] = merge_dicts(defaults[k], v)
        return defaults
    else:
        return overrides