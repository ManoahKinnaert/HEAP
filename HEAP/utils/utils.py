def less(arr: list, a: int, b: int):
    assert a > 0 and a < len(arr)
    assert b > 0 and b < len(arr)
    return arr[a] < arr[b]

def exch(arr: list, a: int, b: int):
    assert a > 0 and a < len(arr)
    assert b > 0 and b < len(arr)
    arr[a], arr[b] = arr[b], arr[a]