FROM python:3.9.2-slim-buster
ADD src / 
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD [ "python", "src/main.py"]