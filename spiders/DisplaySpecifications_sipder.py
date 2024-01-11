import scrapy
import re
# pip install webscrapingapi-scrapy-sdk
#from webscrapingapi_scrapy_sdk import WebScrapingApiSpider, WebScrapingApiRequest
from scrapy.utils.project import get_project_settings
from urllib.parse import urlencode
from DisplaySpecifications.settings import API_KEY

API_KEY = API_KEY

def get_scraperapi_url(url):
    payload = {'apikey': API_KEY, 'url': url}
    proxy_url = 'https://api.zenrows.com/v1/?' + urlencode(payload) + '&premium_proxy=true'
    print(proxy_url)
    return proxy_url

class DisplayspecificationsSpider(scrapy.Spider):
    name = 'devicespecifications'
    #allowed_domains = ['www.zenrows.com']
    start_urls = ['https://www.devicespecifications.com/en']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=get_scraperapi_url(url) , callback=self.parse)
    # Navigation through menus

    def parse(self, response, **kwargs):
        for brand_listing in response.css('.brand-listing-container-frontpage a::attr(href)').getall():
            yield scrapy.Request(url=get_scraperapi_url(brand_listing) , callback=self.parse_brand_listing)

    def parse_brand_listing(self, response, **kwargs):
        for product_url in response.css(".model-listing-container-80 a::attr(href)").getall():
            meta = dict()
            meta['url'] = product_url
            request = scrapy.Request(url=get_scraperapi_url(product_url) , callback=self.parse_item , meta=meta)
            # Using "Crawl Once Middleware" to aviod duplicate items
            request.meta['crawl_once'] = True
            yield request

    def parse_item(self, response, **kwargs):
        spec = dict()
        try:
            spec['name'] = response.css("h1::text").get()
            spec['image_url'] = response.css(
                "meta[property*='og:image']::attr(content)").get()
            spec['url'] = response.meta.get('url')

            # Getting Main Heading E.g: "Brand, series, model"
            for main_tab in response.css('.section-header'):
                try:
                    main_heading = main_tab.css(
                        'h2::text').get().replace('.', ',')
                except AttributeError:
                    continue
                spec[main_heading] = {}
                table = main_tab.xpath('following-sibling::table[1]')

                # Getting Sub Heading E.g: "Brand"
                for sub_tab in table.css('tr'):
                    try:
                        sub_heading = sub_tab.css(
                            'td::text').get().replace('.', ',')
                    except AttributeError:
                        continue
                    value = sub_tab.css('td').xpath(
                        'following-sibling::td[1]/text()').getall()

                    # Check for Mulitple Values
                    if len(value) > 1:
                        self.logger.info('Muliple Values Found')
                        counter = 1
                        for separate_value in value:
                            try:
                                separate_value = re.sub(
                                    ' +', ' ', separate_value).strip()
                            except AttributeError:
                                self.logger.info('Value Not Found')
                                continue
                            sub_heading_number = sub_heading + \
                                ' ' + str(counter)
                            counter += 1
                            spec[main_heading][sub_heading_number] = separate_value
                    else:
                        try:
                            value = re.sub(' +', ' ', " ".join(value)).strip()
                        except AttributeError:
                            self.logger.info('Value Not Found')
                            continue
                        spec[main_heading][sub_heading] = value
            # Check
            if len(spec) < 5:
                self.logger.info(
                    'Product Page Not Fully Load Discarding the Item')
                return
            yield spec
        except (AttributeError, IndexError):
            return
