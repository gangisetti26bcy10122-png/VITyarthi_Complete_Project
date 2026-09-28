# Design Diagrams

## Use Case Diegram
```text
Student
  |-- Create Task
  |-- View Tasks
  |-- Edit Task
  |-- Delete Task
  |-- Mark Complete
  `-- Filter Tasks
```

## Workfllow
```text
Start → Open App → Add/Select Task → Process Action
      → Save in LocalStorage → Refresh Dashboard → End
```

## Component Diagruam
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

## Sequense
```text
Student → UI → JavaScript → LocalStorage
Student ← UI ← JavaScript ← LocalStorage
```

## ER-style Stortage Design
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
