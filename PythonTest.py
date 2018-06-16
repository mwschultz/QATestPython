#Matt Schultz
#Test automatic log in using Selenium for Google Chrome. Uses the https://twitter.com/login as of 11/6/2017


from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

#Pass a login and password
def log_in():
    print("This simple script will check if you have logged in via the supplied user name and password.")
    username = input("Enter your Twitter username:")
    password = input("Enter your Twitter password:")
    driver = webdriver.Chrome('chrome/chromedriver') #Chromedriver is located in the chrome folder. Must maintain the same folder structure.

    driver.get("https://twitter.com/login") #get the Twitter log in page
    #print (driver.current_url)

    email_field = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
    email_field.clear() #clear field in case there is something else already there
    #email_field.send_keys("user@example.com")
    email_field.send_keys(username)

    password_field = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
    password_field.clear() #clear field
    password_field.send_keys(password)

    sign_in = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button") #grab button
    sign_in.click() #click button


    print ("Trying to login with username:",username, "password: password not displayed for security") #let user know the attempted log in password and user name

    #print (driver.current_url)
    if driver.current_url == "https://twitter.com/": #check to see if they have logged in (transitioned from log-in page to Twitter)
        print("Logged in -- you are on Twitter.com")
    else:
        print("Not logged in -- either e-mail or password were invalid")

log_in() #call the method
