from python:3.12-slim
RUN mkdir /app && cd /app 
WORKDIR /app 
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "app.py"]
