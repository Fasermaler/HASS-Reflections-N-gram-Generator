from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

# Login Credentials
f = open("login_credentials.txt", "r")
credentials = f.read().splitlines()
f.close()

login_email = credentials[0]
login_password = credentials[1]



driver = webdriver.Firefox()

start_time = time.time()



def site_login():
		print("\n[INFO] Logging in")
		driver.get("https://www.facebook.com")
		driver.find_element_by_id("email").send_keys(login_email)
		driver.find_element_by_id("pass").send_keys(login_password)
		driver.find_element_by_id("loginbutton").click()
		# WebDriverWait(driver, 10).until(EC.title_contains("home"))
		driver.implicitly_wait(300)


def scroll_to_end():
	SCROLL_PAUSE_TIME = 3
	print("[INFO] Scrolling Page")

	# Get scroll height
	# I would use document.Body.scrollHeight but it has a bug where it does
	# not work on pages lik Facebook and Youtube
	last_height = driver.execute_script("return document.documentElement.scrollHeight")

	# At times Facebook will load a black veil for some reason to conceal elements
	# This bit of code is to click it away
	if last_height < 4000:
		driver.find_element_by_class_name("_3ixn").click()

	while True:
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)
		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height

def click_view_more():
	numposts = len(driver.find_elements_by_css_selector("[id*=mall_post]"))
	print("There are " + str(numposts) + " posts")

	# Tip: Use ChroBug to find the relative xpaths
	numbtns = len(driver.find_elements_by_xpath("//a[@class='_4sxc _42ft']"))
	print("There are " + str(numbtns) + " posts with many comments")
	print("[INFO] Unpacking posts")
	for i in range(numbtns*2 - 1):
		driver.find_elements_by_xpath("//a[@class='_4sxc _42ft']")[0].click()
		# print("Unpacked a post")

def click_comments():
	numcomments = len(driver.find_elements_by_xpath("//a[@class='_5v47 fss'][contains(text(),'See More')]"))
	print("There are " + str(numcomments) + " long form comments")
	print("[INFO] Unpacking comments")
	for i in range(numcomments):
		driver.find_elements_by_xpath("//a[@class='_5v47 fss'][contains(text(),'See More')]")[0].click()

site_login()


driver.get("https://www.facebook.com/groups/2340846329564248/")
driver.implicitly_wait(1000)

scroll_to_end()

click_view_more()
click_comments()

end_time = time.time()
elapsed_time = end_time - start_time

print("[INFO] Completed unpacking webpage in " + str(elapsed_time // 60) + " minutes and " + str(elapsed_time % 60) + " seconds")




# driver.find_element_by_id("loginbutton").click()
