"""Test is_unextendible_product_basis."""
import numpy as np


from toqito.matrix_ops import tensor
from toqito.states import bell, basis, tile
from toqito.state_props import is_unextendible_product_basis


def test_is_unextensible_product_state_non_product_state():
    """Check if exception raised if non-product state is passed."""
    bell_states = [bell(i) for i in range(4)]
    dims = [2, 2]
    np.testing.assert_raises(ValueError, is_unextendible_product_basis, bell_states, dims)


def test_is_unextensible_product_state_wrong_size():
    """Check if exception raised if size of a vector does not match product of dims."""
    bell_states = [bell(i) for i in range(4)]
    dims = [2, 3]
    np.testing.assert_raises(ValueError, is_unextendible_product_basis, bell_states, dims)


def test_is_unextensible_product_state_small_set():
    """Check if correct answer returned when there are too few vectors."""
    ket_0 = basis(2,0)
    ket_1 = basis(2,1)
    ket_plus = (ket_0 + ket_1) / np.sqrt(2)
    ket_minus = (ket_0 - ket_1) / np.sqrt(2)
    # {|0, 1, +>, |1, +, 0>, |+, 0, 1>, |−, −, −>}
    vec_1 = tensor([ket_0, ket_1, ket_plus])
    vec_4 = tensor([ket_minus, ket_minus, ket_minus])
    vecs = [vec_1, vec_4]
    dims = [2, 2, 2]
    res = is_unextendible_product_basis(vecs, dims)
    np.testing.assert_equal(res[0], False)


def test_is_unextensible_product_state_tiles_5():
    """Check if Tiles[0, 1, 2, 3, 4] is correctly identified as UPB."""
    upb_tiles = [tile(i) for i in range(5)]
    dims = [3, 3]
    res = is_unextendible_product_basis(upb_tiles, dims)
    np.testing.assert_equal(res[0], True)


def test_is_unextensible_product_state_tiles_4():
    """Check if Tiles[0, 1, 2, 3] is correctly identified as non-UPB."""
    non_upb_tiles = [tile(i) for i in range(4)]
    dims = [3, 3]
    res = is_unextendible_product_basis(non_upb_tiles, dims)
    np.testing.assert_equal(res[0], False)


def test_is_unextensible_product_state_shifts():
    """Check if Shifts is correctly identified as UPB."""
    ket_0 = basis(2, 0)
    ket_1 = basis(2, 1)
    ket_plus = (ket_0 + ket_1) / np.sqrt(2)
    ket_minus = (ket_0 - ket_1) / np.sqrt(2)
    # {|0, 1, +>, |1, +, 0>, |+, 0, 1>, |−, −, −>}
    vec_1 = tensor([ket_0, ket_1, ket_plus])
    vec_2 = tensor([ket_1, ket_plus, ket_0])
    vec_3 = tensor([ket_plus, ket_0, ket_1])
    vec_4 = tensor([ket_minus, ket_minus, ket_minus])
    vecs = [vec_1, vec_2, vec_3, vec_4]
    dims = [2, 2, 2]
    res = is_unextendible_product_basis(vecs, dims)
    np.testing.assert_equal(res[0], True)
