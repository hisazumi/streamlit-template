# Streamlit Template

**複数のStreamlitアプリケーション開発用テンプレート**

GitHub CodespacesとVSCodeでの開発に最適化された、複数のStreamlitアプリを効率的に管理できるテンプレートプロジェクトです。

## 🚀 クイックスタート

### GitHub Codespaces（推奨）

1. **このリポジトリをフォーク**
2. **Codespace作成**: 緑の「Code」ボタン → 「Create codespace on main」
3. **自動セットアップ完了を待機**
4. **アプリ実行**:
   ```bash
   uv run streamlit run hello_world.py
   ```

### ローカル環境（コンテナを使わない方法）

事前に[Git](https://git-scm.com/downloads)をインストールしてください。VS Codeを使う場合は、リポジトリを開いて「ターミナル」→「新しいターミナル」から以下のコマンドを実行できます。

#### Windows（PowerShell）

1. uvをインストールします。

   ```powershell
   winget install --id=astral-sh.uv -e
   ```

2. PowerShellまたはVS Codeを再起動し、アプリを準備・実行します。

   ```powershell
   git clone https://github.com/hisazumi/streamlit-template.git
   cd streamlit-template
   uv sync
   uv run streamlit run hello_world.py
   ```

#### macOS（ターミナル）

1. [Homebrew](https://brew.sh/)でuvをインストールします。

   ```bash
   brew install uv
   ```

2. アプリを準備・実行します。

   ```bash
   git clone https://github.com/hisazumi/streamlit-template.git
   cd streamlit-template
   uv sync
   uv run streamlit run hello_world.py
   ```

起動後、ブラウザが自動で開かない場合は <http://localhost:8501> にアクセスしてください。終了するにはターミナルで `Ctrl+C` を押します。Pythonはuvが`.python-version`に従って用意するため、通常は別途インストールする必要はありません。

## 📁 プロジェクト構造

```
streamlit-template/
├── hello_world.py             # メインアプリ
├── tests/                     # Streamlit画面の自動テスト
├── .github/workflows/         # GitHub Actions
├── .devcontainer/             # GitHub Codespaces設定
├── .vscode/                   # VSCode設定
├── .streamlit/                # Streamlit設定・シークレット
├── pyproject.toml             # プロジェクト設定（uv対応）
├── uv.lock                    # 依存関係の固定（Git管理対象）
└── .gitignore                 # Git除外設定
```

## 🎯 使用方法

### 新しいアプリの作成

```python
# my_new_app.py
import streamlit as st

st.title("My New App 🚀")
st.write("Hello, Streamlit!")

name = st.text_input("Your name:")
if name:
    st.success(f"Hello, {name}!")
```

### 複数アプリの実行

```bash
# 異なるポートで複数アプリを同時実行
streamlit run hello_world.py --server.port 8501 &
streamlit run my_new_app.py --server.port 8502 &
```

## 🛠️ 開発環境

### 含まれる設定

- **GitHub Codespaces**: 自動環境構築
- **VSCode設定**: Python開発最適化
- **Python 3.12**: ローカル・Codespaces・デプロイ環境を統一
- **Formatter / Linter**: Ruff
- **自動テスト**: pytest・GitHub Actions
- **Streamlit設定**: ポート転送・ファイル変更時の再実行

### 推奨VSCode拡張機能

- Python
- Ruff

## 🔧 カスタマイズ

### 依存関係の追加

```bash
# uv使用
uv add package-name
```

uvを使用する場合、`uv add`は`pyproject.toml`と`uv.lock`を同時に更新します。

### コード品質チェック

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

### Streamlit設定

- **基本設定**: `.streamlit/config.toml`
- **シークレット**: `.streamlit/secrets.toml` (gitignoreに含まれます)

### VSCode設定

- **エディタ設定**: `.vscode/settings.json`
- **推奨拡張**: `.vscode/extensions.json`

## 🔐 セキュリティ

- **`.streamlit/secrets.toml`** は自動的にgitignoreされます
- **APIキー**は secrets.toml で管理してください
- **本番環境**では環境変数を使用してください

## 📦 デプロイ

### Streamlit Community Cloud

1. `pyproject.toml`と`uv.lock`を含めてGitHubにプッシュ
2. [share.streamlit.io](https://share.streamlit.io) でデプロイ（Python 3.12を選択）
3. メインファイル: `hello_world.py` または作成したアプリファイル

Streamlit Community Cloudは`uv.lock`を検出し、固定された依存関係をインストールします。

### その他のプラットフォーム

- Heroku
- Railway
- Render
- Docker

## 🤝 貢献

プルリクエストやイシューを歓迎します！

## 📄 ライセンス

MIT License

---

**🌟 Happy Streamlit Development!**
