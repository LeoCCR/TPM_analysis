def list_csv(path):
    """Return a list of .csv file path from .csv file path or
       folder that contain many .csv file.

    Args:
        path ([string]): .csv file path or folder path
                         that contain many .csv file.

    Returns:
        [list]: A python list that contain .csv file.
    """

    from os import listdir
    from os.path import isdir, isfile, join

    if ".csv" in path and isfile(path):
        return [path]

    elif isdir(path):
        return [join(path, file) for file in listdir(path) if ".csv" in file]
