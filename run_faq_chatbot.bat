@echo off
REM ===== タイトルと見た目 =====
title FAQチャットボット起動中...
echo -----------------------------
echo 🚀 FAQチャットボット起動中
echo -----------------------------
echo.

REM ===== 作業ディレクトリに移動 =====
cd /d D:\Dropbox\Work\portfolio_1\faq_chatbot_complete\faq_chatbot

REM ===== ベクトルストア再生成（csv -> FAISS） =====
echo 🔄 ベクトルストアを再構築中...
python -c "from app.vector_store import build_vector_store; build_vector_store('data/faq.csv')"

REM ===== Streamlit アプリ起動 =====
echo 🚪 Streamlitアプリを起動します...
set PYTHONPATH=.
streamlit run app/main.py

REM ===== 完了表示（万が一落ちた時用） =====
pause
