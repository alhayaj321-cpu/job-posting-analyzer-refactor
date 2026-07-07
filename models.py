from dataclasses import dataclass
from typing import List, Optional

@dataclass
class JobPosting:
    title: str
    description: str
    skills: List[str]
    salary: Optional[float] = None
