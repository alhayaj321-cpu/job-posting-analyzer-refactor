
# CONTEXT

The project is a **Job Posting Analyzer** that reads job postings from a JSON file.

The finished application should:

* Read job postings from a JSON file.
* Count the most common skills across all job postings.
* Compute the average salary from all postings that contain a salary.
* Print a clear summary report showing:

  * Total number of job postings.
  * Average salary.
  * Most common skills and their frequencies.

The final project should also follow good Python project structure by separating responsibilities into three files:

* `models.py` → data classes only.
* `logic.py` → functions that work with the models.
* `main.py` → entry point that runs the application.

The import direction must be one-way only:

`main.py → logic.py → models.py`

There must be **no circular imports**.

Every function should include correct type hints for all parameters and return values.

The project should be suitable for creating a virtual environment, generating a `requirements.txt`, and pushing to GitHub.

# CONSTRAINTS

* Do NOT write code yet.
* Produce a numbered implementation plan only.
* Keep the design beginner-friendly and easy to understand.
* Do not over-engineer the solution.
* Do not use inheritance unless it is clearly necessary.
* Do not create abstract classes or unnecessary Manager, Handler, Factory, or Service classes.
* Keep each class responsible for its own data and related behavior.
* Any stateless operation should be implemented as a plain function instead of a class.
* Use only Python's standard library unless there is a strong justification.
* Keep the project organized so it can easily be reviewed and refactored.
* Maintain one-way imports only:
  `main.py → logic.py → models.py`
* Explain any design decision that might not be obvious.

# DONE-CRITERIA

The project is complete when:

1. The program correctly reads job postings from a JSON file.
2. It correctly counts the most common skills.
3. It correctly computes the average salary.
4. It prints a readable summary report.
5. The project is split into:

   * `models.py`
   * `logic.py`
   * `main.py`
6. All functions have correct type hints.
7. The import direction is one-way only and there are no circular imports.
8. The code is beginner-friendly, maintainable, and free from unnecessary abstraction or inheritance.
9. The project can be run successfully with:
   `python main.py`

