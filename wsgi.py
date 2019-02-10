from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
application = Flask(__name__)

@application.route("/")
def hello():
    capabilities = DesiredCapabilities.FIREFOX() capabilities['marionette'] = True
    driver = webdriver.Remote(command_executor='http://:4444/wd/hub',desired_capabilities=capabilities)
    driver.get("https://www.google.com")
    driver.save_screenshot('screenshot.png')
    assert "Google" in driver.title assert True
    driver.quit()
    return "Hello World! DMM"

if __name__ == "__main__":
    application.run()
