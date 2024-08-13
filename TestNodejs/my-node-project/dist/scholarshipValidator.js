"use strict";
// scholarshipValidator.ts
Object.defineProperty(exports, "__esModule", { value: true });
exports.scholarshipSchemaValidator = void 0;
// Validator Implementation
exports.scholarshipSchemaValidator = {
    validate: (jsonObject) => {
        const json = jsonObject;
        if (typeof json.name === 'string' &&
            typeof json.description === 'string' &&
            typeof json.type_id === 'string' &&
            typeof json.ielt === 'boolean' &&
            typeof json.toefl === 'boolean' &&
            Array.isArray(json.majors) &&
            Array.isArray(json.degrees) &&
            Array.isArray(json.countries) &&
            Array.isArray(json.study_modes)) {
            return { success: true, data: json };
        }
        else {
            return { success: false, message: "Invalid ScholarshipResponse structure" };
        }
    },
    getSchemaText: () => "", // Add getSchemaText property
    getTypeName: () => "" // Add getTypeName property
};
