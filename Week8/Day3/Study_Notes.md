# Week 8 Day 3 — Study Notes

## Core idea

A Django app should not rely on normal Python variables for important data.

Python memory is temporary. A database gives the application **persistent, shared, structured data**.

```text
Browser → Django View → Model / ORM → RDBMS → Database
```

The ORM makes database work easier, but the database still exists underneath it.

---

## 1. Persistence

### Temporary memory

```python
students = ["Ali", "Sara"]
```

This works only while the Python process is running.

Problems:
- restarting the server clears the data
- different users may not share the same state
- searching and updating becomes messy as data grows

### Persistent storage

A database keeps records after:
- a request finishes
- the server restarts
- the application crashes and starts again

### Remember

> Persistence = data survives beyond the code/request that created it.

---

## 2. Database vs DBMS vs RDBMS

### Database

The actual stored data.

Examples:
- students
- courses
- orders
- support tickets

### DBMS

**Database Management System**

Software that manages databases.

Examples:
- PostgreSQL
- MySQL
- SQLite

It handles:
- reading data
- writing data
- access
- rules
- concurrent changes

### RDBMS

**Relational Database Management System**

A DBMS that organizes related data into **tables** and connects them using keys.

Examples:
- PostgreSQL
- MySQL
- SQLite

### Easy difference

```text
Database = the data
DBMS = software managing the data
RDBMS = DBMS using relational tables
```

Common mistake: saying PostgreSQL is the database itself.

More accurately:

> PostgreSQL is the RDBMS that manages the database.

---

## 3. Relational structure

Relational databases mainly use:

```text
Table
 ├── Rows
 └── Columns
```

Example:

```text
STUDENTS
-------------------------
student_id | name | email
1          | Ali  | ...
2          | Sara | ...
```

A row represents one record.

A column represents one attribute.

---

## 4. Primary keys and foreign keys

### Primary Key — PK

Uniquely identifies a row.

Example:

```text
student_id = 15
```

No two students should have the same primary key.

### Foreign Key — FK

Points to a record in another table.

Example:

```text
ENROLLMENTS
-----------------------------
id | student_id | course_id
```

`student_id` refers to a student.

`course_id` refers to a course.

### Why Enrollment gets its own table

A student can join many courses.

A course can have many students.

So we store the relationship separately:

```text
STUDENT 1 ---- many ENROLLMENTS many ---- 1 COURSE
```

This avoids repeatedly storing the student's name and course title.

---

## 5. Constraints

Constraints are rules enforced by the database.

### PRIMARY KEY

Each row must have a unique identity.

### FOREIGN KEY

Referenced data must exist.

Bad example:

```text
student_id = 999
```

if student 999 does not exist.

### UNIQUE

A value cannot appear twice.

Example:

```text
email must be unique
```

### NOT NULL

A required value cannot be empty.

### CHECK

A value must satisfy a condition.

Example:

```text
capacity >= 0
```

### Why constraints matter

Do not rely only on Python validation.

The database should also protect its own data.

---

## 6. Data integrity

Integrity means the stored data stays valid and consistent.

### Entity integrity

Each row has a valid unique identity.

Broken example:

```text
Two students have the same primary key.
```

### Referential integrity

Foreign keys point to existing records.

Broken example:

```text
Enrollment points to a deleted student.
```

### Domain integrity

Values follow allowed rules and types.

Broken example:

```text
course capacity = -10
```

---

## 7. CRUD and SQL

The main database operations are CRUD.

| CRUD | Meaning | SQL |
|---|---|---|
| Create | Add data | `INSERT` |
| Read | Retrieve data | `SELECT` |
| Update | Change data | `UPDATE` |
| Delete | Remove data | `DELETE` |

Example SQL:

```sql
SELECT * FROM students;
```

With Django ORM you may write Python instead:

```python
Student.objects.all()
```

Conceptually Django translates this into SQL for the database.

```text
Django ORM → SQL → RDBMS
```

---

## 8. Transactions and ACID

A transaction is a group of database changes treated as one controlled operation.

### ACID

#### Atomicity
Everything succeeds together, or everything is cancelled.

```text
all or nothing
```

#### Consistency
The database must still follow its rules after the transaction.

#### Isolation
Simultaneous transactions should not corrupt each other.

#### Durability
Once committed, data survives crashes and restarts.

### Good example

Only one seat remains.

Student A and Student B click **Enroll** at almost the same time.

Without proper transaction handling:

```text
Both may think they got the final seat.
```

With the RDBMS:

```text
One succeeds.
The conflicting request is rejected or retried.
```

This is why concurrency control matters.

---

## 9. Files vs spreadsheets vs RDBMS

### Text / JSON file

Good for:
- simple data
- configuration
- small local tasks

Weak for:
- many users writing
- relationships
- complex searching
- concurrency

### Spreadsheet

Better structure than a plain file, but still limited for large applications.

### RDBMS

Best suited when the application needs:
- shared data
- relationships
- strong rules
- safe concurrent changes
- complex queries and joins

---

## 10. Relational vs non-relational

### Relational

Uses tables, schemas, keys, relationships, and joins.

Examples:

```text
PostgreSQL
MySQL
SQLite
```

### Non-relational

May use:
- documents
- key-value pairs
- graphs
- wide-column storage

Examples:

```text
MongoDB
Redis
Neo4j
```

Important:

> Non-relational is not automatically better or worse.

The application's requirements decide which model fits.

---

## 11. Where Django fits

Django models describe data using Python.

Example idea:

```python
class Student:
    name
    email
```

Later, Django models become database tables through migrations.

The flow is roughly:

```text
User
 ↓
View
 ↓
Model / ORM
 ↓
SQL
 ↓
RDBMS
 ↓
Stored database records
```

Common mistake:

> Thinking Django ORM replaces the database.

It does not.

It is an easier Python interface for working with the database.

---

# Common mistakes to avoid

- Confusing a **database** with a **DBMS**
- Thinking Python variables are persistent
- Forgetting that foreign keys must reference existing rows
- Storing repeated data instead of using relationships
- Depending only on application validation instead of database constraints
- Thinking ORM means SQL or the RDBMS no longer matters
- Forgetting concurrency problems when two users change the same data

---

# Final Memory Sheet

```text
Persistence
= data survives requests and restarts

Database
= stored data

DBMS
= software managing databases

RDBMS
= DBMS using related tables

PK
= uniquely identifies a row

FK
= links to another table

Constraints
= PK, FK, UNIQUE, NOT NULL, CHECK

Integrity
= data remains valid and consistent

CRUD
Create → INSERT
Read   → SELECT
Update → UPDATE
Delete → DELETE

ACID
A = Atomicity
C = Consistency
I = Isolation
D = Durability

Django ORM
Python → ORM → SQL → RDBMS

Key idea
The ORM simplifies database access.
It does not replace the database.
```
