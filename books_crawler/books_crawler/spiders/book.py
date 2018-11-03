# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from books_crawler.items import BookCrawlerItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    # Could use this instead of init function if you want to hardcode the category scraped
    start_urls = ['http://books.toscrape.com/']

    # We can use the function to give the starting urls from the comand
    # Use: scrapy crawl book -a category="link_from_website"
    #def __init__(self, category):
    #    self.start_urls = [category]

    def parse(self, response):
        # Get all the books on the main page
        books = response.xpath('//*[@class="product_pod"]')
        for book in books:
            # Get the individual book's page url
            link = book.xpath('.//h3/a/@href').extract_first()
            absolute_link = response.urljoin(link)

            # Acces the book's page and do callback
            yield scrapy.Request(absolute_link, callback=self.parse_book)
        
        """
        # Get the next page url
        next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # Join it with the response url because the URL we get from NEXT_btn is relative
        abs_next_page = response.urljoin(next_page)
        # GOTO the next page
        yield scrapy.Request(abs_next_page)
        """
        
    def parse_book(self, response):
        item  = ItemLoader(item=BookCrawlerItem(), response=response)
        # Scrape the book's page
        title = response.xpath('//h1/text()').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()
        stock = response.xpath('//*[@class="instock availability"]/text()').extract()[1]
        # Replce all the new lines with nothing
        stock = stock.replace('\n', '')
        image_urls = response.xpath('//img/@src').extract_first()
        # Replce all the dots with the domain to get the image
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')
        rating = response.xpath('//*[contains(@class,"star-rating")]/@class').extract_first()
        rating = rating.replace('star-rating', '')  
        description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

        item.add_value('image_urls', image_urls)
        item.add_value('description', description)
        item.add_value('price', price)
        item.add_value('rating', rating)
        item.add_value('stock', stock)
        item.add_value('title', title)

        return item.load_item()