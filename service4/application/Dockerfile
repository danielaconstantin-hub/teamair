FROM python:3.6

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5004

ENTRYPOINT ["python3", "__init__.py"]