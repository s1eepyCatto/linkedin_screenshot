# This program goes into my linkedin account and saves a snapshot everyday 
# make sure selenium is installed 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

secretUsername = "WHOCOULDTHISBE" # change to your username
secretPassword = "SUPERSECRET" # change to your password

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

# LOGIN
username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys(secretUsername)

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys(secretPassword)

password.send_keys(Keys.RETURN)
assert "not a Robot" not in driver.page_source
driver.get("https://www.linkedin.com/in/yourprofileurl/") # Change this to your profile url

time.sleep(10)

# SAVE SNAPSHOT OF MY PROFILE
html_content = driver.page_source
filename = "linkedin_snapshot_" + str(int(time.time())) + ".mhtml"

# use chrome devtools; credits to some stackoverflow guy
res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
with open(filename, 'w', newline='') as f:   
    f.write(res['data'])

time.sleep(10)

driver.close()

