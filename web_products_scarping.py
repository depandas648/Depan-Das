from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup WebDriver (Example: Chrome)
driver = webdriver.Chrome()  # Make sure chromedriver is in PATH

# Open the cart page
driver.get("https://www.vedantcomputers.com/pc-components/processor")
time.sleep(5)  # Let the page load

# Get cart rows
cart_items = driver.find_elements(By.CSS_SELECTOR, "table.table-bordered tbody tr")

data = []
for item in cart_items:
    cols = item.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 4:
        product = cols[0].text.strip()
        model = cols[1].text.strip()
        quantity = cols[2].text.strip()
        price = cols[3].text.strip()
        data.append([product, model, quantity, price])

# Create DataFrame and export to Excel
df = pd.DataFrame(data, columns=["Product", "Price"])
df.to_excel("vedant_cart.xlsx", index=False)

print("Cart data exported to dip.xlsx")

driver.quit()
