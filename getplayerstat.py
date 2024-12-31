from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()  

try:
    url = "https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1&Season=2024-25"
    driver.get(url)

    wait = WebDriverWait(driver, 15)
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Crom_body__UYOcU")))

    # Find table headers
    headers = driver.find_elements(By.CSS_SELECTOR, "thead tr th")
    header_names = [header.text.strip() for header in headers]

    # Find table rows
    rows = driver.find_elements(By.CSS_SELECTOR, "tbody.Crom_body__UYOcU tr")

    # Extract data from each row
    table_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells]
        if row_data:  # Skip empty rows
            table_data.append(row_data)

    # Convert to a DataFrame
    df = pd.DataFrame(table_data, columns=header_names[:len(table_data[0])])  # Adjusting header length
    print(df)

    # Save to CSV (optional)
    df.to_csv("nba_playerstats_2024-2025.csv", index=False)
    print("Table data saved to nba_player_stats.csv")

finally:

    driver.quit()
