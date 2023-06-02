Place .exe in `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`

```
python -m venv .venv
pip-compile
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.pyw
pyinstaller --onefile --name alexa-ifttt-pc-notification.exe app.pyw
```
