"""
bad_example.py

pylintの動作を確認するための、意図的にコーディング規約に違反したファイル
"""

import os
import sys
import json  # 使用していないimport


# 変数名が規約違反（大文字で始まっている）
MyVariable = 10
AnotherBadName = "test"

def BadFunctionName():  # 関数名が規約違反（キャメルケースになっている）
    """docstringはあるが、関数名が悪い"""
    x=1+2+3+4+5  # スペースがない
    return x

def function_with_too_many_args(a, b, c, d, e, f, g, h, i):  # 引数が多すぎる
    """引数が多すぎる関数"""
    return a+b+c+d+e+f+g+h+i

class bad_class_name:  # クラス名が規約違反（小文字で始まっている）
    """クラス名が悪い例"""
    
    def __init__(self):
        self.x = 1
    
    def method(self):
        """メソッド"""
        if True:
            if True:
                if True:
                    if True:
                        if True:  # ネストが深すぎる
                            print("深すぎるネスト")


# 行が長すぎる例
very_long_line = "これは非常に長い行の例で、pylintの行の長さ制限を超えることを意図しています。この行は100文字を超えるように書かれています。"

# 複数の問題を持つ関数
def problematic_function(X, Y):  # 引数名が規約違反（大文字）
    # TODO: これは後で修正する必要があります
    result = X + Y
    unused_variable = "使われていない変数"  # 使用されていない変数
    return result

# グローバル変数（推奨されない）
global_counter = 0

def increment_counter():
    """グローバル変数を変更する関数"""
    global global_counter  # グローバル変数の使用
    global_counter += 1
    return global_counter


# 空白行が多すぎる



# タブとスペースの混在を避けるため、この例は削除
# 代わりに、他の問題を持つ関数を追加
def another_problematic_function():
    """もう一つの問題のある関数"""
    pass  # 空の関数
