from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import re 

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def likeAndComment(self,instaUserName):
        bot = self.bot
        bot.get('https://www.instagram.com/' + instaUserName + '/')
        time.sleep(5)
        links=[]
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            source = bot.page_source
            data=bs(source, 'html.parser')
            body = data.find('body')
            script = body.find('span')
            for link in script.findAll('a'):
                if re.match("/p", link.get('href')):
                    links.append('https://www.instagram.com'+link.get('href'))
        for link in links:
            bot.get(link)
            time.sleep(2)
            like = bot.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')                                
            if like.get_attribute("aria-label")=="Like":
                like.click()

            
username = 'YOUR USERNAME';
password = 'YOUR PASSWORD
ed = InstagramBot(username, password)
ed.login()
ed.likeAndComment('therock')
print("Done")
