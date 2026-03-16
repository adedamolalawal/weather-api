FROM python:3.8-alpine

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY test.py test.py
EXPOSE 5000
ENV PORT=5000
CMD ["python", "test.py"]