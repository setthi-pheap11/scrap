const { Builder, By, until } = require('selenium-webdriver');
const axios = require('axios');
const dotenv = require('dotenv');
const path = require('path');

// Load environment variables from .env file
dotenv.config({ path: path.resolve(__dirname, '.env') });

// Ensure OpenAI API key is loaded from environment variables
const openaiApiKey = process.env.OPENAI_API_KEY;
if (!openaiApiKey) {
    throw new Error("OPENAI_API_KEY environment variable is not set.");
}

async function formatScholarshipData(data) {
    const prompt = `Format the following scholarship details into the specified JSON structure and complete any missing information by referencing other websites:\n\nScholarship details: ${data}\n\nJSON structure:\n{
        "name": "",
        "description": "",
        "exam_detail": "",
        "ielt": "true or false",
        "minimum_ielts": "",
        "overall_ielts": "",
        "toefl": "true or false",
        "toefl_ibt_score": "",
        "toefl_pbt_score": "",
        "gpa": "",
        "ielts_condition": "Not Required or Not Specified",
        "toefl_condition": "Not Required or Not Specified",
        "gender": "Any Gender or Male and Female",
        "max_age": "",
        "experiences": "",
        "experience_detail": "",
        "sat_act": "",
        "gre_gmat": "",
        "amount": "",
        "deadline": "",
        "requirement": "",
        "benefit": "",
        "source_link": "",
        "document": "",
        "apply": "",
        "interview_detail": "",
        "days_remaining": "",
        "image_url": "",
        "thumbnail_url": "",
        "majors": "",
        "degrees": "",
        "countries": "",
        "study_modes": ""
    }`;

    try {
        const response = await axios.post('https://api.openai.com/v1/chat/completions', {
            model: "gpt-4",
            messages: [
                { role: "system", content: "You are a helpful assistant." },
                { role: "user", content: prompt }
            ],
            max_tokens: 2048,
            temperature: 0.5
        }, {
            headers: {
                'Authorization': `Bearer ${openaiApiKey}`,
                'Content-Type': 'application/json'
            }
        });

        const responseText = response.data.choices[0].message.content.trim();
        console.log("OpenAI response:", responseText); // Debugging line

        // Attempt to parse the response as JSON
        try {
            return JSON.parse(responseText);
        } catch (jsonError) {
            console.error("Failed to parse OpenAI response as JSON:", jsonError);
            console.error("OpenAI response text:", responseText);
            return null;
        }
    } catch (error) {
        console.error(`Error formatting data with OpenAI: ${error.message}`);
        return null;
    }
}

async function sendToApi(formattedData) {
    const apiUrl = "https://scholarar-dev.seksa.today/api/create-scholarships";
    const headers = { 'Content-Type': 'application/json' };

    try {
        const response = await axios.post(apiUrl, {
            status: 200,
            status_code: "success",
            message: "OK",
            data: [formattedData]
        }, { headers });

        return { statusCode: response.status, data: response.data };
    } catch (error) {
        console.error(`Error sending data to API: ${error.message}`);
        return null;
    }
}

(async () => {
    console.log("Launching browser...");

    const driver = new Builder().forBrowser('chrome').build();
    const allScholarships = new Set();

    try {
        console.log("Navigating to the website...");
        await driver.get('https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/');

        for (let pageNum = 1; pageNum <= 31; pageNum++) {
            console.log(`Processing page ${pageNum}...`);

            try {
                await driver.wait(until.elementLocated(By.className('entry')), 120000);
            } catch (error) {
                console.error(`Error waiting for scholarships on page ${pageNum}: ${error.message}`);
                break;
            }

            let scholarships = await driver.findElements(By.className('entry'));
            console.log(`Found ${scholarships.length} scholarships on page ${pageNum}.`);

            for (let i = 0; i < scholarships.length; i++) {
                let retries = 3;
                while (retries > 0) {
                    try {
                        console.log(`Processing scholarship on page ${pageNum}, index ${i}...`);

                        scholarships = await driver.findElements(By.className('entry')); // Re-fetch elements
                        const detailsLink = await scholarships[i].findElement(By.tagName('a'));
                        if (detailsLink) {
                            await detailsLink.click();

                            await driver.wait(until.elementLocated(By.className('maincontent')), 120000);
                            const details = await driver.findElement(By.className('maincontent')).getText();

                            if (!allScholarships.has(details)) {
                                allScholarships.add(details);
                            }

                            await driver.navigate().back();
                            await driver.wait(until.elementLocated(By.className('entry')), 120000);
                        }
                        break; // Exit retry loop on success
                    } catch (error) {
                        console.error(`Error processing scholarship on page ${pageNum}, index ${i}: ${error.message}`);
                        retries -= 1;
                        if (retries === 0) {
                            console.error(`Failed to process scholarship on page ${pageNum}, index ${i} after multiple attempts.`);
                        }
                    }
                }
            }

            if (pageNum < 31) {
                try {
                    const nextButton = await driver.findElement(By.linkText((pageNum + 1).toString()));
                    if (nextButton) {
                        await nextButton.click();
                        await driver.sleep(5000);  // Wait for the next page to load
                    }
                } catch (error) {
                    console.error(`Failed to navigate to page ${pageNum + 1}: ${error.message}`);
                    break;
                }
            }
        }
    } catch (error) {
        console.error(`Error navigating to the website: ${error.message}`);
    } finally {
        await driver.quit();
    }

    console.log(`Total scholarships collected: ${allScholarships.size}`);

    for (const scholarship of allScholarships) {
        try {
            const formattedScholarship = await formatScholarshipData(scholarship);
            if (formattedScholarship) {
                const { statusCode, data } = await sendToApi(formattedScholarship);
                console.log(`API Response (Status Code: ${statusCode}): ${JSON.stringify(data)}`);
            } else {
                console.log(`Failed to format scholarship data: ${scholarship}`);
            }
        } catch (error) {
            console.error(`Failed to process scholarship: ${error.message}`);
        }
    }

    console.log("All data has been scraped and sent to the API.");
})();
