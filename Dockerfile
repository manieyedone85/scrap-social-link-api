FROM python:3.7
COPY /src /app
WORKDIR /app
#RUN mkdir requests
RUN pip install -r requirements.txt
RUN apt update
#RUN apt install -y libgl1-mesa-glx
ENTRYPOINT ["python"]
CMD ["Main.py"]
