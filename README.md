# GithubActiontest
githubのactionの動作検証用

## 機能

このリポジトリは、GitHub Actionsを使用して以下の機能を提供します：

1. **ドキュメント自動生成**: ソースコードから自動的にHTMLドキュメントを生成
2. **Pylintコード品質チェック**: コーディング規約の自動チェック

## ドキュメント自動生成

このリポジトリは、GitHub Actionsを使用してソースコードから自動的にドキュメントを生成します。

### ドキュメント生成機能

- Pythonソースコードのdocstringから自動的にHTMLドキュメントを生成
- GitHub Pagesにドキュメントを自動デプロイ
- mainまたはmasterブランチへのpush時に自動実行

### ドキュメント生成の仕組み

1. **ソースコード**: `src/` ディレクトリにPythonファイルとdocstringが含まれています
2. **GitHub Actions**: `.github/workflows/generate-docs.yml` がドキュメント生成を自動化します
3. **pdoc3**: Pythonのdocstringから美しいHTMLドキュメントを生成します
4. **GitHub Pages**: 生成されたドキュメントは `gh-pages` ブランチにデプロイされます

### ドキュメントの閲覧

ドキュメントは以下のURLで閲覧できます（GitHub Pagesを有効にした後）:
```
https://{username}.github.io/GithubActiontest/
```

### ローカルでのドキュメント生成

```bash
# 依存関係のインストール
pip install -r requirements.txt

# ドキュメントの生成
pdoc3 --html --output-dir docs --force src
```

## Pylintコード品質チェック

このリポジトリでは、GitHub Actionsを使用してPylintによるコード品質チェックを自動実行します。

### Pylint機能

- すべてのブランチへのpush時に自動実行
- プルリクエスト作成時に自動実行
- コーディング規約違反を検出して報告
- スコアが8.0未満の場合はビルド失敗

### ローカルでのPylint実行

```bash
# 依存関係のインストール
pip install -r requirements.txt

# Pylintの実行（すべてのソースファイル）
pylint src/ --rcfile=.pylintrc

# Pylintの実行（特定のファイル）
pylint src/calculator.py --rcfile=.pylintrc
```

### Pylint設定

`.pylintrc` ファイルでPylintの動作を設定しています：
- 行の最大長: 100文字
- 無効化されたルール: docstring必須チェック、公開メソッド数チェックなど
- コーディング規約: PEP 8準拠

### コード品質の例

#### 良い例（既存のファイル）
- `src/calculator.py`: 適切にフォーマットされたコード
- `src/utils.py`: ドキュメントとタイプヒントが充実したコード
- `src/euclidean.py`: 詳細なdocstringを持つコード

#### 悪い例（テスト用ファイル）
- `src/bad_example.py`: 意図的にコーディング規約に違反したファイル
  - 命名規約違反（関数名、変数名、クラス名）
  - 未使用のインポート
  - 引数が多すぎる関数
  - グローバル変数の使用
  - ネストが深すぎるコード

このファイルを使用して、Pylintがどのように問題を検出するかを確認できます。

### プロジェクト構造

```
.
├── .github/
│   └── workflows/
│       ├── generate-docs.yml  # ドキュメント生成のワークフロー
│       └── pylint.yml         # Pylintコード品質チェック
├── src/                        # Pythonソースコード
│   ├── __init__.py
│   ├── calculator.py          # 計算機クラス
│   ├── euclidean.py           # ユークリッドの互除法
│   ├── utils.py               # ユーティリティ関数
│   └── bad_example.py         # Pylintテスト用（意図的に悪いコード）
├── .pylintrc                   # Pylint設定ファイル
├── requirements.txt            # Python依存関係
└── README.md                   # このファイル
```
