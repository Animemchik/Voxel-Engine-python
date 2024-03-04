@echo off

python -m venv venv

.\venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r .\requiretments.txt\

python main.py
