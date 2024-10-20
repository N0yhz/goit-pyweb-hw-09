# Scrapy web-scraping
## Steps:

1. **installed scrapy**
2. **started new scrapy project**
3. **genspider for the web**
4. **wrote the script for filtering data**
5. **add "FEEDS" in to the scrapy settings (as it can sort out needed KEY for each JSON file)**
    ```
    FEEDS = {
    'quotes.json': {
        'format': 'json',
        'encoding': 'utf-8',
        'store_empty': False,
        'indent': 4,
        'fields': ['quote', 'author', 'tags'],
    },
    'authors.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': ['name', 'born_date', 'born_location', 'description'],
        'indent': 4,
    }
    }
    ```
6. **wrote the script to run crawl as "main.py" file**
7. **wrote the script to upload data to existed MongoDB database**