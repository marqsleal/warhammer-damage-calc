FROM python:3.12.3

WORKDIR /app

COPY requirements.in ./

RUN pip install --no-cache-dir pip-tools && \
    pip-compile requirements.in --output-file requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]