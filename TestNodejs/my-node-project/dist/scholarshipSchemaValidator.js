"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.scholarshipSchemaValidator = void 0;
// Create the schema validator for ScholarshipResponse
exports.scholarshipSchemaValidator = {
    validate: function (json) {
        return typeof json.name === 'string' &&
            typeof json.description === 'string' &&
            typeof json.type_id === 'string' &&
            typeof json.ielt === 'boolean' &&
            typeof json.toefl === 'boolean' &&
            Array.isArray(json.majors) &&
            Array.isArray(json.degrees) &&
            Array.isArray(json.countries) &&
            Array.isArray(json.study_modes);
    }
};
