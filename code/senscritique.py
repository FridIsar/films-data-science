# python package
import csv
import time
import random
import codecs
import sys
import importlib

# selenium package
from imp import reload

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

# format utf-8


# fonction pause
def pause():
    time_break = random.randint(1,2)
    return time.sleep(time_break)


# options
options = webdriver.ChromeOptions()
capa = DesiredCapabilities.CHROME
options.add_argument("--kiosk")
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(r"C:\Users\PC\Downloads\chromedriver_win32\chromedriver.exe")
wait = WebDriverWait(driver, 30)
pause()
print("open driver")
# url de depart
senscrit_url = "https://www.senscritique.com/films/tops/top100-des-top10"

# aller sur senscritique
driver.get(senscrit_url)
images = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "img.lazy"))
            )
print("connected")

# scroll down smoothly
scheight = .1
while scheight < 1.0:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
    scheight += .2
    pause()

# ouvrir csv
with codecs.open('../datasets/senscritique_liste.csv', 'w') as csvfile:
    fieldnames = ['Titre', 'Director', 'Date', 'Rang', 'Note']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=",")
    writer.writeheader()

    # prendre infos
    items = driver.find_elements_by_css_selector("li.elto-item")

    # boucle
    for item in items:

        # scroll smoothly
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});",
            item)

        # title
        try:
            title = item.find_element_by_css_selector("a.elco-anchor").text
        except NoSuchElementException:
            title = ''
            pass

        # type
        try:
            director = item.find_element_by_css_selector("span.elco-baseline-a").text
        except NoSuchElementException:
            director = ''
            pass

        # date
        try:
            date = item.find_element_by_css_selector("span.elco-date").text
            date.replace('(', '').replace(')', '')
        except NoSuchElementException:
            date = ''
            pass

        # rank
        try:
            rank = item.find_element_by_css_selector("span.elto-rank-item").text
        except NoSuchElementException:
            rank = ''
            pass

        # grade
        try:
            grade = item.find_element_by_css_selector("a.erra-global").text
        except NoSuchElementException:
            grade = ''
            pass

        # write csv
        writer.writerow({'Titre': title, 'Director': director, 'Date': date, 'Rang': rank, 'Note': grade})

        print("✓ %s" % title)

# end
print("end")
driver.close()