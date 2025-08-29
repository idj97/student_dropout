application_mode_mapping = {
    1: 1,  # 1. General Contingent (First, Second, and Third Phases)
    17: 1,
    18: 1,
    5: 2,  # 2. Special Contingent (Regional and Other Specific Categories)
    16: 2,
    39: 2,
    2: 3,  # 3. Ordinance-Specific Admissions (Based on Legal Frameworks)
    10: 3,
    26: 3, 
    27: 3,
    15: 4, # 4. International Students
    57: 4,
    42: 5, # 5. Applicants Seeking to Transfer or Change Course
    43: 5,
    51: 5,
    7: 6,  # 6. Specific Qualifications and Diplomas,
    44: 6,
    53: 6
}

def map_application_mode(mode):
    mapped_mode = application_mode_mapping.get(mode)
    if mapped_mode == None:
        return 0
    else:
        return mapped_mode
    

