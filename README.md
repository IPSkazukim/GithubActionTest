# GithubActiontest
githubのactionの動作検証用

## ドキュメント自動生成

このリポジトリは、GitHub Actionsを使用してソースコードから自動的にドキュメントを生成します。

### 機能

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

### プロジェクト構造

```
.
├── .github/
│   └── workflows/
│       └── generate-docs.yml  # ドキュメント生成のワークフロー
├── src/                        # Pythonソースコード
│   ├── __init__.py
│   ├── calculator.py          # 計算機クラス
│   └── utils.py               # ユーティリティ関数
├── requirements.txt            # Python依存関係
└── README.md                   # このファイル
```
