FROM python:3.7

WORKDIR /UniCloud/Docker/FlaskWeb/flaskpy_project

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "app.py"]