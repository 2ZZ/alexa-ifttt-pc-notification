FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN python -m venv .venv
RUN . .venv/bin/activate

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]