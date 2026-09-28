# Design Diagrams

## Use Case Diagram
```text
Student
  |-- Create Task
  |-- View Tasks
  |-- Edit Task
  |-- Delete Task
  |-- Mark Complete
  `-- Filter Tasks
```

## Workflow
```text
Start → Open App → Add/Select Task → Process Action
      → Save in LocalStorage → Refresh Dashboard → End
```

## Component Diagram
```text
+------------------+
|     Web UI       |
| index.html/css   |
+--------+---------+
         |
         v
+------------------+
| JavaScript App   |
| CRUD + Filtering |
+--------+---------+
         |
         v
+------------------+
|   LocalStorage   |
+------------------+
```

## Sequence
```text
Student → UI → JavaScript → LocalStorage
Student ← UI ← JavaScript ← LocalStorage
```

## ER-style Storage Design
```text
TASK
----------------
id (Primary Key)
title
subject
deadline
priority
completed
```
