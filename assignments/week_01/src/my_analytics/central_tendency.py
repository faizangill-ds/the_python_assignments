from __future__ import annotations
def mean(*values:float) -> float:
    '''
    Returns mean value
    '''
    if not values:
        raise ValueError("mean()  requires at least one value")

    return sum(values)/len(values)



def median(data: list[float]) -> float:
    '''Returns median value

    '''
    if not data:
        raise ValueError("median() requires at least one value")

    srt = sorted(data)
    n = len(data)
    mid = n//2
    return srt[mid] if n/2 else (srt[mid - 1] + srt[mid+1])/2