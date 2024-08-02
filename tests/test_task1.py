import cProfile
import pstats
import io
import pytest
import task11.task1 as task1
import math


def test_square_perimeter():
    assert task1.square_perimeter(2) == 8
    assert task1.square_perimeter(5) == 20


def test_square_area():
    assert task1.square_area(2) == 4
    assert task1.square_area(5) == 25


def test_rectangle_area_and_perimeter():
    assert task1.rectangle_area_and_perimeter(2, 3) == (6, 10)
    assert task1.rectangle_area_and_perimeter(4, 5) == (20, 18)


def test_circle_length():
    assert task1.circle_length(2) == pytest.approx(2 * math.pi)
    assert task1.circle_length(5) == pytest.approx(5 * math.pi)


def test_cube_volume_and_surface_area():
    assert task1.cube_volume_and_surface_area(2) == (8, 24)
    assert task1.cube_volume_and_surface_area(3) == (27, 54)


def test_rectangular_parallelepiped_volume_and_surface_area():
    assert task1.rectangular_parallelepiped_volume_and_surface_area(2, 3, 4) == (24, 52)
    assert task1.rectangular_parallelepiped_volume_and_surface_area(1, 1, 1) == (1, 6)


def test_circle_length_and_area():
    assert task1.circle_length_and_area(2) == pytest.approx((4 * math.pi, 4 * math.pi))
    assert task1.circle_length_and_area(5) == pytest.approx((10 * math.pi, 25 * math.pi))


def test_arithmetic_mean():
    assert task1.arithmetic_mean(2, 4) == 3
    assert task1.arithmetic_mean(5, 5) == 5


def test_geometric_mean():
    assert task1.geometric_mean(2, 8) == 4
    assert task1.geometric_mean(3, 12) == pytest.approx(6)


def test_sum_difference_product_quotient_of_squares():
    assert task1.sum_difference_product_quotient_of_squares(2, 4) == (6, -2, 8, 0.25)
    assert task1.sum_difference_product_quotient_of_squares(3, 6) == (9, -3, 18, 0.25)


# Run all tests
test_square_perimeter()
test_square_area()
test_rectangle_area_and_perimeter()
test_circle_length()
test_cube_volume_and_surface_area()
test_rectangular_parallelepiped_volume_and_surface_area()
test_circle_length_and_area()
test_arithmetic_mean()
test_geometric_mean()
test_sum_difference_product_quotient_of_squares()

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    pr.disable()

    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    with open("profile_results.txt", "w") as f:
        f.write(s.getvalue())
