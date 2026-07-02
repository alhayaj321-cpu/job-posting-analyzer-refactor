class DataHolder:
    def __init__(self, value):
        self.value = value

class JobTitle(DataHolder):
    pass

class JobDescription(DataHolder):
    pass

class SkillList(DataHolder):
    pass

class BaseAnalyzer:
    def analyze(self):
        raise NotImplementedError

class KeywordExtractor(BaseAnalyzer):
    def __init__(self, description: JobDescription):
        self.description = description

    def analyze(self):
        return self.description.value.lower().split()

class SkillMatcher(BaseAnalyzer):
    def __init__(self, keywords: list, required_skills: SkillList):
        self.keywords = keywords
        self.required_skills = required_skills

    def analyze(self):
        matched = [s for s in self.required_skills.value if s.lower() in self.keywords]
        return matched

class ScoreCalculator(BaseAnalyzer):
    def __init__(self, matched_skills: list, required_skills: SkillList):
        self.matched_skills = matched_skills
        self.required_skills = required_skills

    def analyze(self):
        if not self.required_skills.value:
            return 0
        return len(self.matched_skills) / len(self.required_skills.value) * 100

class JobPostingAnalyzer:
    def __init__(self, title: JobTitle, description: JobDescription, required_skills: SkillList):
        self.title = title
        self.description = description
        self.required_skills = required_skills

    def run_analysis(self):
        keywords = KeywordExtractor(self.description).analyze()
        matched = SkillMatcher(keywords, self.required_skills).analyze()
        score = ScoreCalculator(matched, self.required_skills).analyze()
        return {
            "title": self.title.value,
            "matched_skills": matched,
            "match_score": score
        }

if __name__ == "__main__":
    title = JobTitle("Python Developer")
    description = JobDescription("Looking for a developer with experience in Python, SQL, and Docker.")
    required_skills = SkillList(["Python", "SQL", "Docker", "Java"])

    analyzer = JobPostingAnalyzer(title, description, required_skills)
    result = analyzer.run_analysis()

    print("=== Job Analysis Results ===")
    print(f"Job Title: {result['title']}")
    print(f"Matched Skills: {result['matched_skills']}")
    print(f"Match Score: {result['match_score']:.2f}%")