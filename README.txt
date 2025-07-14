==============================
📚 社内FAQチャットボット - README
==============================

■ このプロジェクトの目的
LangChain × OpenAI × Streamlit × FAISS を使い、
社内FAQを自動で回答できるチャットボットを構築する。
ポートフォリオ用のデモとしても活用可能。

---

■ 使用技術スタック
- Python 3.10+
- LangChain
- OpenAI API（APIキー必要）
- FAISS（埋め込み検索用）
- Streamlit（UI構築用）

---

■ ディレクトリ構成（主要ファイル）

faq_chatbot/
├─ app/
│   ├─ main.py             ← Streamlit UI本体
│   ├─ vector_store.py     ← FAQ CSV → FAISS変換スクリプト
│   ├─ chains.py           ← 応答ロジック定義
├─ data/
│   └─ faq.csv             ← FAQデータ（CSV形式）
├─ faiss_index/            ← ベクトルデータ保存先（自動生成）
├─ .env.sample             ← APIキーのテンプレファイル（実キーは入れない）
├─ run_faq_chatbot.bat     ← 起動バッチ（PYTHONPATH + ベクトル生成 + UI起動）
└─ README.txt              ← 本ファイル

---

■ セットアップ手順

1. 依存パッケージのインストール
   pip install -r requirements.txt

2. `.env.sample` をコピーして `.env` にリネームし、
   OpenAI API キーをセット
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

---

■ 起動方法（Windows専用）

run_faq_chatbot.bat を実行するだけで、
1) 作業ディレクトリ移動
2) PYTHONPATH設定
3) FAQベクトル再生成
4) Streamlit 起動
を自動実行します。

---

■ FAQ更新時の流れ
data/faq.csv を編集後、run_faq_chatbot.bat を再実行すれば
自動でベクトルストアを再構築して反映されます。

---

■ セキュリティ注意
- `.env` に実際の API キーを入れたまま **ZIPやGitに含めない** でください。
- 共有・提出には必ず `.env.sample`（ダミーキー）を同梱してください。

---

© 田中 大輝｜2025年 ポートフォリオ用
