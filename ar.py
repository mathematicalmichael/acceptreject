import random

def acceptreject(p):
    """
    Perform accept/reject.
    
    Params
    ------
    p: list-like
        vector of probabilities
    
    Returns
    -------
    indicies: list
        list of accepted indices into original vector
    
    """
    return [i for i in range(len(p)) if random.rand() < p[i]]