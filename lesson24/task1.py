# Add type annotation for previous function
@TypeDecorators.to_int
def make_int(string: str):
    return string


@TypeDecorators.to_bool
def make_bool(string: str):
    return string


@TypeDecorators.to_float
def make_float(string: str):
    return string


@TypeDecorators.to_str
def make_str(string: int | float | bool):
    return string