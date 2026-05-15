# NORMALIZATION REPORT (3rd Normal Form)


---

## 1. Original Functional Dependencies

### Companies
company_id → company_name, industry, location, website, created_at, updated_at  
company_name → company_id (unique constraint)

### Jobs
job_id → company_id, title, salary_range, job_type, location, posted_date, created_at

### Applications
application_id → job_id, status, applied_date, created_at

### Interviews
interview_id → application_id, interview_type, interviewer_name, interview_date, notes, created_at

---

## 2. Anomaly Identification

### Applications Table
- `days_since_applied` was a **derived attribute**, causing:
  - Update anomaly (must recalc daily)
  - Insert anomaly (cannot compute without applied_date)
  - Violation of 3NF (non‑prime attribute depending on non‑key)

---

## 3. Decomposition Steps

### Removed:
days_since_applied INT

### Replaced with:
A computed Django property:


---

## 4. Final 3NF Schema

### Companies(company_id PK, company_name UNIQUE, industry, location, website, created_at, updated_at)

### Jobs(job_id PK, company_id FK, title, salary_range, job_type, location, posted_date, created_at)

### Applications(application_id PK, job_id FK, status, applied_date, created_at)

### Interviews(interview_id PK, application_id FK, interview_type, interviewer_name, interview_date, notes, created_at)

All tables now satisfy:
- 1NF (atomic values)
- 2NF (no partial dependencies)
- 3NF (no transitive dependencies)


