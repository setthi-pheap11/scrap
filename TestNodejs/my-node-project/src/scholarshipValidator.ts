// scholarshipValidator.ts

import { TypeChatJsonValidator, Result } from 'typechat'; // Adjust the import based on actual package

export interface ScholarshipResponse {
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

// Validator Implementation
export const scholarshipSchemaValidator: TypeChatJsonValidator<ScholarshipResponse> = {
    validate: (jsonObject: object): Result<ScholarshipResponse> => {
        const json = jsonObject as ScholarshipResponse;

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
        } else {
            return { success: false, message: "Invalid ScholarshipResponse structure" };
        }
    },
    getSchemaText: () => "", // Add getSchemaText property
    getTypeName: () => "" // Add getTypeName property
};
