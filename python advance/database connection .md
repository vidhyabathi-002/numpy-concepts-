# DATABASE CONNECTION THEORY

## What is Database Connection?

A **database connection** is a communication link established between a Python application and a database. It allows your Python program to:

- Send queries to the database
- Retrieve and display data
- Insert, update, or delete records
- Manage database transactions

> **KEY POINT:** You must establish a connection before you can perform ANY database operation.

---



# MAIN FUNCTIONS :

1. ```plantuml
   @startuml

   start

   :Import sqlite3 module;
   note right
   Imports the SQLite library.
   Provides functions to
   connect and work with
   SQLite databases.
   end note

   :Create Database Connection;
   note right
   Creates a connection
   between Python and
   the database file.

   conn = sqlite3.connect("student.db")

   If the database does not
   exist, SQLite creates it.
   end note

   :Create Cursor;
   note right
   Cursor acts as a bridge
   between Python and the
   database.

   Used to execute SQL
   queries and fetch data.

   cursor = conn.cursor()
   end note

   :Execute SQL Query;
   note right
   Sends SQL commands
   to the database.

   Examples:
   CREATE TABLE
   INSERT
   SELECT
   UPDATE
   DELETE

   cursor.execute(...)
   end note

   :Fetch Results;
   note right
   Retrieves data returned
   by a SELECT query.

   fetchone() -> one row
   fetchmany() -> many rows
   fetchall() -> all rows
   end note

   :Commit Changes;
   note right
   Saves changes permanently
   to the database.

   Required after:
   INSERT
   UPDATE
   DELETE

   conn.commit()
   end note

   :Close Cursor;
   note right
   Releases resources used
   by the cursor object.

   cursor.close()
   end note

   :Close Connection;
   note right
   Terminates the connection
   with the database.

   Prevents memory leaks
   and frees resources.

   conn.close()
   end note

   stop

   @enduml
   ```

## Visual Flow of Database Connection

```
┌─────────────────┐
│   Python App    │
└────────┬────────┘
         │
         │ (Sends Connection Request)
         ▼
┌──────────────────────┐
│  Database Driver     │  ← Translates between Python & Database
│  (sqlite3, MySQLdb)  │
└────────┬─────────────┘
         │
         │ (Establishes Connection)
         ▼
┌──────────────────────┐
│  DATABASE SERVER     │
│  ├─ Tables           │
│  ├─ Records          │
│  └─ Data             │
└──────────────────────┘
```

---

## Connection Establishment Steps

```
Step 1: Import Driver
        ↓
Step 2: Provide Connection Details (Host, User, Password)
        ↓
Step 3: Create Connection Object
        ↓
Step 4: Create Cursor Object (to execute queries)
        ↓
Step 5: Execute SQL Queries
        ↓
Step 6: Commit/Rollback Changes
        ↓
Step 7: Close Connection
```

---

## Connection Lifecycle

```
┌─────────────┐
│ UNCONNECTED │  Initial state - No connection exists
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ CONNECTING  │  Establishing connection with database
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ CONNECTED   │  Active connection - Can execute queries
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ CLOSED      │  Connection terminated - Resources freed
└─────────────┘
```

---

## Connection Components Explained

| Component               | Description                               | Example                         |
| ----------------------- | ----------------------------------------- | ------------------------------- |
| **Driver**        | Software that connects Python to database | sqlite3, MySQL, PostgreSQL      |
| **Host**          | Server address where database is located  | localhost, 192.168.1.1          |
| **Port**          | Communication endpoint on the server      | 3306 (MySQL), 5432 (PostgreSQL) |
| **Username**      | Authentication credential                 | admin, root, user               |
| **Password**      | Secret authentication credential          | •••••••                  |
| **Database Name** | Specific database to access               | myapp_db, students_db           |

---

## What is a Cursor?

A **cursor** is an intermediary object that:

- Acts as a bridge between your Python code and the database
- Points to specific locations in the database
- Holds SQL queries before execution
- Retrieves and stores query results

```
Python Code
    │
    ▼
┌─────────────────┐
│  CURSOR OBJECT  │  ← Stores queries and results
├─────────────────┤
│ SQL Query: ...  │
│ Results: [...]  │
└────────┬────────┘
         │
         ▼
   DATABASE
```

---

## Transaction Concept

A **transaction** is a group of SQL operations that must succeed or fail together (All-or-Nothing principle).

### ACID Properties:

| Property              | Meaning                                      | Example                                                       |
| --------------------- | -------------------------------------------- | ------------------------------------------------------------- |
| **A**tomicity   | Either ALL operations succeed OR ALL fail    | Money transfer: debit & credit must both happen               |
| **C**onsistency | Database stays in a valid state              | No negative account balances                                  |
| **I**solation   | Transactions don't interfere with each other | User A's transaction doesn't see User B's uncommitted changes |
| **D**urability  | Once saved, changes are permanent            | Power failure won't lose committed data                       |

---

## Commit vs Rollback

**COMMIT USES :**         its a function which is used to save  all of the changes  in your data base

**SYNTAX:**  `VAR.COMMIT()`

**ROLLBACK  USES :**  Undo all changes since last commit

**SYNTAX:**   `VAR.ROLLBACK()`

```
TRANSACTION PROCESS:

Start Transaction
    │
    ├─ Query 1 ✓
    │
    ├─ Query 2 ✓
    │
    ├─ Query 3 ✗ (Error!)
    │
    ▼
┌──────────────────────────┐
│ DECISION POINT           │
├──────────────────────────┤
│ ✓ COMMIT                 │  ✗ ROLLBACK
│ (Save all changes)       │  (Undo all changes)
└──────────────────────────┘
```

| Operation          | Effect                             | Usage                          |
| ------------------ | ---------------------------------- | ------------------------------ |
| **COMMIT**   | Permanently saves all changes      | After successful operations    |
| **ROLLBACK** | Undo all changes since last commit | On error or validation failure |

---

## Connection Types at a Glance

### 1. **Local Connection** (File-based)

```
Python App → SQLite Database File (on same computer)
Fast, No network required
```

### 2. **Remote Connection** (Network-based)

```
Python App → Network → Database Server (remote computer)
Requires authentication, Slower due to network
```

### 3. **Connection Pooling**

```
Instead of:  App → New Connection → DB (Every time - Slow!)

Use:         App → Connection Pool → DB
             (Reuse existing connections - Fast!)
```

---

## Common Connection Errors & Solutions

| Error                           | Cause                       | Solution                        |
| ------------------------------- | --------------------------- | ------------------------------- |
| **Connection Refused**    | Database server not running | Start the database service      |
| **Authentication Failed** | Wrong username/password     | Verify credentials              |
| **Host Not Found**        | Invalid server address      | Check hostname/IP address       |
| **Timeout**               | Connection taking too long  | Check network, increase timeout |
| **Connection Lost**       | Network interrupted         | Implement retry logic           |

---

## Connection Resource Management

```
BAD PRACTICE:                 GOOD PRACTICE:
conn = connect()              conn = connect()
# Do operations               try:
# Forget to close!              # Do operations
                              finally:
                                 conn.close()
                              # Always closes!
```

### Why Close Connections?

- Frees up server resources
- Prevents connection exhaustion
- Releases memory on client side
- Maintains system performance

---

## Connection Isolation Levels (Simple Explanation)

```
┌─────────────────────────────────────────────────────────┐
│ ISOLATION LEVEL         │ ISOLATION │ PERFORMANCE       │
├─────────────────────────────────────────────────────────┤
│ Read Uncommitted        │ Lowest    │ Highest (Risky)   │
│ Read Committed          │ Medium    │ Balanced ✓        │
│ Repeatable Read         │ High      │ Lower             │
│ Serializable            │ Highest   │ Lowest (Safe)     │
└─────────────────────────────────────────────────────────┘

Choose based on your application needs!
```

---

## Summary

**Database Connection** = Communication Channel Between App & Database

**Why Needed?**

- Access stored data
- Perform operations
- Maintain data integrity

**Key Components:**

- Driver, Host, Port, Username, Password, Database Name

**Always Remember:**

1. ✓ Establish connection first
2. ✓ Create cursor for queries
3. ✓ Execute SQL operations
4. ✓ Commit changes
5. ✓ Close connection
