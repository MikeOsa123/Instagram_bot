from selenium import webdriver
from time import sleep
from credentials import username, pw

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following')]".format(self.username)).click()
        sleep(2)
        sugs = self.driver.find_element_by_xpath("//h4[contains(text(), Suggestions)]")
        self.driver.execute_script('arguments[0].scrollIntoView()')
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)        
        

my_bot = InstaBot(username, pw)
my_bot.get_unfollowers()