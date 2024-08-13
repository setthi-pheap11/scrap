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

# openai.api_key = 'sk-proj-D2tNbpUULODyWO43uRfpT3BlbkFJoNpNdyeFxwYzIc5DyBtZ'
openai.api_key = os.getenv("OPENAI_API_KEY")

def format_scholarship_data(data):
    prompt = (
        f"Format the following scholarship details into the specified JSON structure:\n\n"
        f"Scholarship details: {data}\n\n"
        f"JSON structure:\n"
        f"{{\n"
        f'    "name": "",\n'
        f'    "description": "",\n'
        f'    "type_id": "",\n'
        f'    "exam_detail": "",\n'
        f'    "ielt": "",\n'
        f'    "minimum_ielts": "",\n'
        f'    "overall_ielts": "",\n'
        f'    "toefl": "",\n'
        f'    "toefl_ibt_score": "",\n'
        f'    "toefl_pbt_score": "",\n'
        f'    "gpa": "3.5+",\n'
        f'    "ielts_condition": "",\n'
        f'    "toefl_condition": "",\n'
        f'    "gender": "",\n'
        f'    "status": "",\n'
        f'    "max_age": "",\n'
        f'    "experiences": "",\n'
        f'    "experience_detail": "",\n'
        f'    "sat_act": "",\n'
        f'    "gre_gmat": "",\n'
        f'    "amount": "",\n'
        f'    "deadline": "",\n'
        f'    "requirement": "",\n'
        f'    "benefit": "",\n'
        f'    "source_link": "",\n'
        f'    "document": "",\n'
        f'    "apply": "",\n'
        f'    "interview_detail": "",\n'
        f'    "days_remaining": "",\n'
        f'    "updated_at": "",\n'
        f'    "created_at": "",\n'
        f'    "id": 142,\n'
        f'    "image_url": "",\n'
        f'    "thumbnail_url": "",\n'
        f'    "majors": [\n'
        f'        {{\n'
        f'            "id": "",\n'
        f'            "name": "",\n'
        f'            "pivot": {{\n'
        f'                "scholarship_id": "",\n'
        f'                "major_id": ""\n'
        f'            }}\n'
        f'        }}\n'
        f'    ],\n'
        f'    "degrees": [\n'
        f'        {{\n'
        f'            "id": "",\n'
        f'            "name": "",\n'
        f'            "image": "",\n'
        f'            "image_url": "",\n'
        f'            "pivot": {{\n'
        f'                "scholarship_id": "",\n'
        f'                "degree_id": ""\n'
        f'            }}\n'
        f'        }}\n'
        f'    ],\n'
        f'    "countries": [\n'
        f'        {{\n'
        f'            "id": "",\n'
        f'            "name": "",\n'
        f'            "image": "",\n'
        f'            "created_at": "",\n'
        f'            "updated_at": "",\n'
        f'            "image_url": "",\n'
        f'            "pivot": {{\n'
        f'                "scholarship_id": "",\n'
        f'                "country_id": ""\n'
        f'            }}\n'
        f'        }}\n'
        f'    ],\n'
        f'    "study_modes": [\n'
        f'        {{\n'
        f'            "id": "",\n'
        f'            "mode": "",\n'
        f'            "pivot": {{\n'
        f'                "scholarship_id": "",\n'
        f'                "study_mode_id": ""\n'
        f'            }}\n'
        f'        }}\n'
        f'    ]\n'
        f'}}'
    )
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.5
    )
    return json.loads(response.choices[0].text.strip())

def send_to_api(formatted_data):
    api_url = "http://127.0.0.1:8000/api/create-scholarships"
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
        status_code, response_json = send_to_api(formatted_scholarship)
        print(f"API Response (Status Code: {status_code}): {response_json}")
    except Exception as e:
        print(f"Failed to process scholarship: {e}")

# Save the collected data to a CSV file
csv_filename = "scholarshipssss3.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Details"])  # Write the header
    for scholarship in all_scholarships:
        csv_writer.writerow([scholarship])

print(f"All data has been scraped and stored in {csv_filename}.")


