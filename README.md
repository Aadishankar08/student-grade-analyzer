# 🎓 Student Grade Analyzer

A Python-based command-line application to manage and analyze student grades across multiple subjects — built using Object-Oriented Programming and JSON file handling.

---

## 📋 Features

- ➕ Add multiple students with subject-wise marks
- ❌ Remove a student by name
- 📊 Display all students with their marks, average, and grade
- 🏆 Find the class topper
- 📈 Calculate the overall class average
- 🥇 Rank all students by average
- 💾 Auto-save and load data using JSON (data persists between sessions)

---

## 🏗️ Project Structure

```
student_grade_analyzer/
│
├── student_grade_analyzer.py   # Main program
└── students.json               # Auto-generated data file (after first save)
```

---

## 🚀 How to Run

Make sure Python 3 is installed, then:

```bash
python student_grade_analyzer.py
```

---

## 🖥️ Menu Options

```
--- Grade Analyzer ---
1. Add student
2. Remove student
3. Show all students
4. Top student
5. Class average
6. Rank students
7. Save and exit
```

---

## 📊 Sample Output

```
Enter name of the student: Aadi
Enter the number of subjects: 3
Enter subject 1 name: Math
Enter marks of Math: 92
Enter subject 2 name: Science
Enter marks of Science: 88
Enter subject 3 name: English
Enter marks of English: 85

name: Aadi
marks:
  Math: 92
  Science: 88
  English: 85
average: 88.33
grade: A

--- Student Rankings ---
Rank 1: Aadi — Average: 88.33 — Grade: A
```

---

## 🧠 Concepts Used

| Concept | Usage |
|---|---|
| OOP (Classes & Objects) | `Student` and `Classroom` classes |
| Instance Methods | `average()`, `grade()`, `display()` |
| File Handling | Save/load data with `json` module |
| Sorting with Lambda | `rank_students()` using `sorted()` |
| Exception Handling | `FileNotFoundError` on first run |

---

## 🎓 Grading Scale

| Grade | Average |
|---|---|
| A | 80 and above |
| B | 60 – 79 |
| C | 50 – 59 |
| D | 40 – 49 |
| F | Below 40 |

---

## 👤 Author

**Aadi**
B.Tech CSE (AI & Robotics) | Aspiring Space Tech Engineer
[GitHub Profile](https://github.com/yourusername)

---

## 📌 Status

✅ Complete — possible future additions: GUI interface, CSV export, subject-wise analytics.
