
# from main import find_probability_to_miss_graduation
import main
# TestCase1 N = 5


def test_with_n_value_5():
    actual = main.find_probability_to_miss_graduation(5)
    expected = "14/29"
    assert expected == actual


def test_with_n_value_10():
    actual = main.find_probability_to_miss_graduation(10)
    expected = "372/773"
    assert expected == actual


