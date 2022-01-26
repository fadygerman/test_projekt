def volume_of_pyramid(b: float, h: float) -> float:
    """
    Calculates the volume of a square pyramid.
    Uses V = 1/3 * b^2 * h.
    :param b: Length of (square) pyramid base
    :param h: Height of the pyramid
    :return: Volume of the pyramid
    """
    return 1 / 3 * b ** 2 * h


class TestVolume:
    def test_vop_1_1(self):
        assert volume_of_pyramid(1, 1) == 1 / 3

    def test_vop_1_2(self):
        assert volume_of_pyramid(1, 2) == 2 / 3

    def test_vop_2_1(self):
        assert volume_of_pyramid(2, 1) == 4 / 3

    def test_vop_2_2(self):
        assert volume_of_pyramid(2, 2) == 8 / 3
