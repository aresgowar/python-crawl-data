# python-crawl-data
```shell

pip install scrapy

scrapy startproject crawler

scrapy shell https://stackoverflow.com/questions/tagged/python

scrapy crawl crawler -o comments.json

pip install scrapy-xlsx

scrapy crawl posts -o posts.xlsx



docker build -t aresgowar/aresdockercrawl:1.0 .

docker compose up

docker cp 0fe874e0a8517b19185829605f5c11831517315807e6b928df64b5bae1ef1793:/crawldata/data.csv D:/MT/Python/crawldata/data.csv

docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home jenkinsci/blueocean

docker run -u 0 --privileged --name jenkins -it -d -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home/jenkins_home:/var/jenkins_home jenkins/jenkins:latest
```
