# SQL Security Analysis Project

## Description
This project demonstrates the use of SQL to investigate employee devices and login activity within an organization. The analysis focuses on retrieving, filtering, and correlating data from multiple database tables to identify outdated systems, unusual login behavior, and potential security risks.

The investigation was conducted using a MariaDB environment compatible with MySQL syntax and reflects common tasks performed by security analysts when reviewing system access and authentication activity.

---

## Investigation Objectives
The objectives of this investigation were to:

- Identify employee devices that require operating system updates
- Review login attempts for unusual or suspicious activity
- Analyze login behavior across different locations and time periods
- Correlate employee and login data using SQL joins

---

## Environment Overview
- **Database system:** MariaDB (MySQL-compatible)
- **Database used:** organization
- **Tables analyzed:**
  - machines
  - employees
  - log_in_attempts
- **Access level:** Read-only (no database modifications performed)

---

## Analysis Approach
SQL queries were used to retrieve and analyze security-relevant data from multiple tables. Filtering techniques helped isolate specific conditions such as outdated operating systems or unusual login attempts. Joins were applied to correlate employee information with device and authentication data, enabling a broader view of potential security risks.

The analysis focused on identifying patterns and anomalies that could indicate misconfigurations, weak access controls, or suspicious behavior.

---

## Skills Demonstrated
- SQL querying using `SELECT` and `FROM`
- Data filtering using `WHERE`, `LIKE`, `AND`, `OR`, and `NOT`
- Sorting results using `ORDER BY`
- Correlating data using `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN`
- Security-focused data analysis and investigation techniques

---

## Security Relevance
SQL-based investigations are a critical skill for security analysts. The ability to efficiently retrieve and analyze data from databases supports incident investigations, access reviews, compliance checks, and threat detection.

This project demonstrates how structured queries can provide meaningful security insights without requiring administrative access, aligning with real-world SOC workflows.

---

## Lab Context
This project was developed using a guided lab environment as part of the **Google Cybersecurity Professional Certificate**. The analysis, queries, and documentation were independently completed to demonstrate understanding of security-focused SQL investigations.
