@echo off

.\venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r .\requirements.txt\

python main.py