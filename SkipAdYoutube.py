#! python3
# -*- coding:utf-8 -*-
import sys,time,os
from datetime import datetime,timedelta,timezone
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def skipAd(seconds=1,browser='chrome'):
    print('skAd started')
    
    #common setting
    start_urls = ['https://www.youtube.com/']
    os.environ['PATH'] = os.environ['PATH'] + ":./"
    
    #each browser's setting. now only chrome.
    if browser == 'chrome':
        #capabilities
        desiredcapabilities = DesiredCapabilities.CHROME.copy()
        desiredcapabilities['platform'] = os.uname().sysname
        desiredcapabilities['version'] = os.uname().version
        
        #options
        options = webdriver.chrome.options.Options()
        user_data_dir = os.environ['HOME'] + '/.config/google-chrome/'
        profile_path = './Default'
        options.add_argument("--user-data-dir=" + user_data_dir)
        options.add_argument("--profie-directory=" + profile_path)
        
        #run browser
        driver = webdriver.Chrome(desired_capabilities=desiredcapabilities, options=options)
        #driver = webdriver.Chrome()
        
    elif browser == 'firefox':
        #options
        profile = webdriver.FirefoxProfile(os.environ['HOME'] + '/.mozilla/firefox/w847djlu.default-esr')
        
        #run browser
        driver = webdriver.Firefox(profile)
        
    #open url
    driver.get(start_urls[0])
        
    #start observation
    while True:
        try:
            time.sleep(seconds)
            
            #search target elements
            div = None            
            div = driver.find_elements_by_css_selector('button.ytp-ad-skip-button')
            if len(div) <= 0:
                div = driver.find_elements_by_css_selector('div.ytp-ad-image-overlay .ytp-ad-overlay-close-button, div.ytp-ad-text-overlay .ytp-ad-overlay-close-button')
            
            #if target exists, run click operation.    
            if type(div) is list and len(div) >= 1:
                print("catch ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%s"))
                for item in div:
                    if isinstance(item, WebElement) and 'click' in dir(item):
                        if item.is_enabled() == True and item.is_displayed() == True:
                            item.click()
                            print("click ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%s"))
            elif type(div) is WebElement:
                print("catch ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%s"))
                if type(div) is WebElement and 'click' in dir(div):
                    if div.is_enabled() == True and div.is_displayed() == True:
                        div.click()
                        print("click ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%s"))
                
        except KeyboardInterrupt as kiInterrupt:
            driver.close()
            driver.quit()
            break
        except TimeoutException as toutEx:
            print("timeout ytp-ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        except Exception as ex:
            print(driver.current_url)
            print("none clickbtn?:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        finally:
            pass
    #end while, close and quit()
    driver.close()
    driver.quit()    
        
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        skipAd(int(sys.argv[1]), sys.argv[2])
    else:
        skipAd()
