# Python Essentials [FastTrack] — Complete 3-Day Courseware

Welcome to the **Python Essentials [FastTrack]** comprehensive training repository. This course is dynamically crafted for high-impact, industry-ready Python mastery, blending software engineering logic, systems programming, and modern Python 3.10/3.11 features.

---

## 📅 3-Day Structural Breakdown

```
e:\training\python_fasttrack\
│
├── README.md                              <-- Master Course Guide (You are here)
├── outline.pdf                            <-- Original Curriculum Specification
│
├── day-1/                                 <-- SECTION 1: Fundamentals & Core Mechanics
│   ├── DAY_01_OVERVIEW.md
│   ├── module_01_intro/                   <-- Module 1: Introduction to Python
│   │   ├── README.md                      <-- Full Concept Explanations & Setup Guide
│   │   ├── teaching_code.py               <-- Instructor Walkthrough Script
│   │   └── practice_exercises.py          <-- Hands-On Challenges & Automated Tests
│   ├── module_02_variables_data_types/    <-- Module 2: Core Concepts: Variables & Data Types
│   ├── module_03_numeric/                 <-- Module 3: Numeric in Python
│   └── module_04_strings/                 <-- Module 4: String Manipulation
│
├── day-2/                                 <-- SECTION 2: Control Flow, Data Structures & Functions
│   ├── DAY_02_OVERVIEW.md
│   ├── module_05_conditionals_flow/       <-- Module 5: Conditional Logic and Flow Control
│   ├── module_06_data_structures/         <-- Module 6: Data Structures in Python
│   └── module_07_loops_functions/         <-- Module 7: Loops and Functions
│
└── day-3/                                 <-- SECTION 3: Systems, Advanced Processing & Modern Python
    ├── DAY_03_OVERVIEW.md
    ├── module_08_external_libraries_recursion/ <-- Module 8: External Libraries & Recursion
    ├── module_09_advanced_processing_techniques/ <-- Module 9: Advanced Processing (OCR, ctypes, Scraping)
    ├── module_10_os_file_handling/             <-- Module 10: OS Utilities & File Handling
    └── module_11_modern_python_features/       <-- Module 11: Python 3.10 & 3.11 New Features
```

---

## 🎯 Syllabus at a Glance

### [Day 1: Foundations of Python Programming](day-1/DAY_01_OVERVIEW.md)
* **[Module 1: Introduction to Python](day-1/module_01_intro/README.md)**: Logic and Algorithm Basics, IPO Architecture, Environment Setup (`venv`, `pip`), IDEs (IDLE, Notebooks, Google Colab, VS Code).
* **[Module 2: Core Concepts: Variables and Data Types](day-1/module_02_variables_data_types/README.md)**: Variables as Object References, Dynamic Typing, PEP 8 Naming, Primitive Types, Type Casting, Truthy/Falsy rules.
* **[Module 3: Numeric in Python](day-1/module_03_numeric/README.md)**: Integers, IEEE 754 Floats, Division (`/`, `//`, `%`), `math` module, High-Precision `decimal.Decimal`, Financial Loan & EMI calculation.
* **[Module 4: String Manipulation](day-1/module_04_strings/README.md)**: Sequence Slicing (`[start:stop:step]`), String Methods, F-Strings, Masking PII, URL Slugifier Project.

---

### [Day 2: Control Flow, Data Structures, and Modularity](day-2/DAY_02_OVERVIEW.md)
* **[Module 5: Conditional Logic and Flow Control](day-2/module_05_conditionals_flow/README.md)**: Booleans, Equality (`==`) vs Identity (`is`), Guard Clauses, Short-Circuiting (`and`/`or`), Tiered Discounts & RBAC access.
* **[Module 6: Data Structures in Python](day-2/module_06_data_structures/README.md)**: Lists (Dynamic Arrays) and Dictionaries (Hash Maps), Deep vs Shallow Copies (`copy.deepcopy`), Sorting with Lambdas, Inventory Management Project.
* **[Module 7: Loops and Functions](day-2/module_07_loops_functions/README.md)**: `for`, `while`, `enumerate`, `zip`, Loop-Else constructs, Pure Functions, LEGB Variable Scope, `*args` and `**kwargs`, List/Dict/Set Comprehensions.

---

### [Day 3: Advanced Techniques, Files, OS & Modern Python](day-3/DAY_03_OVERVIEW.md)
* **[Module 8: Practical Application & External Libraries](day-3/module_08_external_libraries_recursion/README.md)**: Recursion Trees, Data Stream Serialization (JSON, Base64), HTTP REST API Acquisition, Historical Stock Trend & Moving Averages.
* **[Module 9: Advanced Processing Techniques](day-3/module_09_advanced_processing_techniques/README.md)**: Optical Character Recognition (OCR), Calling Compiled C Libraries via `ctypes`, Advanced F-Strings, Web Scraping, Robust Exception Hierarchies.
* **[Module 10: OS Utilities and File Handling](day-3/module_10_os_file_handling/README.md)**: Cross-Platform Paths with `pathlib.Path`, Context Managers (`with open`), Structured CSV (`DictReader`/`DictWriter`) & JSON, Automated File Organizer Script.
* **[Module 11: New Features in Python 3.10 and 3.11](day-3/module_11_modern_python_features/README.md)**: Structural Pattern Matching (`match-case`), Faster CPython Optimizations, Parallel I/O via `concurrent.futures.ThreadPoolExecutor`.

---

## 🚀 How to Run the Code

### 1. Instructor Live Demonstrations
To execute any teaching demonstration script:
```bash
python day-1/module_01_intro/teaching_code.py
python day-2/module_06_data_structures/teaching_code.py
python day-3/module_11_modern_python_features/teaching_code.py
```

### 2. Student Practice Exercises & Automated Testing
Each module contains interactive student exercises with automated test assertions:
```bash
python day-1/module_01_intro/practice_exercises.py
python day-2/module_05_conditionals_flow/practice_exercises.py
python day-3/module_10_os_file_handling/practice_exercises.py
```
If all exercises pass, the suite displays:
```text
All Module X exercises passed successfully! Outstanding work!
```

