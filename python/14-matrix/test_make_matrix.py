from make_matrix import matrix, matrix_direction_vector

def test_matrix_2x2():
    assert matrix(2) == [[1, 2], [4, 3]]

def test_matrix_3x3():
    assert matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

def test_matrix_4x4():
    assert matrix(4) == [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]

def test_direction_vector_matches():
    for n in [2, 3, 4, 5]:
        assert matrix(n) == matrix_direction_vector(n)
