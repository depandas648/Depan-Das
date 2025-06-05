from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Amazon URL
url = "https://www.amazon.in/s?bbn=81107433031&rh=n%3A81107433031%2Cp_85%3A10440599031&ref=pd_hp_d_atf_unk"
driver.get(url)

# Let the page load
time.sleep(5)

# Extract product titles
products = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")

for index, product in enumerate(products[:10]):
    print(f"{index + 1}. {product.text}")

driver.quit()
