"""
test_euclidean.py

EuclideanGCDクラスのテスト
"""

import sys
from src.euclidean import EuclideanGCD


def test_basic_gcd():
    """基本的なGCDテスト"""
    euclidean = EuclideanGCD()
    
    # 48と18の最大公約数は6
    result = euclidean.gcd(48, 18)
    assert result == 6, f"Expected 6, got {result}"
    print("✓ test_basic_gcd: 48と18のGCD = 6")


def test_gcd_with_equal_numbers():
    """同じ数のGCDテスト"""
    euclidean = EuclideanGCD()
    
    # 100と100の最大公約数は100
    result = euclidean.gcd(100, 100)
    assert result == 100, f"Expected 100, got {result}"
    print("✓ test_gcd_with_equal_numbers: 100と100のGCD = 100")


def test_gcd_with_one_dividing_other():
    """一方が他方を割り切る場合のGCDテスト"""
    euclidean = EuclideanGCD()
    
    # 100と50の最大公約数は50
    result = euclidean.gcd(100, 50)
    assert result == 50, f"Expected 50, got {result}"
    print("✓ test_gcd_with_one_dividing_other: 100と50のGCD = 50")


def test_gcd_with_coprime():
    """互いに素な数のGCDテスト"""
    euclidean = EuclideanGCD()
    
    # 17と13は互いに素（GCDは1）
    result = euclidean.gcd(17, 13)
    assert result == 1, f"Expected 1, got {result}"
    print("✓ test_gcd_with_coprime: 17と13のGCD = 1")


def test_gcd_with_zero():
    """0を含むGCDテスト"""
    euclidean = EuclideanGCD()
    
    # 42と0の最大公約数は42
    result = euclidean.gcd(42, 0)
    assert result == 42, f"Expected 42, got {result}"
    print("✓ test_gcd_with_zero: 42と0のGCD = 42")


def test_gcd_with_large_numbers():
    """大きな数のGCDテスト"""
    euclidean = EuclideanGCD()
    
    # 1071と462の最大公約数は21
    result = euclidean.gcd(1071, 462)
    assert result == 21, f"Expected 21, got {result}"
    print("✓ test_gcd_with_large_numbers: 1071と462のGCD = 21")


def test_gcd_negative_numbers():
    """負の数のエラーテスト"""
    euclidean = EuclideanGCD()
    
    try:
        euclidean.gcd(-10, 5)
        assert False, "ValueError should have been raised"
    except ValueError:
        print("✓ test_gcd_negative_numbers: 負の数でValueErrorが発生")


def run_all_tests():
    """すべてのテストを実行"""
    print("EuclideanGCDクラスのテストを実行中...\n")
    
    tests = [
        test_basic_gcd,
        test_gcd_with_equal_numbers,
        test_gcd_with_one_dividing_other,
        test_gcd_with_coprime,
        test_gcd_with_zero,
        test_gcd_with_large_numbers,
        test_gcd_negative_numbers
    ]
    
    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: 予期しないエラー: {e}")
            failed += 1
    
    print(f"\n{'=' * 50}")
    print(f"結果: {len(tests) - failed}/{len(tests)} テスト成功")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
