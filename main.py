import os
from typing import List, Dict, Optional
from logic import load_job_postings, count_skills, calculate_average_salary
from models import JobPosting

def print_summary_report(postings: List[JobPosting], skills_freq: Dict[str, int], avg_salary: Optional[float]) -> None:
    """Prints a clear and formatted summary report of the job postings."""
    print("=========================================")
    print("        JOB POSTING ANALYZER REPORT      ")
    print("=========================================")
    print(f"Total Job Postings: {len(postings)}")
    
    if avg_salary is not None:
        print(f"Average Salary:     ${avg_salary:,.2f}")
    else:
        print("Average Salary:     N/A (No postings with valid salaries)")
        
    print("-----------------------------------------")
    print("Most Common Skills & Frequencies:")
    if not skills_freq:
        print("  No skills found.")
    else:
        # Sort skills by frequency in descending order, then alphabetically
        sorted_skills = sorted(skills_freq.items(), key=lambda item: (-item[1], item[0]))
        for skill, count in sorted_skills:
            print(f"  - {skill}: {count} time(s)")
    print("=========================================")

def main() -> None:
    file_path = "sample.json"
    
    if not os.path.exists(file_path):
        print(f"Error: JSON file '{file_path}' not found.")
        return
        
    try:
        postings = load_job_postings(file_path)
    except Exception as e:
        print(f"Error loading or parsing JSON file: {e}")
        return
        
    skills_freq = count_skills(postings)
    avg_salary = calculate_average_salary(postings)
    
    print_summary_report(postings, skills_freq, avg_salary)

if __name__ == "__main__":
    main()
