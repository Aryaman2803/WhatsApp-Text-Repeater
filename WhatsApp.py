from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


name = input('Enter the name of user  :')
msg = input("Enter your message : ")


count = int(input("Enter the count : "))
input("Enter anything after scanning the QR code of WhatsApp ")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

"""Enter the class container value(Check HTML and Xpath for more info) of the person name.
Open WhatsApp Web and Inspect the user name."""
msg_box = driver.find_element_by_class_name('')

for i in range(count):
    msg_box.send_keys(msg)
    """Find the class name of the text box so that it can pass the input message to it.
        Find it by inspecting the Text Box of WhatsApp Web"""
    button = driver.find_element_by_class_name('')
    button.click()

    
