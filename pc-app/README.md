```
python -m venv .venv
pip-compile
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
pyinstaller --onefile --name alexa-ifttt-pc-notification.exe app.py
```
