import numpy as np

DEBUG = False

def set_debug(debug: bool):
    """
    Set debug mode

    Args:
        debug (bool): Debug mode

    Returns:
        None
    """
    global DEBUG
    DEBUG = debug

def dprint(*args, **kwargs):
    """
    Print debug messages

    Args:
        *args: Arguments to print
        **kwargs: Keyword arguments to print

    Returns:
        None
    """
    if DEBUG:
        print(*args, **kwargs)

def print_matrix(m: np.ndarray, ndigits: int = 2):
    """
    Print a matrix in a well-formatted way

    Args:
        m (numpy.ndarray): Matrix to print
        ndigits (int): Number of digits to round to

    Returns:
        None
    """
    rows, cols = m.shape
    for i in range(rows):
        for j in range(cols):
            if j != cols - 1:
                dprint(f"{np.round(m[i][j], decimals=ndigits)}, ", end="")
            else:
                dprint(f"{np.round(m[i][j], decimals=ndigits)}", end="")
        dprint()
