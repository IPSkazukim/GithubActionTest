"""
euclidean.py

ユークリッドの互除法を実装したモジュール
"""

from src.calculator import Calculator


class EuclideanGCD:
    """
    Calculatorクラスを使用してユークリッドの互除法を実装するクラス
    
    このクラスはCalculatorの基本演算を使用して、
    2つの整数の最大公約数（GCD）を計算します。
    
    Examples:
        >>> euclidean = EuclideanGCD()
        >>> euclidean.gcd(48, 18)
        6
        >>> euclidean.gcd(100, 50)
        50
    """
    
    def __init__(self):
        """EuclideanGCDクラスのコンストラクタ"""
        self.calculator = Calculator()
    
    def gcd(self, a: int, b: int) -> int:
        """
        ユークリッドの互除法を使用して2つの整数の最大公約数を計算します
        
        このメソッドは、Calculatorクラスの基本演算を使用して
        ユークリッドの互除法を実装しています。
        アルゴリズムは以下の原理に基づいています：
        - gcd(a, b) = gcd(b, a mod b)
        - a mod b が 0 になったとき、b が最大公約数となります
        
        Args:
            a (int): 最初の整数
            b (int): 2番目の整数
        
        Returns:
            int: 2つの整数の最大公約数
        
        Raises:
            ValueError: aまたはbが負の数の場合
        
        Examples:
            >>> euclidean = EuclideanGCD()
            >>> euclidean.gcd(48, 18)
            6
            >>> euclidean.gcd(100, 50)
            50
            >>> euclidean.gcd(17, 13)
            1
        """
        # 負の数のチェック
        if a < 0 or b < 0:
            raise ValueError("負の数は使用できません")
        
        # aとbを絶対値に変換（念のため）
        a = abs(a)
        b = abs(b)
        
        # bが0の場合、aが最大公約数
        if b == 0:
            return a
        
        # ユークリッドの互除法のメインループ
        while b != 0:
            # Calculatorを使用してa mod bを計算
            # a mod b = a - (a // b) * b
            quotient = int(self.calculator.divide(a, b))
            remainder = int(self.calculator.subtract(a, self.calculator.multiply(quotient, b)))
            
            # 次のイテレーションのための値を更新
            a = b
            b = remainder
        
        return a
