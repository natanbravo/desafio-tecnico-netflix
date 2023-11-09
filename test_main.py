from main import solution


def test_solution():
    # TEST CASE 1
    s1 = "abcdffffffffff"
    assert solution(s1) == 'a'

    # TEST CASE 2
    s2 = "abakabac"
    assert solution(s2) == 'k'

    # TEST CASE 3
    s3 = "abbbbbggggga"
    assert solution(s3) == '_'


if __name__ == '__main__':
    import pytest
    pytest.main()
