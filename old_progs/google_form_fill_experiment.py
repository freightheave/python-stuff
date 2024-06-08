import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

i=1

while i<=50:
    browser = webdriver.Firefox()
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSe06NAGaFWI88qVPwbhaJGj94Vz4NbwIeECAGs6QXYTwf4OHg/viewform?vc=0&c=0&w=1')
    assert 'Contact information' in browser.title

    var1_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var1_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var1_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var1_1, var1_2, var1_3])).click()  #Choose a random option from Q1
    time.sleep(random.randint(1,2)+random.random())

    var2_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var2_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var2_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var2_1, var2_2, var2_3])).click()  #Choose a random option from Q2
    time.sleep(random.randint(1,2)+random.random())

    var3_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var3_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var3_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
    var3_4 = '/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var3_1, var3_2, var3_3])).click()  #Choose a random option from Q3
    time.sleep(random.randint(1,2)+random.random())

    var4_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var4_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var4_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
    var4_4 = '/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var4_1, var4_2, var4_3,var4_4])).click()  #Choose a random option from Q4
    time.sleep(random.randint(1,2)+random.random())

    var5_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var5_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var5_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
    var5_4 = '/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var5_1, var5_2, var5_3, var5_4])).click()  #Choose a random option from Q5
    time.sleep(random.randint(1,2)+random.random())

    var6_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div'
    var6_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div'
    var6_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div'
    var6_4 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div'
    var6_5 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div'
    var6_6 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div'
    var6_7 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div'
    var6_8 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div'
    var6_9 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div'
    var6_10 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div'
    var6_11 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div'
    var6_12 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[6]/span/div[5]/div/div/div[3]/div'
    var6_13 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div'
    var6_14 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div'
    var6_15 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[8]/span/div[4]/div/div/div[3]/div'
    var6_16 = '/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/div[1]/div/div[8]/span/div[5]/div/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var6_1, var6_2, var6_3, var6_4])).click()  #Choose a random option from Q6
    time.sleep(random.randint(1,2)+random.random())
    elem = browser.find_element_by_xpath(random.choice([var6_5, var6_6, var6_7, var6_8])).click()
    time.sleep(random.randint(1,2)+random.random())
    elem = browser.find_element_by_xpath(random.choice([var6_9, var6_10, var6_11, var6_12])).click()
    time.sleep(random.randint(1,2)+random.random())
    elem = browser.find_element_by_xpath(random.choice([var6_13, var6_14, var6_15, var6_16])).click()
    time.sleep(random.randint(1,2)+random.random())


    var7_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var7_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'


    elem = browser.find_element_by_xpath(random.choice([var7_1, var7_2])).click()  #Choose a random option from Q7
    time.sleep(random.randint(1,2)+random.random())

    var8_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var8_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var8_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
    var8_4 = '/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var8_1, var8_2, var8_3, var8_4])).click()  #Choose a random option from Q8
    time.sleep(random.randint(1,2)+random.random())

    var9_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var9_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var9_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var9_1, var9_2, var9_3])).click()  #Choose a random option from Q9
    time.sleep(random.randint(1,2)+random.random())

    var10_1 = '/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
    var10_2 = '/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
    var10_3 = '/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
    var10_4 = '/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

    elem = browser.find_element_by_xpath(random.choice([var10_1, var10_2, var10_3, var10_4])).click()  #Choose a random option from Q10
    time.sleep(random.randint(1,2)+random.random())

    elem = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div/div/div/span').click() #Clicks on submit
    
    browser.quit()

    i=i+1

