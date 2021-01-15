#! python3
# -*- coding:utf-8 -*-
import sys, time, os, csv
import platform
from datetime import datetime,timedelta,timezone
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import InvalidSessionIdException
from msedge.selenium_tools import Edge, EdgeOptions

def skipAd(seconds=1, browser='chrome'):
    if browser != 'chrome' and browser != 'firefox' and browser != 'edge':
        print('No target borwser was indicated... Please indicate target browser (chrome or firefox or edge)')
        sys.exit(1)
    
    print('skAd started')
    
    #common setting
    start_urls = ['https://www.youtube.com/']
    
    if platform.system() == 'Windows':
        os.environ['PATH'] = os.environ['PATH'] + ";." + os.sep + "win"
    else:
        os.environ['PATH'] = os.environ['PATH'] + ":./linux"
    
    #profile
    user_data_dir = ''
    profile_path = ''
    cfgName = ''
    if browser == 'chrome':
        cfgName = 'target_profile_chrome.cfg'
    elif browser == 'firefox':
        cfgName = 'target_profile_firefox.cfg'
    elif browser == 'edge':
        cfgName = 'target_profile_edge.cfg'
    #check what config file exists.
    if os.path.exists(cfgName) == False:
        print('No Configuration File... Please make ' + cfgName + ' and setting.')
        sys.exit(2)
        
    #read config file.
    with open(cfgName, 'r') as f:
        for row in csv.reader(f):
            if row[0] == 'user_data_dir':
                user_data_dir = row[1]
            if row[0] == 'profile_path':
                profile_path = row[1]    
    
    #check profile place
    useProfile = True
    if os.path.exists(user_data_dir + profile_path) == False:
        print('No such as profile path... ' + user_data_dir + profile_path)
        print('This process will run without profile.')
        useProfile = False
    
    #each browser's setting. now only chrome.
    if browser == 'chrome':
        #capabilities
        desiredcapabilities = DesiredCapabilities.CHROME.copy()
        desiredcapabilities['platform'] = platform.system()
        desiredcapabilities['version']  = platform.version()
        
        if useProfile == True:
            #options
            options = webdriver.chrome.options.Options()
            options.add_argument("--user-data-dir=" + user_data_dir)
            options.add_argument("--profie-directory=" + profile_path)
            
            #run browser
            driver = webdriver.Chrome(desired_capabilities=desiredcapabilities, options=options)
        else:
            #run browser
            driver = webdriver.Chrome(desired_capabilities=desiredcapabilities)
        
    elif browser == 'firefox':
        if useProfile == True:
            #options
            profile = webdriver.FirefoxProfile(user_data_dir + profile_path)
            #run browser
            driver = webdriver.Firefox(profile)
        else:
            driver = webdriver.Firefox()
            
    elif browser == 'edge':
        if useProfile == True:
            #profile
            options = EdgeOptions()
            #options.use_chromium = True
            options.add_argument('--user-data-dir=' + user_data_dir)
            options.add_argument('--profile-directory=' + profile_path)
            path = 'win' + os.sep + 'msedgedriver.exe'
            #run browser
            driver = Edge(executable_path=path, options=options)
        else:
            driver = Edge('win' + os.sep + 'msedgedriver.exe')
        
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
                print("catch ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                for item in div:
                    if isinstance(item, WebElement) and 'click' in dir(item):
                        if item.is_enabled() == True and item.is_displayed() == True:
                            item.click()
                            print("click ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            elif type(div) is WebElement:
                print("catch ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                if type(div) is WebElement and 'click' in dir(div):
                    if div.is_enabled() == True and div.is_displayed() == True:
                        div.click()
                        print("click ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
                
        except KeyboardInterrupt as kiInterrupt:
            driver.close()
            driver.quit()
            break
        except TimeoutException as toutEx:
            print("timeout ytp-ad:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        except NoSuchWindowException as nswEx:
            print(nswEx)
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            break            
        except InvalidSessionIdException as isidEx:
            print(isidEx)
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            break
        except Exception as ex:
            print(ex)
            print("none clickbtn?:" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        finally:
            pass
    #end while, close and quit()
    driver.close()
    driver.quit()    
        
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        #running with indicated settings ( 1st:wait seconds, 2nd:browser)
        skipAd(int(sys.argv[1]), sys.argv[2])
    else:
        #running as default settings (chrome)
        skipAd()
