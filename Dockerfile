FROM python:3.12-slim
RUN useradd --create-home appuser
WORKDIR /app
COPY app.py .
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]
