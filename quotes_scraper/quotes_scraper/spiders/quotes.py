import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_text = quote.css('span.text::text').get()
            author_name = quote.css('span small::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'quote': quote_text,
                'author': author_name,
                'tags': tags
            }

        author_url = quote.css('span a::attr(href)').get()
        if author_url is not None:
            author_page = response.urljoin(author_url)
            yield scrapy.Request(author_page, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        name = response.css('h3.author-title::text').get().strip()
        born_date = response.css('span.author-born-date::text').get()
        born_location = response.css('span.author-born-location::text').get()
        description = response.css('div.author-description::text').get().strip()

        yield {
            'name': name,
            'born_date': born_date,
            'born_location': born_location,
            'description': description,
        }