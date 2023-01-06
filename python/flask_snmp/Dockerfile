FROM --platform=linux/amd64 python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP controller.py
EXPOSE 9090
CMD ["python3","-m","flask","run","--host=0.0.0.0"]