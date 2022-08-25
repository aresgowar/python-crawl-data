```shell

pip install scrapy

scrapy startproject crawler

scrapy shell https://stackoverflow.com/questions/tagged/python

scrapy crawl crawler-spider -o posts.json

pip install scrapy-xlsx

scrapy crawl crawler-spider -o posts.xlsx

docker compose up

docker cp a1dc5ee47d575f7b15a8d4a037d09bb3c8a9b93a6d672e6a0ac75358391965ce:/crawlpy/questions.csv D:/SYNC/Learn/Python/CrawlDataPython/questions.csv

```