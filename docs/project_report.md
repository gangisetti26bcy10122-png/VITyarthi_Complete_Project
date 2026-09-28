# Project Report – VITyarthi Student Task Manager

## 1. Cover Page
**Project:** VITyarthi Student Task Manager  
**Type:** Web Application

## 2. Introduction
The application helps students organize academic tasks and track completion.

## 3. Problem Statement
Students may lose track of assignments, deadlines and completion status when information is stored in different places.

## 4. Functional Requirements
- Create task
- Update task
- Delete task
- Complete/uncomplete task
- Filter tasks
- Display dashboard statistics

## 5. Non-Functional Requirements
- Usability
- Performance
- Reliability
- Maintainability

## 6. System Architecture
Browser UI → JavaScript Application Logic → LocalStorage

## 7. Design Diagrams
See `docs/diagrams.md`.

## 8. Design Decisions
A browser-based solution was selected because it is simple to deploy and requires no server for the basic version.

## 9. Implementation Details
HTML provides structure, CSS provides responsive presentation, and JavaScript implements CRUD operations and LocalStorage persistence.

## 10. Results
The application displays tasks and dashboard counts and preserves data after page refresh.

## 11. Testing
Manual functional testing is provided in `tests/test_cases.md`.

## 12. Challenges
Designing CRUD operations and maintaining browser storage consistency.

## 13. Learnings
The project demonstrates modular JavaScript, DOM manipulation, validation and client-side persistence.

## 14. Future Enhancements
- Login system
- Cloud database
- Reminder notifications
- Calendar integration

## 15. References
MDN Web Docs concepts for HTML, CSS, JavaScript and Web Storage.
