```
python -m venv .venv
pip-compile
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$Env:MQTT_BROKER = "192.168.1.61"
python app.py

```

```
curl -XPOST -H "Authorization: 6136a6c5-619b-4554-bad8-5aef3ffa9aa7" -d '{"hello":"world"}' 127.0.0.1:8080
```
