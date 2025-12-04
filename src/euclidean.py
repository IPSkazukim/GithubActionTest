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
        """EuclideanGCDクラスのコンストラクタ
        
        ```mermaid
        flowchart TD
            Start([開始]) --> Create[Calculatorインスタンスを作成]
            Create --> End([終了])
        ```
        """
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
        
        ```mermaid
        flowchart TD
            Start([開始]) --> Input[/入力: a, b/]
            Input --> CheckNeg{a < 0 or b < 0?}
            CheckNeg -->|Yes| Error[ValueErrorを発生]
            Error --> End1([終了])
            CheckNeg -->|No| CheckZero{b == 0?}
            CheckZero -->|Yes| ReturnA[/aを返す/]
            ReturnA --> End2([終了])
            CheckZero -->|No| Loop[ループ: b != 0の間]
            Loop --> CalcQuot[quotient = a // b]
            CalcQuot --> CalcRem[remainder = a - quotient * b<br/>Calculatorを使用]
            CalcRem --> Update[a = b<br/>b = remainder]
            Update --> CheckLoop{b != 0?}
            CheckLoop -->|Yes| Loop
            CheckLoop -->|No| ReturnResult[/aを返す/]
            ReturnResult --> End3([終了])
        ```
        
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
        
        # bが0の場合、aが最大公約数
        if b == 0:
            return a
        
        # ユークリッドの互除法のメインループ
        while b != 0:
            # Calculatorを使用してa mod bを計算
            # a mod b = a - (a // b) * b
            # 整数除算のため、除算結果をintに変換してから計算
            quotient = int(a // b)
            # Calculatorを使用して剰余を計算
            remainder = int(self.calculator.subtract(a, self.calculator.multiply(quotient, b)))
            
            # 次のイテレーションのための値を更新
            a = b
            b = remainder
        
        return a
