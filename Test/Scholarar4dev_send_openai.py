import openai
import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException, TimeoutException
import json
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure OpenAI API key is loaded from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

def format_scholarship_data(data):
    prompt = f"Format the following scholarship details into the specified JSON structure:\n\nScholarship details: {data}\n\nJSON structure:\n{{\n    'name': '',\n    'description': '',\n    'type_id': '',\n    'exam_detail': '',\n    'ielt': '',\n    'minimum_ielts': '',\n    'overall_ielts': '',\n    'toefl': '',\n    'toefl_ibt_score': '',\n    'toefl_pbt_score': '',\n    'gpa': '3.5+',\n    'ielts_condition': '',\n    'toefl_condition': '',\n    'gender': '',\n    'status': '',\n    'max_age': '',\n    'experiences': '',\n    'experience_detail': '',\n    'sat_act': '',\n    'gre_gmat': '',\n    'amount': '',\n    'deadline': '',\n    'requirement': '',\n    'benefit': '',\n    'source_link': '',\n    'document': '',\n    'apply': '',\n    'interview_detail': '',\n    'days_remaining': '',\n    'updated_at': '',\n    'created_at': '',\n    'id': 142,\n    'image_url': '',\n    'thumbnail_url': '',\n    'majors': [\n        {{\n            'id': '',\n            'name': '',\n            'pivot': {{\n                'scholarship_id': '',\n                'major_id': ''\n            }}\n        }}\n    ],\n    'degrees': [\n        {{\n            'id': '',\n            'name': '',\n            'image': '',\n            'image_url': '',\n            'pivot': {{\n                'scholarship_id': '',\n                'degree_id': ''\n            }}\n        }}\n    ],\n    'countries': [\n        {{\n            'id': '',\n            'name': '',\n            'image': '',\n            'created_at': '',\n            'updated_at': '',\n            'image_url': '',\n            'pivot': {{\n                'scholarship_id': '',\n                'country_id': ''\n            }}\n        }}\n    ],\n    'study_modes': [\n        {{\n            'id': '',\n            'mode': '',\n            'pivot': {{\n                'scholarship_id': '',\n                'study_mode_id': ''\n            }}\n        }}\n    ]\n}}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=16384,
            temperature=0.5
        )
        return json.loads(response.choices[0].message['content'].strip())
    except Exception as e:
        print(f"Error formatting data with OpenAI: {e}")
        return None

def send_to_api(formatted_data):
    api_url = "https://scholarar-dev.seksa.today/api/create-scholarships"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json={"status": 200, "status_code": "success", "message": "OK", "data": [formatted_data]}, headers=headers)
    return response.status_code, response.json()

# Specify the path to msedgedriver.exe
PATH = r"C:\msedgedriver.exe"

# Create a Service object with the path to msedgedriver
service = Service(PATH)

# Create an Options object
options = Options()

# Initialize the Edge driver
driver = webdriver.Edge(service=service, options=options)

# Use a set to track collected scholarships to prevent duplicates
all_scholarships = set()

try:
    # Open the website
    driver.get("https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/")
    
    for page in range(1, 32):  # Loop through pages 1 to 31
        # Wait for the elements to load
        scholarships = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "entry"))
        )
        
        for index in range(len(scholarships)):
            retry_count = 0
            max_retries = 3
            while retry_count < max_retries:
                try:
                    # Re-fetch scholarships to avoid stale element reference
                    scholarships = WebDriverWait(driver, 60).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "entry"))
                    )
                    # Click on the scholarship entry
                    scholarship_link = scholarships[index].find_element(By.TAG_NAME, 'a')
                    scholarship_link.click()
                    
                    # Wait for the detailed page to load and collect the detailed information
                    details = WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "maincontent"))
                    )
                    details_text = details.text
                    
                    # Add the details to the set
                    if details_text not in all_scholarships:
                        all_scholarships.add(details_text)
                    
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

# Format and send each scholarship data to OpenAI and then to your API
for scholarship in all_scholarships:
    try:
        formatted_scholarship = format_scholarship_data(scholarship)
        if formatted_scholarship:
            status_code, response_json = send_to_api(formatted_scholarship)
            print(f"API Response (Status Code: {status_code}): {response_json}")
        else:
            print(f"Failed to format scholarship data: {scholarship}")
    except Exception as e:
        print(f"Failed to process scholarship: {e}")

# Save the collected data to a CSV file
csv_filename = "scholarships.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Details"])  # Write the header
    for scholarship in all_scholarships:
        csv_writer.writerow([scholarship])

print(f"All data has been scraped and stored in {csv_filename}.")
