import scrapy

class DiscussionForumSpider(scrapy.Spider):
    name = 'forum'
    page_number = 2
    start_urls = ['https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/%5Bgpgt%5D-satki-ceca-explain-why-cannot-find-suitable-candidates-her-posting-6353838.html']
    
    def parse(self, response):
        sequence = response.css('.thead strong::text').extract()
        date = response.css('.thead:nth-child(1)::text')[2:-2:4].extract()
        user = response.css('.bigusername::text').extract()
        comment = response.css('.post_message::text').extract()
        
        
        yield {
                'Sequence' : sequence,
                'Date' : [dt.strip() for dt in date],
                'User' : user,
				'Comment' : [com.strip() for com in comment]
                }
        page = str(DiscussionForumSpider.page_number)
        next_page = 'https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/%5Bgpgt%5D-satki-ceca-explain-why-cannot-find-suitable-candidates-her-posting-6353838'+ '-'+ page + '.html'
        if DiscussionForumSpider.page_number < 8:
            DiscussionForumSpider.page_number = DiscussionForumSpider.page_number + 1
            yield response.follow(next_page, callback= self.parse)
            