"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var selenium_webdriver_1 = require("selenium-webdriver");
var dotenv_1 = require("dotenv");
var path_1 = require("path");
var typechat = require("typechat");
var axios_1 = require("axios");
var scholarshipSchemaValidator_1 = require("./scholarshipSchemaValidator");
// Load environment variables from .env file
dotenv_1.default.config({ path: path_1.default.resolve(__dirname, '.env') });
// Ensure OpenAI API key is loaded from environment variables
var openaiApiKey = process.env.OPENAI_API_KEY;
if (!openaiApiKey) {
    throw new Error("OPENAI_API_KEY environment variable is not set.");
}
// Use the validator in TypeChat
var model = typechat.createLanguageModel({ apiKey: openaiApiKey });
var translator = typechat.createJsonTranslator(model, scholarshipSchemaValidator_1.scholarshipSchemaValidator);
function formatScholarshipData(data) {
    return __awaiter(this, void 0, void 0, function () {
        var prompt, response, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    prompt = "Format the following scholarship details into the specified JSON structure and complete any missing information by referencing other websites:\n\nScholarship details: ".concat(data);
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 3, , 4]);
                    return [4 /*yield*/, translator.translate(prompt)];
                case 2:
                    response = _a.sent();
                    if (!response.success) {
                        console.error(response.message);
                        return [2 /*return*/, null];
                    }
                    // Ensure max_age is an integer
                    if (response.data.max_age && isNaN(response.data.max_age)) {
                        response.data.max_age = parseInt(response.data.max_age.toString(), 10);
                    }
                    return [2 /*return*/, response.data];
                case 3:
                    error_1 = _a.sent();
                    console.error("Error formatting data with TypeChat: ".concat(error_1.message));
                    return [2 /*return*/, null];
                case 4: return [2 /*return*/];
            }
        });
    });
}
function sendToApi(formattedData) {
    return __awaiter(this, void 0, void 0, function () {
        var apiUrl, headers, response, error_2;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    apiUrl = "https://dev-portal.scholarar.com/api/create-scholarships";
                    headers = { 'Content-Type': 'application/json' };
                    console.log("Sending data to API:", JSON.stringify({ scholarships: [formattedData] }, null, 2));
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 3, , 4]);
                    return [4 /*yield*/, axios_1.default.post(apiUrl, {
                            scholarships: [formattedData]
                        }, { headers: headers })];
                case 2:
                    response = _a.sent();
                    return [2 /*return*/, { statusCode: response.status, data: response.data }];
                case 3:
                    error_2 = _a.sent();
                    console.error("Error sending data to API: ".concat(error_2.message));
                    if (error_2.response) {
                        console.error("API response status: ".concat(error_2.response.status));
                        console.error("API response data: ".concat(JSON.stringify(error_2.response.data)));
                    }
                    return [2 /*return*/, null];
                case 4: return [2 /*return*/];
            }
        });
    });
}
(function () { return __awaiter(void 0, void 0, void 0, function () {
    var driver, allScholarships, pageNum, error_3, scholarships, i, retries, detailsLink, details, error_4, nextButton, error_5, error_6, _i, allScholarships_1, scholarship, formattedScholarship, result, statusCode, data, error_7;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0:
                console.log("Launching browser...");
                return [4 /*yield*/, new selenium_webdriver_1.Builder().forBrowser('chrome').build()];
            case 1: return [4 /*yield*/, (_a.sent())];
            case 2:
                driver = _a.sent();
                allScholarships = new Set();
                _a.label = 3;
            case 3:
                _a.trys.push([3, 35, 36, 38]);
                console.log("Navigating to the website...");
                return [4 /*yield*/, driver.get('https://www.scholars4dev.com/category/level-of-study/post-doctoral-fellowships/')];
            case 4:
                _a.sent();
                pageNum = 1;
                _a.label = 5;
            case 5:
                if (!(pageNum <= 31)) return [3 /*break*/, 34];
                console.log("Processing page ".concat(pageNum, "..."));
                _a.label = 6;
            case 6:
                _a.trys.push([6, 8, , 9]);
                return [4 /*yield*/, driver.wait(selenium_webdriver_1.until.elementLocated(selenium_webdriver_1.By.className('entry')), 120000)];
            case 7:
                _a.sent();
                return [3 /*break*/, 9];
            case 8:
                error_3 = _a.sent();
                console.error("Error waiting for scholarships on page ".concat(pageNum, ": ").concat(error_3.message));
                return [3 /*break*/, 34];
            case 9: return [4 /*yield*/, driver.findElements(selenium_webdriver_1.By.className('entry'))];
            case 10:
                scholarships = _a.sent();
                console.log("Found ".concat(scholarships.length, " scholarships on page ").concat(pageNum, "."));
                i = 0;
                _a.label = 11;
            case 11:
                if (!(i < scholarships.length)) return [3 /*break*/, 26];
                retries = 3;
                _a.label = 12;
            case 12:
                if (!(retries > 0)) return [3 /*break*/, 25];
                _a.label = 13;
            case 13:
                _a.trys.push([13, 23, , 24]);
                console.log("Processing scholarship on page ".concat(pageNum, ", index ").concat(i, "..."));
                return [4 /*yield*/, driver.findElements(selenium_webdriver_1.By.className('entry'))];
            case 14:
                scholarships = _a.sent(); // Re-fetch elements
                return [4 /*yield*/, scholarships[i].findElement(selenium_webdriver_1.By.tagName('a'))];
            case 15:
                detailsLink = _a.sent();
                if (!detailsLink) return [3 /*break*/, 22];
                return [4 /*yield*/, detailsLink.click()];
            case 16:
                _a.sent();
                return [4 /*yield*/, driver.wait(selenium_webdriver_1.until.elementLocated(selenium_webdriver_1.By.className('maincontent')), 120000)];
            case 17:
                _a.sent();
                return [4 /*yield*/, driver.findElement(selenium_webdriver_1.By.className('maincontent'))];
            case 18: return [4 /*yield*/, (_a.sent()).getText()];
            case 19:
                details = _a.sent();
                if (!allScholarships.has(details)) {
                    allScholarships.add(details);
                }
                return [4 /*yield*/, driver.navigate().back()];
            case 20:
                _a.sent();
                return [4 /*yield*/, driver.wait(selenium_webdriver_1.until.elementLocated(selenium_webdriver_1.By.className('entry')), 120000)];
            case 21:
                _a.sent();
                _a.label = 22;
            case 22: return [3 /*break*/, 25]; // Exit retry loop on success
            case 23:
                error_4 = _a.sent();
                console.error("Error processing scholarship on page ".concat(pageNum, ", index ").concat(i, ": ").concat(error_4.message));
                retries -= 1;
                if (retries === 0) {
                    console.error("Failed to process scholarship on page ".concat(pageNum, ", index ").concat(i, " after multiple attempts."));
                }
                return [3 /*break*/, 24];
            case 24: return [3 /*break*/, 12];
            case 25:
                i++;
                return [3 /*break*/, 11];
            case 26:
                if (!(pageNum < 31)) return [3 /*break*/, 33];
                _a.label = 27;
            case 27:
                _a.trys.push([27, 32, , 33]);
                return [4 /*yield*/, driver.findElement(selenium_webdriver_1.By.linkText((pageNum + 1).toString()))];
            case 28:
                nextButton = _a.sent();
                if (!nextButton) return [3 /*break*/, 31];
                return [4 /*yield*/, nextButton.click()];
            case 29:
                _a.sent();
                return [4 /*yield*/, driver.sleep(5000)];
            case 30:
                _a.sent(); // Wait for the next page to load
                _a.label = 31;
            case 31: return [3 /*break*/, 33];
            case 32:
                error_5 = _a.sent();
                console.error("Failed to navigate to page ".concat(pageNum + 1, ": ").concat(error_5.message));
                return [3 /*break*/, 34];
            case 33:
                pageNum++;
                return [3 /*break*/, 5];
            case 34: return [3 /*break*/, 38];
            case 35:
                error_6 = _a.sent();
                console.error("Error navigating to the website: ".concat(error_6.message));
                return [3 /*break*/, 38];
            case 36: return [4 /*yield*/, driver.quit()];
            case 37:
                _a.sent();
                return [7 /*endfinally*/];
            case 38:
                console.log("Total scholarships collected: ".concat(allScholarships.size));
                _i = 0, allScholarships_1 = allScholarships;
                _a.label = 39;
            case 39:
                if (!(_i < allScholarships_1.length)) return [3 /*break*/, 47];
                scholarship = allScholarships_1[_i];
                _a.label = 40;
            case 40:
                _a.trys.push([40, 45, , 46]);
                return [4 /*yield*/, formatScholarshipData(scholarship)];
            case 41:
                formattedScholarship = _a.sent();
                if (!formattedScholarship) return [3 /*break*/, 43];
                return [4 /*yield*/, sendToApi(formattedScholarship)];
            case 42:
                result = _a.sent();
                if (result) {
                    statusCode = result.statusCode, data = result.data;
                    console.log("API Response (Status Code: ".concat(statusCode, "): ").concat(JSON.stringify(data)));
                }
                else {
                    console.log("Failed to send scholarship data to API: ".concat(scholarship));
                }
                return [3 /*break*/, 44];
            case 43:
                console.log("Failed to format scholarship data: ".concat(scholarship));
                _a.label = 44;
            case 44: return [3 /*break*/, 46];
            case 45:
                error_7 = _a.sent();
                console.error("Failed to process scholarship: ".concat(error_7.message));
                return [3 /*break*/, 46];
            case 46:
                _i++;
                return [3 /*break*/, 39];
            case 47:
                console.log("All data has been scraped and sent to the API.");
                return [2 /*return*/];
        }
    });
}); })();
