import json
from seleniumwire import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
import time
import brotli
from model.config.HtmlTag import HtmlTag
from model.config.Web import Web
from Constant import HTML_TAG_CLASS, HTML_TAG_CLASSES, HTML_TAG_ID, HTML_TAG_XPATH

class WebWorker:
    
    def __init__(self, config: Web):
        firefox_profile = FirefoxProfile(config.firefox_profile_path)
        self.driver = webdriver.Firefox(firefox_profile=firefox_profile)

    def __get_tag_element(self, html_tag: HtmlTag) -> object:
        err = str.format("Invalid tag '%s' of type '%s'", html_tag.tag, html_tag.type)
        if(html_tag.type == HTML_TAG_ID):
            return self.driver.find_element_by_id(html_tag.tag)
        elif(html_tag.type == HTML_TAG_CLASS):
            return self.driver.find_elements_by_class_name(html_tag.tag)[0]
        elif(html_tag.type == HTML_TAG_CLASSES):
            elements = self.driver.find_elements_by_class_name(html_tag.tag)
            if(len(elements) == 0):
                raise Exception(err)
            return elements
        elif(html_tag.type == HTML_TAG_XPATH):
            return self.driver.find_element_by_xpath(html_tag.tag)
        else:
            raise Exception(err)

    def open_url(self, url: str):
        self.driver.get(url)

    def enter_input(self, input_tag: HtmlTag, input_content: str):
        self.wait_on(input_tag)
        tag_element = self.__get_tag_element(input_tag)
        tag_element.send_keys(input_content)
        
    def perform_click(self, button_tag: HtmlTag):
        self.wait_on(button_tag)
        tag_element = self.__get_tag_element(button_tag)
        tag_element.click()

    def enter_pin(self, pin_tag: HtmlTag, pin: str):
        self.wait_on(pin_tag)
        pin_elements = self.__get_tag_element(pin_tag)
        for i in range(len(pin)):
            pin_elements[i].send_keys(pin[i])

    def wait_on(self, html_tag: HtmlTag, time_out: int = 10, raise_exp: bool = True) -> bool:
        sleep_time = 0
        sleep_step = 0.1
        while(True):
            try:
                self.__get_tag_element(html_tag)
                return True
            except:
                time.sleep(sleep_step)
                sleep_time += sleep_step
                if(sleep_time >= time_out):
                    if(raise_exp):
                        raise Exception('Timedout waiting for tag %s', html_tag.tag)
                    return False

    def get_network_request_data(self, uri: str) -> dict:
        data = {}
        for request in self.driver.requests:
            if(request.url == uri):
                body = request.response.body
                binary = brotli.decompress(body)
                json_str = binary.decode("utf-8")
                return json.loads(json_str)