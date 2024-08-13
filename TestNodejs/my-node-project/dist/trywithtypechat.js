"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const selenium_webdriver_1 = require("selenium-webdriver");
const dotenv_1 = __importDefault(require("dotenv"));
const typechat = __importStar(require("typechat"));
const scholarshipValidator_1 = require("./scholarshipValidator");
const axios_1 = __importDefault(require("axios"));
dotenv_1.default.config();
// Load environment variables from .env file
// dotenv.config({ path: path.resolve(__dirname, '.env') });
// Ensure OpenAI API key is loaded from environment variables
const openaiApiKey = process.env.OPENAI_API_KEY;
if (!openaiApiKey) {
    throw new Error("OPENAI_API_KEY environment variable is not set.");
}
// Create a TypeChat language model and translator
const model = typechat.createLanguageModel({ apiKey: openaiApiKey });
const translator = typechat.createJsonTranslator(model, scholarshipValidator_1.scholarshipSchemaValidator);
function formatScholarshipData(data) {
    return __awaiter(this, void 0, void 0, function* () {
        const prompt = `Format the following scholarship details into the specified JSON structure and complete any missing information by referencing other websites:\n\nScholarship details: ${data}`;
        try {
            const response = yield translator.translate(prompt);
            if (!response.success) {
                console.error(response.message);
                return null;
            }
            // Ensure max_age is an integer
            if (response.data.max_age && isNaN(response.data.max_age)) {
                response.data.max_age = parseInt(response.data.max_age.toString(), 10);
            }
            return response.data;
        }
        catch (error) {
            if (error instanceof Error) {
                console.error(`Error formatting data with TypeChat: ${error.message}`);
            }
            else {
                console.error('An unknown error occurred while formatting scholarship data.');
            }
            return null;
        }
    });
}
function sendToApi(formattedData) {
    return __awaiter(this, void 0, void 0, function* () {
        const apiUrl = "https://dev-portal.scholarar.com/api/create-scholarships";
        const headers = { 'Content-Type': 'application/json' };
        console.log("Sending data to API:", JSON.stringify({ scholarships: [formattedData] }, null, 2));
        try {
            const response = yield axios_1.default.post(apiUrl, { scholarships: [formattedData] }, { headers });
            return { statusCode: response.status, data: response.data };
        }
        catch (error) {
            if (error instanceof Error) {
                console.error(`Error sending data to API: ${error.message}`);
                if (axios_1.default.isAxiosError(error) && error.response) {
                    console.error(`API response status: ${error.response.status}`);
                    console.error(`API response data: ${JSON.stringify(error.response.data)}`);
                }
            }
            else {
                console.error('An unknown error occurred while sending data to the API.');
            }
            return null;
        }
    });
}
(() => __awaiter(void 0, void 0, void 0, function* () {
    console.log("Launching browser...");
    const driver = yield new selenium_webdriver_1.Builder().forBrowser('chrome').build();
    const allScholarships = new Set();
    try {
        console.log("Navigating to the website...");
        yield driver.get('https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/');
        for (let pageNum = 1; pageNum <= 31; pageNum++) {
            console.log(`Processing page ${pageNum}...`);
            try {
                yield driver.wait(selenium_webdriver_1.until.elementLocated(selenium_webdriver_1.By.className('entry')), 120000);
            }
            catch (error) {
                if (error instanceof Error) {
                    console.error(`Error waiting for scholarships on page ${pageNum}: ${error.message}`);
                }
                else {
                    console.error('An unknown error occurred while waiting for scholarships.');
                }
                break;
            }
            let scholarships = yield driver.findElements(selenium_webdriver_1.By.className('entry'));
            console.log(`Found ${scholarships.length} scholarships on page ${pageNum}.`);
            for (let i = 0; i < scholarships.length; i++) {
                let retries = 3;
                while (retries > 0) {
                    try {
                        console.log(`Processing scholarship on page ${pageNum}, index ${i}...`);
                        scholarships = yield driver.findElements(selenium_webdriver_1.By.className('entry')); // Re-fetch elements
                        const detailsLink = yield scholarships[i].findElement(selenium_webdriver_1.By.tagName('a'));
                        if (detailsLink) {
                            yield detailsLink.click();
                            yield driver.wait(selenium_webdriver_1.until.elementLocated(selenium_webdriver_1.By.className('maincontent')), 120000);
                            const details = yield driver.findElement(selenium_webdriver_1.By.className('maincontent')).getText();
                            if (!allScholarships.has(details)) {
                                allScholarships.add(details);
                            }
                            yield driver.navigate().back();
                            yield driver.wait(selenium_webdriver_1.until.elementLocated(selenium_webdriver_1.By.className('entry')), 120000);
                        }
                        break; // Exit retry loop on success
                    }
                    catch (error) {
                        if (error instanceof Error) {
                            console.error(`Error processing scholarship on page ${pageNum}, index ${i}: ${error.message}`);
                        }
                        else {
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
                    const nextButton = yield driver.findElement(selenium_webdriver_1.By.linkText((pageNum + 1).toString()));
                    if (nextButton) {
                        yield nextButton.click();
                        yield driver.sleep(5000); // Wait for the next page to load
                    }
                }
                catch (error) {
                    if (error instanceof Error) {
                        console.error(`Failed to navigate to page ${pageNum + 1}: ${error.message}`);
                    }
                    else {
                        console.error('An unknown error occurred while navigating to the next page.');
                    }
                    break;
                }
            }
        }
    }
    catch (error) {
        if (error instanceof Error) {
            console.error(`Error navigating to the website: ${error.message}`);
        }
        else {
            console.error('An unknown error occurred while navigating to the website.');
        }
    }
    finally {
        yield driver.quit();
    }
    console.log(`Total scholarships collected: ${allScholarships.size}`);
    for (const scholarship of allScholarships) {
        try {
            const formattedScholarship = yield formatScholarshipData(scholarship);
            if (formattedScholarship) {
                const result = yield sendToApi(formattedScholarship);
                if (result) {
                    const { statusCode, data } = result;
                    console.log(`API Response (Status Code: ${statusCode}): ${JSON.stringify(data)}`);
                }
                else {
                    console.log(`Failed to send scholarship data to API: ${scholarship}`);
                }
            }
            else {
                console.log(`Failed to format scholarship data: ${scholarship}`);
            }
        }
        catch (error) {
            if (error instanceof Error) {
                console.error(`Failed to process scholarship: ${error.message}`);
            }
            else {
                console.error('An unknown error occurred while processing the scholarship.');
            }
        }
    }
    console.log("All data has been scraped and sent to the API.");
}))();
