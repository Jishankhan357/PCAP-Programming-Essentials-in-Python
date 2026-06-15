# 🔍 API-Driven GitHub Profile Analyzer

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Category](https://img.shields.io/badge/Category-API_Integration-success)

## 📌 Overview

A powerful Command Line Interface (CLI) application that interacts directly with the **GitHub REST API (v3)**. It fetches real-time developer statistics, parses complex JSON responses, and generates a clean, readable dashboard directly in the terminal.

## ✨ Technical Features

- **HTTP Protocol Handling:** Utilizes Python's built-in `urllib` to send secure GET requests and handle API rate-limiting gracefully.
- **JSON Data Parsing:** Extracts specific data points from massive API payloads (nested dictionaries).
- **Advanced Sorting:** Uses Python `lambda` functions to sort through 100+ repositories and extract the Top 3 based on Stargazer count.
- **Dynamic Formatting:** Converts ISO 8601 timestamps (e.g., `2017-08-04T00:00:00Z`) into user-friendly date formats using the `datetime` module.

## 🚀 How to Run

1. Open your terminal and navigate to this directory.
2. Execute the script: `python main.py` (or `py main.py` on Windows).
3. Enter any valid GitHub username when prompted.
4. View the generated live profile dashboard!
