<div align="center">

# 🧠 Logic Box

### An interactive Python CLI for pattern generation and number analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=flat)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat)

</div>

---

## 📖 About

**Logic Box** is an interactive Python CLI tool that combines two powerful modules: a **pattern generator** that renders ASCII art shapes in the terminal, and a **number analyzer** that performs range-based computations. Built to practice Python 3.10+ `match/case` statements, nested loops, and input validation — all in a single clean menu-driven interface.

---

## 🗂️ Modules

### 🔷 Pattern Generator
Renders ASCII star patterns with a custom row count.

| Option | Pattern |
|--------|---------|
| 1 | Right Angle Triangle |
| 2 | Left Angle Triangle |
| 3 | Star Pyramid |
| 4 | Exit pattern menu |

### 🔢 Number Analyzer
Performs range-based analysis on a user-defined number range.

| Option | Analysis |
|--------|----------|
| 1 | Odd and Even classifier |
| 2 | Range sum calculator |
| 3 | Exit analyzer menu |

---

## ✅ Requirements

- **Python 3.10 or above** — required for `match/case` syntax
- No third-party libraries — uses Python standard library only
- A terminal or command prompt

---

## 🚀 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/raj-jivani/logic-box.git

# 2. Navigate into the project folder
cd logic-box

# 3. Run the script
python logic-box.py
```

---

## ⚙️ How It Works

1. **Main menu** — A `while True` loop presents three options: Pattern Generator, Number Analyzer, or Exit
2. **Sub-menu selection** — Each module opens its own nested loop with further options, handled by `match/case`
3. **Input validation** — `isdigit()` checks all numeric inputs; range comparisons guard against invalid values
4. **Output** — Patterns are printed with nested `for` loops; analysis results are printed line by line with f-strings

---

## 🖥️ Sample Session

```
Welcome to the Pattern Generator and Number Analyzer
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 1

Select any pattern from below:
1. Right Angle Triangle Pattern
2. Left Angle Triangle Pattern
3. Star pyramid Pattern
4. Exit

Choose your Pattern: 1
Enter the number of rows for the pattern: 5

* 
* * 
* * * 
* * * * 
* * * * * 
```

---

## 📁 Project Structure

```
logic-box/
│
├── logic-box.py    # Main script — all logic lives here
└── README.md       # Project documentation
```

---

## 📚 Concepts Covered

- `while True` infinite loops with `break` to exit
- `match/case` statements (Python 3.10+)
- Nested `for` loops for pattern rendering
- User input handling via `input()`
- Input validation with `isdigit()` and range checks
- Type casting (`int()`, `float()`)
- Arithmetic operations and modulo (`%`) for odd/even detection
- F-strings for formatted output

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ as a Python logic-building project &nbsp;·&nbsp; © 2026 raj-jivani

</div>
