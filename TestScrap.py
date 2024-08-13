from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

url = 'https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/'
driver = webdriver.Edge()
driver.get(url)

all_scholarships = []

try:
    for page in range(1, 32):  # Loop through pages 1 to 31
        # Find elements by class name
        scholarships = driver.find_elements(By.CLASS_NAME, 'entry')

        # Click each scholarship entry
        for index in range(len(scholarships)):
            try:
                # Re-fetch scholarships to avoid stale element reference
                scholarships = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'entry'))
                )
                
                # Click on the scholarship entry
                scholarships[index].find_element(By.TAG_NAME, 'a').click()
                
                # Wait for the detailed page to load and collect the detailed information
                details = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'maincontent'))
                )

                title = details.find_element(By.XPATH, './/h1').text
                link = driver.current_url
                
                

                all_scholarships.append({
                    'title': title,
                    'link': link,
                    
                })
                print(f"Title: {title}\nLink: {link}\n")

                # Go back to the list page
                driver.back()
                
                # Wait for the list page to load again
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'entry'))
                )
            except Exception as e:
                print(f"Error extracting scholarship details at index {index} on page {page}: {e}")

        # Check if there's a next page button, go to next page
        if page < 31:
            try:
                next_button = WebDriverWait(driver, 60).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, str(page + 1)))
                )
                next_button.click()
                time.sleep(5)  # Wait for the next page to load
            except Exception as e:
                print(f"Failed to navigate to page {page + 1}: {e}") 
                break
finally:
    # Close the driver
    driver.quit()

# Print the total number of scholarships collected
print(f"Total scholarships collected: {len(all_scholarships)}")

# Save the collected data to a CSV file
csv_filename = "scholarships.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=['title', 'link','eligible'])
    csv_writer.writeheader()
    csv_writer.writerows(all_scholarships)

print(f"All data has been scraped and stored in {csv_filename}.")
