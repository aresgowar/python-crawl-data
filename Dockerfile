FROM python:3
 
WORKDIR /crawlpy
 
COPY requirements.txt ./
 
RUN pip3 install --no-cache-dir -r requirements.txt
 
COPY . .
 
CMD [ "python", "./crawl.py" ]
