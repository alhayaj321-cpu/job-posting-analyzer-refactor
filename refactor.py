#make functions instead of classses as they are not doing anything meaningful.
#use single responsibility principle.
#use high cohesion.

def extract_keywords(description):
    return description.lower().split()

def match_skills(keywords, required_skills):
    return [s for s in required_skills if s.lower() in keywords]

def calculate_score(matched_skills, required_skills):
    if not required_skills:
        return 0
    return len(matched_skills) / len(required_skills) * 100

class JobPostingAnalyzer:

    def __init__(self, title, description, required_skills):
        self.title = title
        self.description = description
        self.required_skills = required_skills

    def run_analysis(self):
        #used composition instead of inheritance.
        keywords = extract_keywords(self.description)
        matched = match_skills(keywords, self.required_skills)
        score = calculate_score(matched, self.required_skills)

        return {
            "title": self.title,
            "matched_skills": matched,
            "match_score": score
        }