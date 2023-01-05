# start from the latest version of the Python 3.9 image
FROM python:3.9
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1
# set the working directory to /app
WORKDIR /app
# copy the requirements.txt file to the working directory
COPY requirements.txt .
# install the dependencies
RUN pip install -r requirements.txt
# copy the rest of the app's source code to the working directory
COPY . /app
# run the app
CMD python manage.py runserver 0.0.0.0:$PORT
