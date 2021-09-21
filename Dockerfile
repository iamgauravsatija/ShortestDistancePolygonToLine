FROM python:3

ENV PYTHONUNBUFFERED=1
WORKDIR .
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]