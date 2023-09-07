# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /code
# command to run on development inviroment
ENV FLASK_ENV development
#creatin enviroments variable
ENV ROOMS_FILES_PATH rooms/
# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
# copy the content of the local src directory to the working directory
COPY / .
#publish on port 5000
EXPOSE 5000

#health check
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5000/health || exit 1
CMD [ "python", "./chatApp.py" ]
