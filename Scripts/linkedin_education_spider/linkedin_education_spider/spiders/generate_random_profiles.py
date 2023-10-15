import random
import json

profiles = []

for i in range(100):
    profile = {}
    profile["profile"] = f"profile_{i}"
    profile["url"] = f"https://www.linkedin.com/in/profile_{i}/"
    profile["name"] = f"Name_{i}"
    profile["description"] = f"Description_{i}"
    profile["location"] = random.choice(["Bogota, Colombia", "Berlin, Germany", "New York, USA"])
    profile["followers"] = str(random.randint(1, 1000))
    profile["connections"] = str(random.randint(1, 500))
    profile["about"] = f"About_{i}"
    
    experience = []
    for j in range(random.randint(1, 5)):
        exp = {}
        exp["organisation_profile"] = f"https://www.linkedin.com/company/org_{j}"
        exp["location"] = random.choice(["Bogota, Colombia", "Berlin, Germany", "New York, USA"])
        exp["description"] = f"Description_{j}"
        exp["start_time"] = f"Jan {random.randint(2015, 2022)}"
        exp["end_time"] = f"Dec {random.randint(2015, 2022)}"
        experience.append(exp)
    profile["experience"] = experience
    
    education = []
    for k in range(random.randint(1, 3)):
        edu = {}
        edu["organisation"] = f"Organisation_{k}"
        edu["organisation_profile"] = f"https://www.linkedin.com/school/org_{k}/"
        edu["course_details"] = f"Course_{k}"
        edu["description"] = f"Description_{k}"
        edu["start_time"] = f"{random.randint(2010, 2015)}"
        edu["end_time"] = f"{random.randint(2015, 2022)}"
        education.append(edu)
    profile["education"] = education
    
    profiles.append(profile)

print("sss")
with open('linkedin_profiles.json', 'w') as f:
    json.dump(profiles, f, indent=3,separators=(',', ':'))
