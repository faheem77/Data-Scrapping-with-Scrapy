import scrapy
from tldextract import extract


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.highpointmarket.org/exhibitor?fbclid=IwAR3YbWUNDHuvazHryg6VhZJvx5B-QK1S3LDA5UuTfhwDkYVuB17dcpRk1so']
    
    
    def parse(self, response, **kwargs):
        products = response.css('div.exhibitor-row')
        num = 0
        
        for product in products:
            
            yield {
                "Title": product.css('h3.exh-name::text').extract(),
                "Location": product.css(f'#ctl00_ContentPlaceHolder1_lvExhibitors_ctrl{num}_lblLocation::text').get(),
                "Shuttle shop": product.css(f"#ctl00_ContentPlaceHolder1_lvExhibitors_ctrl{num}_lblBusStop::text").extract(),
                "Neighbourhood": product.css(f'#ctl00_ContentPlaceHolder1_lvExhibitors_ctrl{num}_lblNeighborhood::text').extract(),      
            }
            num += 1
            
            
    