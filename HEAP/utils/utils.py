from utils.counter import Counter

def less(arr: list, a: int, b: int, counter: Counter):
    assert a > 0 and a < len(arr)
    assert b > 0 and b < len(arr)
    counter.increment_compares()
    return arr[a] < arr[b]

def exch(arr: list, a: int, b: int, counter: Counter):
    assert a > 0 and a < len(arr)
    assert b > 0 and b < len(arr)
    counter.increment_exchanges()
    arr[a], arr[b] = arr[b], arr[a]