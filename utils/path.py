from pathlib import Path
import resources


def abs_path(relative_path: str):
    return str(Path(resources.__file__).parent.joinpath(relative_path).absolute())