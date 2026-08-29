FROM python:3.14
WORKDIR /app
COPY requirements.txt req.txt
RUN pip3 install -r req.txt
COPY . .
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["main.py"]