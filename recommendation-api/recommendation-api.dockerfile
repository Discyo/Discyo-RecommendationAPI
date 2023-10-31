FROM python:3.8-slim

# set a directory for the app
WORKDIR /usr/src/app

# copy requirements to container
COPY ./requirements.txt /requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# copy all the files to the container
COPY ./app /usr/src/app

# define the port number the container should expose
EXPOSE 8000

# run the command
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]