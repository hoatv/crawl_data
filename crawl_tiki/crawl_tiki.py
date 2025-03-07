from lxml import html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HtmlGetter:

    def get_html(self, url):
        pass


class HtmlParseGetter(HtmlGetter):

    def __init__(self, subject):
        self.subject = subject

    def get_html(self, url):
        html_source = self.subject.get_html(url)
        html_element = html.fromstring(html_source)
        return html_element


class SeleniumHtmlGetter(HtmlGetter):
    def __init__(self, scroll_to_bottom=True):
        self.scroll_to_bottom = scroll_to_bottom

    def get_html(self, url):
        browser = webdriver.Chrome("C:\\Users\\hoatv\\Downloads\\chromedriver_win32\\chromedriver.exe")
        browser.maximize_window()
        browser.get(url)

        if self.scroll_to_bottom:
            last = None
            for v in range(500):
                for k in range(5):
                    browser.find_element_by_xpath('//html').send_keys(Keys.DOWN)
                if last is not None and last == browser.execute_script('return window.pageYOffset;'):
                    break
                last = browser.execute_script('return window.pageYOffset;')

        html_source = browser.page_source
        browser.quit()
        return html_source


if __name__ == '__main__':
    url = 'https://tiki.vn/deal-hot?src=header_label&_lc=Vk4wMzQwMjAwMDM%253D&tab=now&page=2'
    html_getter = HtmlParseGetter(SeleniumHtmlGetter( ))
    html_tree = html_getter.get_html(url)
    for v in html_tree.xpath("//a[@class='deal-item']"):
        print(v.xpath("./div[@class='title']/text()"))
        print(v.xpath(".//span[@class='price-regular']/text()"))
        print(v.xpath(".//div[@class='price-sale']/text()"))
        print(v.xpath("./div[@class='image']//img/@src"))
        print()
