def required_field(value=None):
    if value:
        return value != ''
    return False
