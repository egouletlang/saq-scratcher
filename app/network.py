import os
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseNetworkInteractor:

    def __init__(self):
        implicit_wait_timeout = os.environ.get('IMPLICIT_WAIT_TIMEOUT', 10)
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(implicit_wait_timeout)
        self.driver.set_window_size(1024, 768)


    def get_url(self, url):
        print(f"Getting {url}")
        self.driver.get(url)

    def find_elem(self, nested_elements):
        elem = self.driver
        for (elem_type, elem_name) in nested_elements:
            elem = elem.find_element(elem_type, elem_name) if elem else None
        return elem


    def wait_for_elem_visibility(self, elem):
        print(f"Waiting for element to be visible")
        if isinstance(elem, tuple):
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(elem))
        else:
            WebDriverWait(self.driver, 10).until(EC.visibility_of(elem))


    def read_html(self):
        return self.driver.page_source

class SaqNetworkInteractor(BaseNetworkInteractor):

    def run(self, url):
        self.get_url(url)
        
        # wait for the `available in store` button
        btn = self.find_elem(
            nested_elements=[
                (By.CLASS_NAME, "available-in-store"),
                (By.CLASS_NAME, "action"),
            ]
        )
        self.wait_for_elem_visibility(btn)

        # click on the `available in store` button
        btn.click()

        # wait for `available in store` content
        self.wait_for_elem_visibility((By.CLASS_NAME, "store-list-item-content"))

        return self.read_html()

