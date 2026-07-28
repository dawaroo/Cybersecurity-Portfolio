# Step 1: Ask the Question

## Question
Which URL or website characteristics best predict whether a site is phishing or legitimate?

## Benefit
A SOC or security analyst benefits from identifying which technical indicators are most reliable for prioritizing phishing alerts and automating detection rules, reducing triage time and false positives.

## Analysis Type
**Diagnostic** — the goal is to understand *why* certain sites are classified as phishing (which variables correlate with that label), rather than just describing how many exist.

## Initial Hypothesis
Phishing sites are expected to show longer URLs, more special characters, absence of HTTPS, use of IP addresses instead of domains, and more subdomains compared to legitimate sites.

---

# Step 2: Determine the Necessary Data

## Identified Data Elements
- URL length
- Presence of special characters (@, -, %, =, ~, etc.)
- Use of IP address instead of domain name
- HTTPS usage
- Number of subdomains (dot count in the domain)
- Suspicious words within the URL
- Digit count in the URL
- URL entropy (character randomness)

## Sources Investigated
- Kaggle — "Phishing URLs Dataset with Extracted Features" (victusadi)
- Kaggle — "Phishing Websites Dataset" (based on the UCI Machine Learning Repository)

---

# Reflection Questions

**1. Why is it important to identify the question to be answered by the analysis before starting the project?**

Because the question determines what data needs to be collected, what type of analysis to apply, and what tools to use. Without a clear question, there's a risk of collecting irrelevant data or wasting time analyzing information that doesn't address a real need. In security, this is equivalent to investigating without knowing what you're looking for.

**2. Name some open data sources for the analysis found while searching for your data elements.**

Kaggle ("Phishing URLs Dataset with Extracted Features" and "Phishing Websites Dataset" datasets), both based on academic research on phishing detection (UCI Machine Learning Repository).
