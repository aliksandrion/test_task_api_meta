FROM python:3.10

WORKDIR /usr/src/eVisionTech

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /usr/src/eVisionTech

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0.8000"]