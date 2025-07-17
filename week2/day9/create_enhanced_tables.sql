
-- Create Department table
CREATE TABLE IF NOT EXISTS department (
    department_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- Create Country table
CREATE TABLE IF NOT EXISTS country (
    country_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- Create Employee table
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary NUMERIC,
    department_id INTEGER REFERENCES department(department_id),
    country_id INTEGER REFERENCES country(country_id)
);

-- Create Performance table
CREATE TABLE IF NOT EXISTS performance (
    employee_id INTEGER PRIMARY KEY REFERENCES employee(id),
    review_score NUMERIC,
    tenure_years INTEGER,
    seniority TEXT
);
