#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# flake8: noqa

"""
Project: hhs_oauth_server
App: apps.fhir.testac.utils
FILE: sample_json_bb
Created: 7/27/16 10:39 AM

Created by: Mark Scirmshire @ekivemark

"""

SAMPLE_FHIR_CREATE_SUCCESS = """
{"issue": [{"severity": "information",
            "code": "informational",
            "diagnostics": "Successfully created resource \\"Patient/9334211/_history/1\\" in 47ms"
           }
          ],
 "resourceType": "OperationOutcome"
 }
"""

SAMPLE_BB_JSON = """
{
    "header": {
        "effectiveTime": {
            "value": "20130316051000+0500"
        },
        "source": "MyMedicare.gov",
        "versionNumber": {
            "value": "2"
        },
        "originator": "MyMedicare.gov",
        "title": "MyMedicare.gov Personal Health Information",
        "comments": [
            "generated by python-cmsblue utility",
            "http://github.com/ekivemark/python-cmsblue",
            "using text file downloaded from",
            "https://myMedicare.gov",
            "**********CONFIDENTIAL***********",
            "Produced by the Blue Button (v2.0)"
        ],
        "languageCode": "code='en-US'",
        "confidentialityCode": {
            "code": "N",
            "codeSystem": "2.16.840.1.113883.5.25"
        },
        "header": {
            "header": "MYMEDICARE.GOV PERSONAL HEALTH INFORMATION"
        }
    },
    "patient": {
        "patient": {
            "patient": "Demographic"
        },
        "source": "MyMedicare.gov",
        "name": "JOHN DOE",
        "dateOfBirth": "19100101",
        "address": {
            "addressType": "",
            "addressLine1": "123 ANY ROAD",
            "addressLine2": "",
            "city": "ANYTOWN",
            "state": "VA",
            "zip": "00001"
        },
        "phoneNumber": [
            "123-456-7890"
        ],
        "email": "JOHNDOE@example.com",
        "medicare": {
            "partAEffectiveDate": "20120101",
            "partBEffectiveDate": "20120101"
        }
    },
    "emergencyContact": [
        {
            "emergencyContact": "Emergency Contact",
            "contactName": "JANE DOE",
            "address": {
                "addressType": "Home",
                "addressLine1": "123 AnyWhere St",
                "addressLine2": "",
                "city": "AnyWhere",
                "state": "DC",
                "zip": "00002-1111"
            },
            "relationship": "Other",
            "phone": {
                "work": "000-001-0001",
                "home": "123-456-7890",
                "mobile": "000-001-0002"
            },
            "emailAddress": "JANEDOE@example.com",
            "category": "Emergency Contact",
            "source": "patient"
        },
        {
            "contactName": "STEVE DOE",
            "address": {
                "addressType": "",
                "addressLine1": "123 AnyWhere Rd",
                "addressLine2": "",
                "city": "AnyWhere",
                "state": "VA",
                "zip": "00001"
            },
            "relationship": "Other",
            "phone": {
                "work": "000-001-0001",
                "home": "123-456-7890",
                "mobile": "000-001-0002"
            },
            "emailAddress": "STEVEDOE@example.com",
            "category": "Emergency Contact",
            "source": "patient"
        }
    ],
    "medicalConditions": [
        {
            "medicalConditions": "Self Reported Medical Conditions",
            "conditionName": "Arthritis",
            "medicalConditionStartDate": "20050809",
            "medicalConditionEndDate": "20110228",
            "category": "Self Reported Medical Conditions",
            "source": "patient"
        },
        {
            "conditionName": "Asthma",
            "medicalConditionStartDate": "20080125",
            "medicalConditionEndDate": "20100125",
            "category": "Self Reported Medical Conditions",
            "source": "patient"
        }
    ],
    "Allergies": [
        {
            "Allergies": "Self Reported Allergies",
            "allergyName": "Antibotic",
            "type": "Drugs",
            "reaction": "Vomiting",
            "severity": "Severe",
            "diagnosed": "Yes",
            "treatment": "Allergy Shots",
            "firstEpisodeDate": "19260108",
            "lastEpisodeDate": "19550313",
            "lastTreatmentDate": "19490928",
            "comments": [
                "Erythromycin"
            ],
            "category": "Self Reported Allergies",
            "source": "patient"
        },
        {
            "allergyName": "Grasses",
            "type": "Environmental",
            "reaction": "Sneezing",
            "severity": "Severe",
            "diagnosed": "Yes",
            "treatment": "Avoidance",
            "firstEpisodeDate": "19730513",
            "lastEpisodeDate": "19960720",
            "lastTreatmentDate": "20080927",
            "comments": [
                ""
            ],
            "category": "Self Reported Allergies",
            "source": "patient"
        }
    ],
    "ImplantableDevices": [
        {
            "ImplantableDevices": "Self Reported Implantable Device",
            "deviceName": "Artificial Eye Lenses",
            "dateImplanted": "19420127",
            "category": "Self Reported Implantable Device",
            "source": "patient"
        }
    ],
    "Immunizations": [
        {
            "Immunizations": "Self Reported Immunizations",
            "immunizationName": "Varicella/Chicken Pox",
            "dateAdministered": "20020421",
            "method": "Nasal Spray(mist)",
            "wereYouVaccinatedInTheUs": "",
            "comments": [
                "congestion"
            ],
            "category": "Self Reported Immunizations",
            "source": "patient"
        },
        {
            "booster1Date": "19900202",
            "booster2Date": "",
            "booster3Date": "",
            "immunizationName": "typhoid",
            "dateAdministered": "20090102",
            "method": "Injection",
            "wereYouVaccinatedInTheUs": "",
            "comments": [
                ""
            ],
            "category": "Self Reported Immunizations",
            "source": "patient"
        },
        {
            "booster1Date": "",
            "booster2Date": "",
            "booster3Date": "",
            "category": "Self Reported Immunizations",
            "source": "patient"
        }
    ],
    "Labs": [
        {
            "Labs": "Self Reported Labs and Tests",
            "testLabType": "Glucose Level",
            "dateTaken": "20080321",
            "administeredBy": "AnyLab",
            "requestingDoctor": "Dr. Smith",
            "reasonTestLabRequested": "Ongoing elevated glucose",
            "results": "135, 170, 150, 120",
            "comments": [
                "Fasting, hour 1, hour 2, hour 3"
            ],
            "category": "Self Reported Labs and Tests",
            "source": "patient"
        }
    ],
    "vitals": [
        {
            "vitals": "Self Reported Vital Statistics",
            "vitalStatisticType": "Blood Pressure",
            "date": "20110722",
            "time": "3:00 PM",
            "reading": "120/80",
            "comments": [
                ""
            ],
            "category": "Self Reported Vital Statistics",
            "source": "patient"
        },
        {
            "vitalStatisticType": "Glucose",
            "date": "20120320",
            "time": "12:00 PM",
            "reading": "110",
            "comments": [
                ""
            ],
            "category": "Self Reported Vital Statistics",
            "source": "patient"
        }
    ],
    "familyHistory": [
        {
            "familyHistory": "Family Medical History",
            "source": "patient",
            "familyMember": "Brother",
            "type": "",
            "dob": "19150110",
            "dod": "",
            "age": "",
            "condition": [
                {
                    "type": "type",
                    "description": "description",
                    "category": "Family Medical History",
                    "source": "patient"
                },
                {
                    "description": "description",
                    "category": "Family Medical History",
                    "source": "patient"
                },
                {
                    "description": "description",
                    "type": "type",
                    "category": "Family Medical History",
                    "source": "patient"
                },
                {
                    "description": "description",
                    "category": "Family Medical History",
                    "source": "patient"
                },
                {
                    "description": "description",
                    "category": "Family Medical History",
                    "source": "patient"
                },
                {
                    "description": "description",
                    "category": "Family Medical History",
                    "source": "patient"
                },
                {
                    "description": "description"
                }
            ]
        }
    ],
    "medications": [
        {
            "medications": "Drugs",
            "drugName": "Aspirin",
            "supply": "Dialy",
            "origDrugEntry": "Aspirin",
            "category": "Drugs",
            "source": "patient"
        }
    ],
    "preventiveServices": [
        {
            "preventiveServices": "Preventive Services",
            "description": "DIABETES",
            "nextEligibleDate": "20111001",
            "lastDateOfService": "",
            "category": "Preventive Services",
            "source": "MyMedicare.gov"
        },
        {
            "description": "PAP TEST DR",
            "nextEligibleDate": "20111001",
            "lastDateOfService": "",
            "category": "Preventive Services",
            "source": "MyMedicare.gov"
        },
        {
            "description": "ABDOMINAL AORTIC ANEURYSM",
            "nextEligibleDate": "20120701",
            "lastDateOfService": "",
            "category": "Preventive Services",
            "source": "MyMedicare.gov"
        },
        {
            "description": "ANNUAL WELLNESS VISIT",
            "nextEligibleDate": "20130101",
            "lastDateOfService": "",
            "category": "Preventive Services",
            "source": "MyMedicare.gov"
        },
        {
            "description": "DEPRESSION SCREENING",
            "nextEligibleDate": "20121014",
            "lastDateOfService": "",
            "category": "Preventive Services",
            "source": "MyMedicare.gov"
        }
    ],
    "providers": [
        {
            "providers": "Providers",
            "providerName": "ANY CARE",
            "providerAddress": "123 Any Rd, Anywhere, MD 99999",
            "type": "NHC",
            "specialty": "",
            "medicareProvider": "Not Available",
            "category": "Providers",
            "source": "patient"
        },
        {
            "providerName": "ANY HOSPITAL1",
            "providerAddress": "123 Drive, Anywhere, VA 00001",
            "type": "HOS",
            "specialty": "",
            "medicareProvider": "Not Available",
            "category": "Providers",
            "source": "patient"
        },
        {
            "providerName": "Jane Doe",
            "providerAddress": "123 Road, Anywhere, VA 00001",
            "type": "PHY",
            "specialty": "Other",
            "medicareProvider": "Not Available",
            "category": "Providers",
            "source": "patient"
        }
    ],
    "pharmacies": [
        {
            "pharmacies": "Pharmacies",
            "pharmacyName": "PHARMACY, EAST STREET ANYWHERE, DC 00002",
            "pharmacyPhone": "000-000-0001",
            "category": "Pharmacies",
            "source": "patient"
        },
        {
            "pharmacyName": "ANY PHARMACY, WEST STREET ANYWHERE, VA 00001",
            "pharmacyPhone": "000-000-0002",
            "category": "Pharmacies",
            "source": "patient"
        }
    ],
    "insurance": [
        {
            "insurance": "Plans",
            "contractIdPlanId": "H9999/9999",
            "planPeriod": "09/01/2011 - current",
            "planName": "A Medicare Plan Plus (HMO)",
            "marketingName": "HealthCare Payer",
            "planAddress": "123 Any Road Anytown PA 00003",
            "planType": "3 - Coordinated Care Plan (HMO, PPO, PSO, SNP)",
            "category": "Plans",
            "source": "MyMedicare.gov"
        },
        {
            "contractIdPlanId": "S9999/000",
            "planPeriod": "01/01/2010 - current",
            "planName": "A Medicare Rx Plan (PDP)",
            "marketingName": "Another HealthCare Payer",
            "planAddress": "123 Any Road Anytown PA 00003",
            "planType": "11 - Medicare Prescription Drug Plan",
            "category": "Plans",
            "source": "MyMedicare.gov"
        },
        {
            "employerPlan": "STATE HEALTH BENEFITS PROGRAM",
            "employerSubsidyStartDate": "20110101",
            "employerSubsidyEndDate": "20111231",
            "category": "Employer Subsidy",
            "source": "MyMedicare.gov"
        },
        {
            "mspType": "End stage Renal Disease (ESRD)",
            "policyNumber": "1234567890",
            "insurerName": "Insurer1",
            "insurerAddress": "PO BOX 0000 Anytown, CO 00002-0000",
            "effectiveDate": "20110101",
            "terminationDate": "20110930",
            "category": "Primary Insurance",
            "source": "MyMedicare.gov"
        },
        {
            "mspType": "End stage Renal Disease (ESRD)",
            "policyNumber": "12345678901",
            "insurerName": "Insurer2",
            "insurerAddress": "0000 Any ROAD ANYWHERE, VA 00000-0000",
            "effectiveDate": "20100101",
            "terminationDate": "20101231",
            "category": "Primary Insurance",
            "source": "MyMedicare.gov"
        },
        {
            "mspType": "",
            "policyNumber": "00001",
            "insurerName": "Insurer",
            "insurerAddress": "00 Address STREET ANYWHERE, PA 00000",
            "effectiveDate": "19841001",
            "terminationDate": "20081130",
            "category": "Other Insurance",
            "source": "MyMedicare.gov"
        }
    ],
    "claims": [
        {
            "claims": "Claim Summary",
            "claimNumber": "1234567890000",
            "provider": "No Information Available",
            "providerBillingAddress": "",
            "date": {
                "serviceStartDate": "20121018",
                "serviceEndDate": ""
            },
            "charges": {
                "amountCharged": "$60.00",
                "medicareApproved": "$34.00",
                "providerPaid": "$27.20",
                "youMayBeBilled": "$6.80"
            },
            "claimType": "PartB",
            "diagnosisCode1": "3534",
            "diagnosisCode2": "7393",
            "diagnosisCode3": "7392",
            "diagnosisCode4": "3533",
            "category": "Claim Summary",
            "source": "MyMedicare.gov",
            "details": [
                {
                    "details": "Claim Lines for Claim Number",
                    "lineNumber": "1",
                    "dateOfServiceFrom": "20121018",
                    "dateOfServiceTo": "20121018",
                    "procedureCodeDescription": "98941 - Chiropractic Manipulative Treatment (Cmt); Spinal, Three To Four Regions",
                    "modifier1Description": "AT - Acute Treatment (This Modifier Should Be Used When Reporting Service 98940, 98941, 98942)",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "1",
                    "submittedAmountCharges": "$60.00",
                    "allowedAmount": "$34.00",
                    "nonCovered": "$26.00",
                    "placeOfServiceDescription": "11 - Office",
                    "typeOfServiceDescription": "1 - Medical Care",
                    "renderingProviderNo": "0000001",
                    "renderingProviderNpi": "123456789",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "1234567890000"
                }
            ]
        },
        {
            "claim": "claim Header",
            "claimNumber": "12345678900000VAA",
            "provider": "No Information Available",
            "providerBillingAddress": "",
            "date": {
                "serviceStartDate": "20120922",
                "serviceEndDate": ""
            },
            "charges": {
                "amountCharged": "$504.80",
                "medicareApproved": "$504.80",
                "providerPaid": "$126.31",
                "youMayBeBilled": "$38.84"
            },
            "claimType": "Outpatient",
            "diagnosisCode1": "56400",
            "diagnosisCode2": "7245",
            "diagnosisCode3": "V1588",
            "category": "claim Header",
            "source": "MyMedicare.gov",
            "details": [
                {
                    "details": "Claim Lines for Claim Number",
                    "lineNumber": "1",
                    "dateOfServiceFrom": "20120922",
                    "revenueCodeDescription": "0250 - General Classification PHARMACY",
                    "procedureCodeDescription": "",
                    "modifier1Description": "",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "1",
                    "submittedAmountCharges": "$14.30",
                    "allowedAmount": "$14.30",
                    "nonCovered": "$0.00",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "12345678900000VAA"
                },
                {
                    "lineNumber": "2",
                    "dateOfServiceFrom": "20120922",
                    "revenueCodeDescription": "0320 - General Classification DX X-RAY",
                    "procedureCodeDescription": "74020 - Radiologic Examination, Abdomen; Complete, Including Decubitus And/Or Erect Views",
                    "modifier1Description": "",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "1",
                    "submittedAmountCharges": "$175.50",
                    "allowedAmount": "$175.50",
                    "nonCovered": "$0.00",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "12345678900000VAA"
                },
                {
                    "lineNumber": "3",
                    "dateOfServiceFrom": "20120922",
                    "revenueCodeDescription": "0450 - General Classification EMERG ROOM",
                    "procedureCodeDescription": "99283 - Emergency Department Visit For The Evaluation And Management Of A Patient, Which Requires Th",
                    "modifier1Description": "25 - Significant, Separately Identifiable Evaluation And Management Service By The Same Physician On",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "1",
                    "submittedAmountCharges": "$315.00",
                    "allowedAmount": "$315.00",
                    "nonCovered": "$0.00",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "12345678900000VAA"
                },
                {
                    "lineNumber": "4",
                    "dateOfServiceFrom": "",
                    "revenueCodeDescription": "0001 - Total Charges",
                    "procedureCodeDescription": "",
                    "modifier1Description": "",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "0",
                    "submittedAmountCharges": "$504.80",
                    "allowedAmount": "$504.80",
                    "nonCovered": "$0.00",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "12345678900000VAA"
                }
            ]
        },
        {
            "claimNumber": "1234567890123",
            "provider": "No Information Available",
            "providerBillingAddress": "",
            "serviceStartDate": "20121201",
            "serviceEndDate": "",
            "amountCharged": "* Not Available *",
            "medicareApproved": "* Not Available *",
            "providerPaid": "* Not Available *",
            "youMayBeBilled": "* Not Available *",
            "claimType": "PartB",
            "diagnosisCode1": "7392",
            "diagnosisCode2": "7241",
            "diagnosisCode3": "7393",
            "diagnosisCode4": "7391",
            "category": "Claim Lines for Claim Number",
            "source": "MyMedicare.gov",
            "details": [
                {
                    "details": "Claim Lines for Claim Number",
                    "lineNumber": "1",
                    "dateOfServiceFrom": "20121201",
                    "dateOfServiceTo": "20121201",
                    "procedureCodeDescription": "98941 - Chiropractic Manipulative Treatment, 3 To 4 Spinal Regions",
                    "modifier1Description": "GA - Waiver Of Liability Statement Issued As Required By Payer Policy, Individual Case",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "1",
                    "submittedAmountCharges": "* Not Available *",
                    "allowedAmount": "* Not Available *",
                    "nonCovered": "* Not Available *",
                    "placeOfServiceDescription": "11 - Office",
                    "typeOfServiceDescription": "1 - Medical Care",
                    "renderingProviderNo": "123456",
                    "renderingProviderNpi": "123456789",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "1234567890123"
                },
                {
                    "lineNumber": "2",
                    "dateOfServiceFrom": "20121201",
                    "dateOfServiceTo": "20121201",
                    "procedureCodeDescription": "G0283 - Electrical Stimulation (Unattended), To One Or More Areas For Indication(S) Other Than Wound",
                    "modifier1Description": "GY - Item Or Service Statutorily Excluded, Does Not Meet The Definition Of Any Medicare Benefit Or,",
                    "modifier2Description": "",
                    "modifier3Description": "",
                    "modifier4Description": "",
                    "quantityBilledUnits": "1",
                    "submittedAmountCharges": "* Not Available *",
                    "allowedAmount": "* Not Available *",
                    "nonCovered": "* Not Available *",
                    "placeOfServiceDescription": "11 - Office",
                    "typeOfServiceDescription": "1 - Medical Care",
                    "renderingProviderNo": "123456",
                    "renderingProviderNpi": "123456789",
                    "category": "Claim Lines for Claim Number",
                    "source": "MyMedicare.gov",
                    "claimNumber": "1234567890123"
                }
            ]
        },
        {
            "partDClaim": "Part D Claims",
            "claimType": "Part D",
            "claimNumber": "123456789012",
            "claimServiceDate": "20111117",
            "pharmacyServiceProvider": "123456789",
            "pharmacyName": "PHARMACY2 #00000",
            "drugCode": "00093013505",
            "drugName": "CARVEDILOL",
            "fillNumber": "0",
            "days'Supply": "30",
            "prescriberIdentifer": "123456789",
            "prescriberName": "Jane Doe",
            "category": "Part D Claims",
            "source": "MyMedicare.gov"
        },
        {
            "partDClaim": "Part D Claims",
            "claimType": "Part D",
            "claimNumber": "123456789011",
            "claimServiceDate": "20111123",
            "pharmacyServiceProvider": "1234567890",
            "pharmacyName": "PHARMACY3 #00000",
            "drugCode": "00781223310",
            "drugName": "OMEPRAZOLE",
            "fillNumber": "4",
            "days'Supply": "30",
            "prescriberIdentifer": "123456789",
            "prescriberName": "Jane Doe",
            "category": "Part D Claims",
            "source": "MyMedicare.gov"
        }
    ]
}
"""