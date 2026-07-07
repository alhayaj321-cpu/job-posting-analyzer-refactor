import json
from collections import Counter
from typing import List, Dict, Optional
from models import JobPosting

def load_job_postings(file_path: str) -> List[JobPosting]:
    """Reads job postings from a JSON file and maps them to JobPosting objects."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    postings: List[JobPosting] = []
    for item in data:
        # Get fields, safely handling optional/missing fields
        title: str = item.get("title", "")
        description: str = item.get("description", "")
        skills: List[str] = item.get("skills", [])
        
        # item.get("salary") returns None if "salary" key is missing or explicitly set to null
        salary_val = item.get("salary")
        salary: Optional[float] = None
        
        if salary_val is not None:
            try:
                salary = float(salary_val)
            except (ValueError, TypeError):
                salary = None
                
        postings.append(
            JobPosting(
                title=title,
                description=description,
                skills=skills,
                salary=salary
            )
        )
    return postings

def count_skills(postings: List[JobPosting]) -> Dict[str, int]:
    """Counts the frequency of each skill across all job postings."""
    skill_counter: Counter[str] = Counter()
    for posting in postings:
        skill_counter.update(posting.skills)
    return dict(skill_counter)

def calculate_average_salary(postings: List[JobPosting]) -> Optional[float]:
    """Computes the average salary of all job postings that contain a salary."""
    salaries = [p.salary for p in postings if p.salary is not None]
    if not salaries:
        return None
    return sum(salaries) / len(salaries)
