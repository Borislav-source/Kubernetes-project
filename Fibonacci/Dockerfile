FROM python:3.7


RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

expose 8000

WORKDIR /code

COPY . ./code

# runs the production server
ENTRYPOINT ["python", "code/fibonacci/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]