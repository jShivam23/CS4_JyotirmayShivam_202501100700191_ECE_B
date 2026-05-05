Problem Statement:
Task 1: Basic File Reading
Task 2: Log Classification
Task 3: Write Filtered Files
Task 4: Search Feature

Output:
--- Task 1: Basic File Reading ---
Total number of lines: 10

First 2 lines:
2026-04-01 10:15:32 INFO User login success user_id=101
2026-04-01 10:17:45 ERROR Database connection failed

Last 2 lines:
2026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully

Using readline() to read the first line:
2026-04-01 10:15:32 INFO User login success user_id=101

Using read() to print the first 50 characters:
2026-04-01 10:15:32 INFO User login success user_i

--- Task 2: Log Classification ---
Log Keyword Counts: {'INFO': 5, 'WARNING': 2, 'ERROR': 3}

--- Task 3: Write Filtered Files ---
Filtered files created: info_logs.txt, warning_logs.txt, error_logs.txt

--- Task 4: Search Feature ---
Enter keyword to search (e.g., ERROR, INFO, WARNING)
