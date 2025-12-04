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
    
    ```mermaid
    flowchart TD
        Start([開始]) --> Input[/入力: num, decimals/]
        Input --> Format[f-stringで指定桁数に<br/>フォーマット]
        Format --> Return[/フォーマット済み文字列を返す/]
        Return --> End([終了])
    ```
    
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
    
    ```mermaid
    flowchart TD
        Start([開始]) --> Input[/入力: numbers/]
        Input --> Check{リストは空?}
        Check -->|Yes| Error[ValueErrorを発生]
        Error --> End1([終了])
        Check -->|No| Sum[合計を計算]
        Sum --> Divide[合計を要素数で除算]
        Divide --> Return[/平均値を返す/]
        Return --> End2([終了])
    ```
    
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
    
    ```mermaid
    flowchart TD
        Start([開始]) --> Input[/入力: n/]
        Input --> Check1{n < 2?}
        Check1 -->|Yes| ReturnFalse1[/False を返す/]
        ReturnFalse1 --> End1([終了])
        Check1 -->|No| Check2{n == 2?}
        Check2 -->|Yes| ReturnTrue1[/True を返す/]
        ReturnTrue1 --> End2([終了])
        Check2 -->|No| Check3{n % 2 == 0?}
        Check3 -->|Yes| ReturnFalse2[/False を返す/]
        ReturnFalse2 --> End3([終了])
        Check3 -->|No| InitLoop[i = 3]
        InitLoop --> LoopCheck{i <= √n?}
        LoopCheck -->|No| ReturnTrue2[/True を返す/]
        ReturnTrue2 --> End4([終了])
        LoopCheck -->|Yes| CheckDiv{n % i == 0?}
        CheckDiv -->|Yes| ReturnFalse3[/False を返す/]
        ReturnFalse3 --> End5([終了])
        CheckDiv -->|No| Increment[i += 2]
        Increment --> LoopCheck
    ```
    
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
