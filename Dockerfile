FROM python:3.9-slim-buster
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "webserver.py"]
