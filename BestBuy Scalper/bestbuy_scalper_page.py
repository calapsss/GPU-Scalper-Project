import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#This scalper refreshes the page every day. When the item becomes available, it checks out the item.
#V_1 Account Checkout Automation

def initialize_chromedriver():
    PATH = r"C:\Users\C24Charles.Calapini\chromedriver.exe"
    options = webdriver.ChromeOptions()
    #options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    global driver
    driver = webdriver.Chrome(options=options, executable_path=PATH)

#This next function is only for my current dev environment. My current chrome settings is not compatible with chromdriver binaries. Thus, I made a work around to leave the
#tabs running after all tasked are finished.
#
def leave_tabs_open():
    time.sleep(3600)
    driver.quit()


def scalping_session():
    
    #Account Test details --- (separate function must bemade to import details) (profile will be a class or multi dimensional arraay future versions will be made.=)
    email = "youremail@gmail.com"
    password = "your"
    #billing profile a class will soon be made
    


    product_link = "https://www.bestbuy.com/site/pny-xlr8-gaming-single-fan-nvidia-geforce-gtx-1660-super-overclocked-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6407309.p?skuId=6407309"
    cart_link = "https://www.bestbuy.com/cart"
    driver.get(product_link)
    time.sleep(3)
    addToCart_xpath = r"/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[13]/div[2]/div/div/div/button"
    addToCart_class = "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"
    time.sleep(2)
    xpath_failed = False
    try:
        driver.find_element_by_xpath(addToCart_xpath)\
            .click()
    except:
        print("Add to Cart - Xpath - Not working\n")
        xpath_failed = True

    if xpath_failed:
        driver.find_element_by_class_name(addToCart_class)\
            .click()

    


    #try pop-up 
    popup_failed = False
    try:
        time.sleep(2)
        cart_popUp_xpath = r"/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a"
        driver.find_element_by_xpath(cart_popUp_xpath)\
            .click()
    except:
        print("Pop up - Xpath - Not working\n")
        popup_failed = True


    #clicks cart instead
    if popup_failed:
        driver.get(cart_link)



    #CHECKOUT

    #Clicks button
    checkoutButton_xpath = r"/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button"
    time.sleep(2)
    driver.find_element_by_xpath(checkoutButton_xpath)\
        .click()
    
    #Login details
    email_Field_id = "fld-e"
    pass_Field_id = "fld-p1"
    time.sleep(5)
    driver.find_element_by_id(email_Field_id)\
        .send_keys(email)
    driver.find_element_by_id(pass_Field_id)\
        .send_keys(password)
    
    login_submit_xpath = r"/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[3]/button"
    driver.find_elements_by_xpath(login_submit_xpath)\
        .click()

    
    
    


    



    








initialize_chromedriver()

scalping_session()

leave_tabs_open()





