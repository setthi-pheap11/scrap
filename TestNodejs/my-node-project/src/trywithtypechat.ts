import { Builder, By, until, WebDriver } from 'selenium-webdriver';
import dotenv from 'dotenv';
import path from 'path';
import * as typechat from 'typechat';
import { scholarshipSchemaValidator } from './scholarshipValidator';
import * as fs from 'fs';
import axios from 'axios';
dotenv.config();



// Load environment variables from .env file
// dotenv.config({ path: path.resolve(__dirname, '.env') });

// Ensure OpenAI API key is loaded from environment variables
const openaiApiKey = process.env.OPENAI_API_KEY;
if (!openaiApiKey) {
    throw new Error("OPENAI_API_KEY environment variable is not set.");
}

// Interface for scholarship response
interface ScholarshipResponse {
    name: string;
    description: string;
    type_id: string;
    exam_detail: string;
    ielt: boolean;
    minimum_ielts: string;
    overall_ielts: string;
    toefl: boolean;
    toefl_ibt_score: string;
    toefl_pbt_score: string;
    gpa: string;
    ielts_condition: string;
    toefl_condition: string;
    gender: string;
    status: string;
    max_age: number | null;
    experiences: string;
    experience_detail: string;
    sat_act: string;
    gre_gmat: string;
    amount: string;
    deadline: string;
    requirement: string;
    benefit: string;
    source_link: string;
    document: string;
    apply: string;
    interview_detail: string;
    days_remaining: string;
    id: number | null;
    image_url: string;
    thumbnail_url: string;
    majors: string[];
    degrees: string[];
    countries: string[];
    study_modes: string[];
}

// Create a TypeChat language model and translator
const model = typechat.createLanguageModel({ apiKey: openaiApiKey });
const translator = typechat.createJsonTranslator<ScholarshipResponse>(model, scholarshipSchemaValidator);

async function formatScholarshipData(data: string): Promise<ScholarshipResponse | null> {
    const prompt = `Format the following scholarship details into the specified JSON structure and complete any missing information by referencing other websites:\n\nScholarship details: ${data}`;

    try {
        const response = await translator.translate(prompt);
        if (!response.success) {
            console.error(response.message);
            return null;
        }

        // Ensure max_age is an integer
        if (response.data.max_age && isNaN(response.data.max_age)) {
            response.data.max_age = parseInt(response.data.max_age.toString(), 10);
        }

        return response.data;
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Error formatting data with TypeChat: ${error.message}`);
        } else {
            console.error('An unknown error occurred while formatting scholarship data.');
        }
        return null;
    }
}

async function sendToApi(formattedData: ScholarshipResponse) {
    const apiUrl = "https://dev-portal.scholarar.com/api/create-scholarships";
    const headers = { 'Content-Type': 'application/json' };

    console.log("Sending data to API:", JSON.stringify({ scholarships: [formattedData] }, null, 2));

    try {
        const response = await axios.post(apiUrl, { scholarships: [formattedData] }, { headers });
        return { statusCode: response.status, data: response.data };
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Error sending data to API: ${error.message}`);
            if (axios.isAxiosError(error) && error.response) {
                console.error(`API response status: ${error.response.status}`);
                console.error(`API response data: ${JSON.stringify(error.response.data)}`);
            }
        } else {
            console.error('An unknown error occurred while sending data to the API.');
        }
        return null;
    }
}

(async () => {
    console.log("Launching browser...");

    const driver: WebDriver = await new Builder().forBrowser('chrome').build();
    const allScholarships = new Set<string>();

    try {
        console.log("Navigating to the website...");
        await driver.get('https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/');

        for (let pageNum = 1; pageNum <= 31; pageNum++) {
            console.log(`Processing page ${pageNum}...`);

            try {
                await driver.wait(until.elementLocated(By.className('entry')), 120000);
            } catch (error) {
                if (error instanceof Error) {
                    console.error(`Error waiting for scholarships on page ${pageNum}: ${error.message}`);
                } else {
                    console.error('An unknown error occurred while waiting for scholarships.');
                }
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
                        if (error instanceof Error) {
                            console.error(`Error processing scholarship on page ${pageNum}, index ${i}: ${error.message}`);
                        } else {
                            console.error('An unknown error occurred while processing the scholarship.');
                        }
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
                    if (error instanceof Error) {
                        console.error(`Failed to navigate to page ${pageNum + 1}: ${error.message}`);
                    } else {
                        console.error('An unknown error occurred while navigating to the next page.');
                    }
                    break;
                }
            }
        }
    } catch (error) {
        if (error instanceof Error) {
            console.error(`Error navigating to the website: ${error.message}`);
        } else {
            console.error('An unknown error occurred while navigating to the website.');
        }
    } finally {
        await driver.quit();
    }

    console.log(`Total scholarships collected: ${allScholarships.size}`);

    for (const scholarship of allScholarships) {
        try {
            const formattedScholarship = await formatScholarshipData(scholarship);
            if (formattedScholarship) {
                const result = await sendToApi(formattedScholarship);
                if (result) {
                    const { statusCode, data } = result;
                    console.log(`API Response (Status Code: ${statusCode}): ${JSON.stringify(data)}`);
                } else {
                    console.log(`Failed to send scholarship data to API: ${scholarship}`);
                }
            } else {
                console.log(`Failed to format scholarship data: ${scholarship}`);
            }
        } catch (error) {
            if (error instanceof Error) {
                console.error(`Failed to process scholarship: ${error.message}`);
            } else {
                console.error('An unknown error occurred while processing the scholarship.');
            }
        }
    }

    console.log("All data has been scraped and sent to the API.");
})();
