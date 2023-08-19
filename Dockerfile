FROM python:3.8-slim
WORKDIR /app
COPY app.py .
RUN pip install flask nltk
EXPOSE 5000
CMD ["python", "app.py"]
