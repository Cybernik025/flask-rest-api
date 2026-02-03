FROM python:3.12
EXPOSE 5000
WORKDIR /app
RUN pip install flask
ENV FLASK_APP=app
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]