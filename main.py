import os
import logging
logging.basicConfig(
    filename="analyzer.log",level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
from typing import List, Dict, Optional
from logic import load_job_postings, count_skills, calculate_average_salary
from models import JobPosting

def print_summary_report(postings: List[JobPosting], skills_freq: Dict[str, int], avg_salary: Optional[float]) -> None:
    """Prints a clear and formatted summary report of the job postings."""
    logging.info("Generating summary report")
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
        logging.warning("No skills found in any of the processed job postings.")
        print("  No skills found.")
    else:
        # Sort skills by frequency in descending order, then alphabetically
        sorted_skills = sorted(skills_freq.items(), key=lambda item: (-item[1], item[0]))
        
        # Accessing top skill to demonstrate handling of IndexError
        try:
            top_skill = sorted_skills[0]
            logging.info(f"Top skill identified: '{top_skill[0]}' with frequency {top_skill[1]}")
        except IndexError:
            logging.warning("IndexError avoided: sorted_skills list is empty.")
            
        for skill, count in sorted_skills:
            print(f"  - {skill}: {count} time(s)")
    print("=========================================")

def main() -> None:
    file_path = "sample.json"
    
    if not os.path.exists(file_path):
        logging.error(f"Error: JSON file '{file_path}' not found.")
        print(f"Error: JSON file '{file_path}' not found.")
        return
        
    try:
        logging.info(f"Starting to load job postings from '{file_path}'")
        postings = load_job_postings(file_path)
        logging.info(f"Successfully loaded {len(postings)} job postings")
    except Exception as e:
        logging.exception(f"Error loading or parsing JSON file: {e}")
        print(f"Error loading or parsing JSON file. Check analyzer.log for details.")
        return
    logging.info("Starting skill frequency count")
    skills_freq = count_skills(postings)
    logging.info("Starting average salary calculation")
    avg_salary = calculate_average_salary(postings)
    print_summary_report(postings, skills_freq, avg_salary)

if __name__ == "__main__":
    main()
