# Python SQL Assignments

This repository contains a collection of my smaller assignments and practice projects across **Python and SQL**. Each project is designed to strengthen my understanding of programming, data analysis, and database concepts by applying them to targeted problems. While these projects are smaller in scope than my standalone portfolio work, they highlight core skills in computation, logic, and data handling.

---

## 📂 Project List

### 1. **Final Grade Calculator** (`Final_Grade_Calculator.py`)
This project implements a Python-based grade calculator that allows users to input exam, homework, research, and final project scores. Each component is weighted, and the program validates input ranges to ensure accuracy. It then calculates the weighted average and assigns the final letter grade.  

- **Key Features**: Input validation, weighted averages, modular functions for reusability.  
- **Skills Demonstrated**: Python programming, control flow, user input handling, functional decomposition.  
- **Practical Use**: Can be adapted into a simple grading assistant tool for students and instructors.

## 🖥️ Sample Output
```bash
Enter exam score: 85
Enter homework score: 90
Enter project score: 95

Final Score: 90.5
Final Grade: A
```

---

### 2. **Retirement Savings Growth Calculator** (`Retirement_Savings_Growth_Calculator.py`)
A financial planning tool written in Python that models how retirement savings grow year over year. Users can set annual contributions, interest rates, and retirement timelines. The program calculates compound interest and outputs a detailed year-by-year growth table along with the final savings total.  

- **Key Features**: Compound growth calculations, dynamic user input, tabular display of results.  
- **Skills Demonstrated**: Loops, mathematical modeling, formatted output for financial projections.  
- **Practical Use**: A helpful starting point for individuals to estimate long-term savings goals and understand the power of compound interest.  

## 🖥️ Sample Output
```bash
Enter annual savings amount: 5000
Enter annual interest rate (%): 6
Enter number of years until retirement: 5

Year 1: $5,300.00
Year 2: $10,918.00
Year 3: $16,873.08
Year 4: $23,185.46
Year 5: $29,877.59

Final Retirement Savings: $29,877.59
```

---

### 3. **ETL & Warehouse SQL** (`ETL & Warehouse SQL.txt`)
This project simulates the design and implementation of a small-scale **data warehouse**. It consolidates data from multiple sources (`rider` and `riders_acquired` tables), applies transformations via SQL views, and integrates them into a clean warehouse schema (`rider_dw`). Stored procedures handle inserts, updates, and merges to maintain consistency.  

- **Key Features**: Schema creation, views for data standardization, ETL procedures (insert, merge, and full upsert).  
- **Skills Demonstrated**: SQL (DDL & DML), ETL concepts, database normalization, procedural SQL.  
- **Practical Use**: Illustrates how companies integrate data from acquisitions or multiple systems into one warehouse for analytics and reporting.

**Sample Warehouse Schema**:
```sql
CREATE TABLE rider_dw (
    rider_id NUMBER NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone CHAR(12) NOT NULL,
    address VARCHAR(50) NOT NULL,
    zip CHAR(5) NOT NULL,
    data_source CHAR(4) NOT NULL,
    CONSTRAINT rider_dw_pk PRIMARY KEY (rider_id, data_source)
);
```

---

### 4. **Ride Fares & Payments** (`Ride Fares & Payments.txt`)
A set of SQL queries designed to analyze and manage data for a ride-hailing platform. The queries handle tasks such as formatting dates, calculating discounts, masking sensitive payment data, and ranking drivers by performance. This project demonstrates how SQL can be applied to solve practical business problems in transportation and payments.  

- **Key Features**:  
  - Date and time formatting for ride records.  
  - Discount application and recalculation of fares.  
  - Payment card masking for data security.  
  - Ranking drivers with SQL window functions.  
- **Skills Demonstrated**: SQL string manipulation, joins, conditional logic, PII protection, window functions (`DENSE_RANK`).  
- **Practical Use**: Represents the type of backend SQL logic required in real ride-hailing or payment transaction systems.  

**Sample Query**:
```sql
CREATE TABLE rider_dw (
    rider_id NUMBER NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone CHAR(12) NOT NULL,
    address VARCHAR(50) NOT NULL,
    zip CHAR(5) NOT NULL,
    data_source CHAR(4) NOT NULL,
    CONSTRAINT rider_dw_pk PRIMARY KEY (rider_id, data_source)
);
```

| Rider Name  | Card Type | Redacted Card Number   |
|-------------|-----------|------------------------|
| John Smith  | VISA      | `****-****-****-1234`  |
| Priya Patel | MSTR      | `****-****-****-5678`  |

---

## 🔧 Tools & Technologies
- **Languages**: Python, SQL  
- **Libraries**: None (implemented using core Python and SQL functionality)  
- **Tools**: Jupyter Notebook, VS Code, Oracle/ANSI SQL  

---

## 📬 Contact
Created by **Pranit Yadav**  
- 📧 Email: [pranit.ydv@gmail.com]  
- 💼 [LinkedIn](https://www.linkedin.com/in/pranityadav19/)  
- 🐙 [GitHub](https://github.com/pranityadav19)  
