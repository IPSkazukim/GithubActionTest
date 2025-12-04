"""
calculator.py

基本的な計算機能を提供するモジュール
"""


class Calculator:
    """
    シンプルな計算機クラス
    
    このクラスは基本的な算術演算を実行します。
    
    Examples:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.multiply(4, 5)
        20
    """
    
    def __init__(self):
        """Calculatorクラスのコンストラクタ"""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """
        2つの数値を加算します
        
        Args:
            a (float): 最初の数値
            b (float): 2番目の数値
        
        Returns:
            float: 加算結果
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(10, 20)
            30.0
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        aからbを減算します
        
        Args:
            a (float): 減算される数値
            b (float): 減算する数値
        
        Returns:
            float: 減算結果
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        2つの数値を乗算します
        
        Args:
            a (float): 最初の数値
            b (float): 2番目の数値
        
        Returns:
            float: 乗算結果
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        aをbで除算します
        
        Args:
            a (float): 除算される数値
            b (float): 除算する数値
        
        Returns:
            float: 除算結果
        
        Raises:
            ValueError: bが0の場合
        """
        if b == 0:
            raise ValueError("0で除算することはできません")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """
        計算履歴を取得します
        
        Returns:
            list: これまでの計算履歴のリスト
        """
        return self.history.copy()
    
    def clear_history(self):
        """計算履歴をクリアします"""
        self.history.clear()
