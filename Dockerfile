FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /hackernews
WORKDIR /hackernews
COPY requirements.txt /hackernews/
RUN pip install -r requirements.txt
COPY . /hackernews/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
