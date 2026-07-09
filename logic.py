import json
import logging

from collections import Counter
from typing import List, Dict, Optional
from models import JobPosting
logging.basicConfig(
    filename="analyzer.log",level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
def load_job_postings(file_path: str) -> List[JobPosting]:
    """Reads job postings from a JSON file and maps them to JobPosting objects."""
    try:
        logging.info(f"Loading job postings from '{file_path}'")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, PermissionError) as e:
        logging.exception(f"File error occurred when opening '{file_path}': {e}")
        raise e
    except json.JSONDecodeError as e:
        logging.exception(f"JSON decoding failed for file '{file_path}': {e}")
        raise e

    postings: List[JobPosting] = []
    if not isinstance(data, list):
        logging.error(f"Expected JSON root to be a list, but got {type(data).__name__}")
        raise TypeError("JSON root must be a list")

    for row_idx, item in enumerate(data, start=1):
        try:
            if not isinstance(item, dict):
                raise AttributeError("Item is not a dictionary")

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
                    logging.warning(f"Row {row_idx}: Could not convert salary value '{salary_val}' to float; setting to None")
                    salary = None
                    
            postings.append(
                JobPosting(
                    title=title,
                    description=description,
                    skills=skills,
                    salary=salary
                )
            )
        except AttributeError as e:
            logging.warning(f"Row {row_idx}: Skipped due to invalid data format (not a dictionary). Raw value: '{item}'")

    logging.info(f"Successfully loaded {len(postings)} job postings")
    return postings

def count_skills(postings: List[JobPosting]) -> Dict[str, int]:
    """Counts the frequency of each skill across all job postings."""
    skill_counter: Counter[str] = Counter()
    logging.info(f"Processing skills for {len(postings)} postings")
    for posting in postings:
        skill_counter.update(posting.skills)

    return dict(skill_counter)

def calculate_average_salary(postings: List[JobPosting]) -> Optional[float]:
    """Computes the average salary of all job postings that contain a salary."""
    salaries = [p.salary for p in postings if p.salary is not None]
    try:
        return sum(salaries) / len(salaries)
    except ZeroDivisionError:
        logging.warning("No job postings found with a valid salary value; average salary calculation division by zero avoided.")
        return None
