FROM python:3.10.9-slim-buster
WORKDIR /app
RUN pip install flask
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
