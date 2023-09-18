from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# executable_path='C:\\Users\\Apurv\\Downloads\\chromedriver_win32\\chromedriver'
# Initialize the WebDriver
driver = webdriver.Chrome()

driver.get("https://www.bt.com/")

try:
    cookie_popup = driver.find_element(By.XPATH, "//button[contains(text(),'Accept cookies')]")
    if cookie_popup.is_displayed():
        cookie_popup.click()
except:
    pass

mobile_menu = driver.find_element(By.XPATH, "//span[text()='Mobile']")
ActionChains(driver).move_to_element(mobile_menu).perform()

mobile_phones_option = driver.find_element(By.XPATH, "//a[text()='Mobile phones']")
mobile_phones_option.click()

banners = driver.find_elements(By.XPATH, "//div[contains(@class,'slider-container')]//div[contains(@class,'slide')]")
if len(banners) < 3:
    print("Error: The number of banners is less than 3")
else:
    print("Number of banners is sufficient")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
view_sim_deals_button = driver.find_element(By.XPATH, "//a[text()='View SIM only deals']")
view_sim_deals_button.click()

new_page_title = driver.title
if "SIM Only Deals" in new_page_title:
    print("Title validated: " + new_page_title)
else:
    print("Error: Title validation failed")

plan_details = driver.find_element(By.XPATH, "//strong[text()='30% off and double data']")
if "125GB 250GB Essential Plan, was £27 £18.90 per month" in plan_details.text:
    print("Plan details validated: " + plan_details.text)
else:
    print("Error: Plan details validation failed")

driver.quit()
