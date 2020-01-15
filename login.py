# import selenium
import os
import time
import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def arg_parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('username', type=str, help='login user name')
    parser.add_argument('password', type=str, help='login password')
    parser.add_argument('-q', '--quiet', help='(option) do not show browser', action='store_true')
    args = parser.parse_args()

    return args

def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def login(driver, username, password):
    # Open the website
    driver.get('http://rs01.guc-asic.com/Citrix/XenApp/auth/login.aspx')
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "downloadButtonImg")))
    driver.get('http://rs01.guc-asic.com/Citrix/XenApp/auth/login.aspx')

    # Select the id box
    id_box = driver.find_element_by_id('user')
    id_box.send_keys(username)

    # Find password box
    pass_box = driver.find_element_by_id('password')
    pass_box.send_keys(password)

    # Find login button Click login
    login_button = driver.find_element_by_id('btnLogin')
    login_button.click()

    download_id = "idCitrix.MPS.App.GUC_005fXenApp.linux238_005f3"
    WebDriverWait(driver, 1).until(expected_conditions.presence_of_element_located((By.ID, download_id)))
    download_icon = driver.find_element_by_id(download_id)
    download_icon.click()

    while not os.path.isfile('/tmp/launch.ica'):
        time.sleep(1)

def main():
    args = arg_parse()

    options = Options()

    # do not show browser if set -q flag
    if args.quiet:
        options.add_argument('--headless')

    # Using Chrome to access web
    driver = webdriver.Chrome(options=options)

    # Download path
    enable_download_headless(driver, '/tmp')

    try:
        username, password = args.username, args.password
        print("Login to the VNC by username %s and password %s" %
                (username, password))
        login(driver, username, password)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()

