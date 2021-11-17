import os

# Struct-like simplenamespace (https://dbader.org/blog/records-structs-and-data-transfer-objects-in-python)
from types import SimpleNamespace

# Configure file paths
paths = SimpleNamespace()
paths.data_dir = "data"
paths.output_dir = "out"

# convert all to absolute paths - consider the above relative to where this script lives, not where it's called from
for key, relative_path in paths.__dict__.items():
    # this would be relative to where config.py is imported from!
    # full_path = os.path.abspath(relative_path)

    # apply path relative to where config.py lives, not where it's imported from:
    dirname = os.path.dirname(__file__)
    # go one more level up
    dirname = os.path.dirname(dirname)
    paths.__dict__[key] = os.path.abspath(os.path.join(dirname, relative_path))
