import scrapy
#

# print(scrapy)
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://secure.runescape.com/m=forum/forums?75,76,331,66006366']

    def parse(self, response):
        print("Response:")
        print(response.css)
        for title in response.css('.forum-post__body'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.  parse)

