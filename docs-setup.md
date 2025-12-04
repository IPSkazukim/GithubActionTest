# GitHub Pagesのセットアップ手順

このドキュメントは、GitHub Actionsで生成されたドキュメントをGitHub Pagesで公開するための設定手順を説明します。

## 手順

1. **リポジトリの設定画面を開く**
   - GitHubでリポジトリのページを開きます
   - 上部メニューの「Settings」をクリックします

2. **GitHub Pagesを有効にする**
   - 左サイドバーで「Pages」をクリックします
   - 「Source」セクションで以下を選択します:
     - Branch: `gh-pages`
     - Folder: `/ (root)`
   - 「Save」ボタンをクリックします

3. **ワークフローの実行**
   - ワークフローは、`main`または`master`ブランチへのpush時に自動実行されます
   - 手動で実行する場合:
     - 「Actions」タブを開きます
     - 「Generate Documentation」ワークフローを選択します
     - 「Run workflow」ボタンをクリックします

4. **ドキュメントの確認**
   - ワークフローが完了すると、GitHub Pagesが自動的にデプロイされます
   - 通常、デプロイには数分かかります
   - ドキュメントは以下のURLでアクセス可能になります:
     ```
     https://{username}.github.io/{repository-name}/
     ```

## トラブルシューティング

### ワークフローが失敗する場合

- 「Actions」タブでワークフローのログを確認してください
- `requirements.txt`に記載された依存関係が正しいか確認してください

### GitHub Pagesが表示されない場合

- Settings → Pages でGitHub Pagesが正しく設定されているか確認してください
- `gh-pages`ブランチが存在するか確認してください
- ワークフローが正常に完了しているか確認してください

### ドキュメントの内容を更新したい場合

- `src/`ディレクトリ内のPythonファイルのdocstringを編集してください
- 変更を`main`または`master`ブランチにpushすると、自動的にドキュメントが再生成されます

## ローカルでのプレビュー

ドキュメントをローカルで生成してプレビューすることもできます:

```bash
# 依存関係のインストール
pip install -r requirements.txt

# ドキュメントの生成
pdoc3 --html --output-dir docs --force src

# 生成されたファイルを移動
mv docs/src/* docs/
rm -rf docs/src

# シンプルなHTTPサーバーで確認
cd docs
python -m http.server 8000
```

ブラウザで `http://localhost:8000` を開くとドキュメントを確認できます。
