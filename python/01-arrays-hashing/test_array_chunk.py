from array_chunk import chunk, chunk_comprehension

def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

def test_chunk_comprehension_matches():
    assert chunk_comprehension([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
