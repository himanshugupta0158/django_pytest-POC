# In this test we are going to use selenium web-driver

import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

# Example 1

# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         '''
#         make sure you have downloaded your browser's webdriver
#         and place that webdriver's exe file in folder 
#         where you can access it
#         '''
#         driver = webdriver.Chrome("./chromedriver")
#         driver.get(("%s%s" %(self.live_server_url , "/admin/")))
#         assert "Log in | Django site admin"  in driver.title



# Example 2
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title


# Example 3
# fixture for Chrome
# @pytest.fixture(scope="class")
# def chrome_driver_init(request):
    
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver" , options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()    


# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title

@pytest.fixture(params=["chrome" , "firefox"] , scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=r"./chromedriver")
    
    # you need firefox webdriver -> geckodriver and firefox browser
    if request.param == "firefox" :
        web_driver = webdriver.Firefox(executable_path=r"./geckodriver")
    request.cls.driver = web_driver 
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class Test_URL_Chrome:
    def test_open_url(self , live_server):
        self.driver.get(("%s%s" %(live_server.url , "/admin/")))
        assert "Log in | Django site admin" in self.driver.title 
        

