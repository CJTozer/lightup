def merge_dicts(defaults, overrides):
    """Merges defaults and overrides.  overrides cannot define new keys not in defaults"""
    if isinstance(overrides, dict) and isinstance(defaults, dict):
        for k,v in defaults.iteritems():
            if k not in overrides:
                overrides[k] = v
            else:
                overrides[k] = merge_dicts(overrides[k], v)
    return overrides