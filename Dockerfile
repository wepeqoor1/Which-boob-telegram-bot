FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
# RUN python3 -m venv .venv
# RUN . .venv/bin/activate 
RUN  pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

