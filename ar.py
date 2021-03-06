import random

def ar(probabilities):
    """
    Perform accept/reject.
    
    Params
    ------
    probabilities: list-like
        vector of probabilities
    
    Returns
    -------
    indices: list
        list of accepted indices into original vector
    
    """
    p = probabilities/max(probabilities)
    return [i for i in range(len(p)) if random.random() < p[i]]
