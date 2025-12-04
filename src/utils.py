"""
utils.py

ユーティリティ関数を提供するモジュール
"""

from typing import List, Union


def format_number(num: Union[int, float], decimals: int = 2) -> str:
    """
    数値を指定された小数点以下の桁数でフォーマットします
    
    Args:
        num (Union[int, float]): フォーマットする数値
        decimals (int): 小数点以下の桁数 (デフォルト: 2)
    
    Returns:
        str: フォーマットされた数値文字列
    
    Examples:
        >>> format_number(3.14159, 2)
        '3.14'
        >>> format_number(100, 0)
        '100'
    """
    return f"{num:.{decimals}f}"


def average(numbers: List[Union[int, float]]) -> float:
    """
    数値リストの平均を計算します
    
    Args:
        numbers (List[Union[int, float]]): 数値のリスト
    
    Returns:
        float: 平均値
    
    Raises:
        ValueError: リストが空の場合
    
    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([10, 20, 30])
        20.0
    """
    if not numbers:
        raise ValueError("リストが空です")
    return sum(numbers) / len(numbers)


def is_prime(n: int) -> bool:
    """
    指定された数が素数かどうかを判定します
    
    Args:
        n (int): 判定する整数
    
    Returns:
        bool: 素数の場合True、そうでない場合False
    
    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
        >>> is_prime(2)
        True
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
