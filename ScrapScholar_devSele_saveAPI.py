import csv
import mysql.connector
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException, TimeoutException

# Specify the path to msedgedriver.exe
PATH = r"C:\msedgedriver.exe"

# Create a Service object with the path to msedgedriver
service = Service(PATH)

# Create an Options object
options = Options()

# Initialize the Edge driver
driver = webdriver.Edge(service=service, options=options)

all_scholarships = []

try:
    # Open the website
    driver.get("https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/")
    
    for page in range(1, 32):  # Loop through pages 1 to 31
        # Wait for the elements to load
        scholarships = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "entry"))
        )
        
        print(f"Page {page}: Found {len(scholarships)} scholarships")
       
        for index in range(len(scholarships)):
            retry_count = 0
            max_retries = 3
            while retry_count < max_retries:
                try:
                    # Re-fetch scholarships to avoid stale element reference
                    scholarships = WebDriverWait(driver, 60).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "entry"))
                    )
                    
                    # Check if scholarships list is empty
                    if len(scholarships) == 0:
                        print(f"No scholarships found on page {page}")
                        break
                    #TAG_NAME, 'a'

                    # Click on the scholarship entry
                    scholarship_link = scholarships[index].find_element(By.TAG_NAME, 'a')
                    scholarship_link.click()
                  
                    # Wait for the detailed page to load and collect the detailed information
                    details = WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "maincontent"))
                    )

                    name = details.find_element(By.XPATH, '//*[@id="post-1002"]/h1').text
                    last_update = details.find_element(By.XPATH, '//*[@id="post-1002"]/p').text
                    degree = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/div[1]/p').text
                    deadline = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/div[2]/p[1]').text
                    study = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/div[2]/p[2]').text
                    course = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/div[2]/p[3]').text
                    brief_description = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[5]').text
                    host_institution = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[7]').text
                    number_of_scholarships = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[12]').text
                    target_group = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[14]').text
                    scholarship_value = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[16]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[17]').text
                    eligibility = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[19]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[20]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[21]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[23]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[24]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[25]').text
                    application_instructions = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[27]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[28]').text
                    website = details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[30]').text + details.find_element(By.XPATH, '//*[@id="post-1002"]/div/p[31]').text

                    scholarship_data = {
                        "name": name,
                        "last_update": last_update,
                        "degree": degree,
                        "deadline": deadline,
                        "study": study,
                        "course": course,
                        "brief_description": brief_description,
                        "host_institution": host_institution,
                        "number_of_scholarships": number_of_scholarships,
                        "target_group": target_group,
                        "scholarship_value": scholarship_value,
                        "eligibility": eligibility,
                        "application_instructions": application_instructions,
                        "website": website
                    }
                    all_scholarships.append(scholarship_data)

                    # Go back to the list page
                    driver.back()
                    
                    # Wait for the list page to load again
                    WebDriverWait(driver, 60).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "entry"))
                    )
                    break  # Exit the retry loop if successful
                
                except (StaleElementReferenceException, NoSuchElementException, NoSuchWindowException, TimeoutException) as e:
                    retry_count += 1
                    print(f"Retry {retry_count}/{max_retries} for scholarship at index {index} on page {page}: {e}")
                    if retry_count >= max_retries:
                        print(f"Failed to process scholarship at index {index} on page {page} after {max_retries} retries")
                        break

        # Check if there's a next page button, go to next page
        if page < 31:
            try:
                next_button = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.LINK_TEXT, str(page + 1)))
                )
                next_button.click()
                time.sleep(5)  # Wait for the next page to load
            except Exception as e:
                print(f"Failed to navigate to page {page + 1}: {e}") 
                break
finally:
    # Quit the driver
    driver.quit()

# Print the total number of scholarships collected
print(f"Total scholarships collected: {len(all_scholarships)}")

# Save the collected data to a CSV file
csv_filename = "scholarships.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=all_scholarships[0].keys() if all_scholarships else [])
    csv_writer.writeheader()
    csv_writer.writerows(all_scholarships)

print(f"All data has been scraped and stored in {csv_filename}.")
