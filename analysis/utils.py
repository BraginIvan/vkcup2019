def _callMethod(obj, def_name, row):
    return getattr(obj, def_name)(row)

def get_methods(the_class):
    return [func for func in dir(the_class) if callable(getattr(the_class, func)) and not func.startswith("_")]


def map_methods_from_class(df, the_class, column):
    for method in get_methods(the_class):
        df[method] = df[column].map(lambda q: _callMethod(the_class, method, q))

def apply_methods_from_class(df, the_class):
    for method in get_methods(the_class):
        df[method] = df.apply(lambda row: _callMethod(the_class, method, row), axis=1)

weird_rows=[7953]
def drop_weird_rows(df):
    for wr in weird_rows:
        df.drop(wr, inplace=True)

