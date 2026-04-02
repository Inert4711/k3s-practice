FROM python:3.11-slim as builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt    

FROM python:3.11-slim
RUN useradd -m -u 1000 appuser && \
    mkdir -p /app && chown -R appuser:appuser /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --chown=appuser:appuser app/ .
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]