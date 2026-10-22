# Upwork Profile — Optimized Draft

> Draft copy for an Upwork profile. Written in English because most Upwork clients
> post in English. Everything here is based on projects in this repository.
> Items marked **[CONFIRM]** must be checked by you before publishing.

---

## 1. Positioning

**Core message:** entry-level cybersecurity analyst who delivers small, clearly
documented security deliverables (log reviews, phishing analysis, policies, risk
assessments, Python automation), using AI tools to speed up the work and
human review to make sure it is correct.

**Target clients:** small and mid-sized businesses without a full security team,
startups that need a security baseline, and agencies that need security write-ups
or small scripts.

**Avoid bidding on:** live penetration testing of systems you do not own,
24/7 monitoring, compliance certification work, and anything that requires
production access you have not been trained on.

---

## 2. Profile Title (headline)

```
Cybersecurity Analyst – Log Analysis, IR & Python Automation
```

Alternative (if you want to lead with AI):

```
Cybersecurity Analyst | AI-Assisted Log Triage, Policies & Python Automation
```

---

## 3. Overview

```
I help small businesses and growing teams understand and reduce their security
risk with clear, practical work: log and alert reviews, phishing email analysis,
risk assessments, incident write-ups, security policy drafts, and small Python
scripts that automate repetitive checks.

I'm a cybersecurity analyst with hands-on training from the Google Cybersecurity
Professional Certificate [CONFIRM: add Security+ here only if you hold it] and a
portfolio of completed projects:

- Incident response write-up for a Denial-of-Service attack, following the NIST
  Cybersecurity Framework from detection through lessons learned
- Internal IT audit of a small business: assets, controls, and compliance gaps
- SQL investigation of login attempts and outdated devices in a MariaDB environment
- Python tools for log parsing, IPv4 validation, and allow-list management
- Linux security: file permissions, log investigation, user management, hardening
- Phishing investigation covering email headers and URL analysis
- Threat model for a web application with prioritized mitigations

How I work with AI: I use AI tools to speed up log triage, first drafts of
reports and documentation, and script scaffolding. Every finding is checked
by me against the source data before it reaches you, and each recommendation
comes with its reasoning so your team can act on it.

What you get: a clear written deliverable, source files or scripts when relevant,
and a short walkthrough if you want one.

Good fit for:
- Phishing and suspicious email analysis reports
- Log review and alert summaries
- Security policy and documentation drafts (aligned to NIST CSF)
- Risk assessments and threat models for web applications
- Python scripts for repetitive security tasks
- SQL queries for security reporting

Not a fit: live penetration testing on systems I am not authorized to test,
or round-the-clock monitoring.

Time zone: [CONFIRM: Costa Rica, CST — say you overlap with US Central hours]
```

---

## 4. Skills (select these 15 on Upwork)

1. Cybersecurity
2. Security Analysis
3. Incident Response
4. Log Analysis
5. Risk Assessment
6. Threat Modeling
7. Phishing Analysis
8. Python
9. SQL
10. Linux
11. Network Security
12. Security Policy Writing
13. Technical Writing
14. Data Analysis
15. Wireshark

> Upwork lets you take Skill Assessments. Take the ones that match your core
> skills (Python, SQL, Linux) to add a verified badge.

---

## 5. Services to Offer / Bid On

| # | Service | What the client gets | Pricing model to start |
|---|---------|---------------------|------------------------|
| 1 | Phishing email analysis | Written report: headers, URLs, indicators, verdict, recommended action | Fixed price per batch |
| 2 | Log review & alert summary | Findings report from CSV/text logs with prioritized issues | Fixed price per log set |
| 3 | Python security automation | Small, commented script with a README and usage example | Fixed price per script |
| 4 | Security policy drafts | Password, acceptable use, or incident response policy, NIST CSF-aligned, editable | Fixed price per policy |
| 5 | Small-business risk assessment | Asset list, threats, risk ratings, prioritized mitigations | Fixed price, or hourly for scope discovery |
| 6 | Web app threat model | Scope, assets, threats, mitigations, summary | Fixed price |
| 7 | SQL security reporting | Queries and a short explanation of what they show | Hourly |

**Starting rates (verify against comparable profiles in your category before you set them):**
- Hourly: about $20–30/hr for analysis and writing work
- Fixed price: start small ($50–150) for a single script, report, or policy to build reviews

---

## 6. Portfolio Entries

Use each folder in this repo as a portfolio item. Label lab work honestly; clients
respect that more than inflated claims.

**1. Incident Response: Denial-of-Service Attack**
Type: Case study (guided lab scenario)
Description: Documented the response to a simulated ICMP flood against an internal
network, using the NIST Cybersecurity Framework. Covered detection, containment,
mitigation, restoration, and lessons learned.
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/01-Incident-Response

**2. Phishing Investigation**
Type: Analysis report (guided lab scenario)
Description: Analyzed a suspicious email through its headers and URLs and wrote up the findings and recommended actions.
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/01b-Incident-Response-Phishing

**3. IT Security Audit: Botium Toys**
Type: Audit report (guided lab scenario)
Description: Reviewed a small business's assets, controls, and compliance gaps, and prioritized the controls to implement.
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/02-Risk-Assessment

**4. SQL Security Investigation**
Type: Data analysis (MariaDB)
Description: Used SELECT, WHERE, ORDER BY, and JOINs to find outdated devices and unusual login patterns, without modifying the database.
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/05-SQL-Analysis

**5. Linux Security: Permissions, Logs, and Users**
Type: Hands-on lab write-up
Description: Documented file permission hardening, log investigation, package management, and user management with the commands used and the evidence.
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/04-Linux-Security

**6. Python Security Automation**
Type: Code samples
Description: Four small scripts: log IP extraction, IPv4 validation, allow-list management, and file automation, each with its own README.
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/07-Python-Automation

**7. Threat Modeling: Web Application**
Type: Threat model
Description: Defined scope and assets, identified phishing, unauthorized access, and DoS threats, rated risk, and proposed mitigations (MFA, awareness training, traffic filtering).
Link: https://github.com/dawaroo/cybersecurity-portfolio/tree/main/06-Threat-Modeling

---

## 7. Cover Letter Template

Keep it under 120 words. Reply to the client's specific problem first.

```
Hi [Client name],

Your post mentions [specific problem]. I can help with that. [One sentence on
what you would deliver, e.g., "I would review your authentication logs and
deliver a prioritized findings report with recommended actions."]

Relevant work from my portfolio: [one matching portfolio item, with link].

Before I start, I would confirm [one scope question, e.g., the log format and
time range you want reviewed]. I can deliver a first version within [timeframe].

Best,
Daniel
```

---

## 8. Before You Publish: Checklist

- [ ] **Confirm Security+.** The root README says you are certified (SY0-701); the
      professional profile does not mention it. Use one version everywhere, and
      only claim certifications you hold.
- [ ] **Change "pursuing a junior role" language.** The Upwork profile should read
      as a freelancer offering services, not a job seeker.
- [ ] **Update `08-Professional-Profile/README.md`** to match this draft so the
      GitHub and Upwork stories agree.
- [ ] **Add a short intro video** (60–90 seconds) and a clear profile photo.
- [ ] **Set your time zone and availability** (hours per week).
- [ ] **Take the Upwork Skill Assessments** for Python, SQL, and Linux if available.
- [ ] **Be ready to explain every script line by line.** Some scripts are basic, for
      example `07-Python-Automation/01-log-analysis/log_analysis.py` hardcodes the
      file name `login.txt`. A client may ask about this. Be prepared to say it is a
      learning project and how you would generalize it.
- [ ] **Start with 3–5 small jobs** to build reviews before bidding on larger work.
- [ ] **Use AI, then verify.** Clients will check your output. Never submit AI
      output you have not checked against the source data.

---

## 9. Next Skills to Add (AI + Security, when you're ready)

These would strengthen the profile, but do not list them until you have a
project to show:

- **OWASP Top 10 for LLM Applications:** a short write-up reviewing an AI chatbot
  for prompt injection, data leakage, and excessive permissions. Good fit for
  businesses that are adding AI features.
- **Python + LLM API project:** a script that summarizes alerts or log entries
  into a structured report, with human review built in. This is a strong portfolio
  piece for AI-assisted SOC work.
- **A second log dataset:** rerun your log analysis on a different log source
  (for example, web server logs) and document the differences.
