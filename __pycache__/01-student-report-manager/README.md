# 🎓 PyScholar: CLI Student Management System

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

**PyScholar** is a robust, menu-driven Command Line Interface (CLI) application built entirely in Python. It serves as a comprehensive Student Report Card and Management System.

This project was developed to practically implement core programming concepts, specifically **File Handling (Binary Serialization)**, **Modular Programming**, and **CRUD Operations** as part of my journey completing the _PCAP: Programming Essentials in Python_ certification.

## ✨ Key Features

- **Create (C):** Add new student records including their roll number, name, and subject-wise marks.
- **Read (R):** View individual student report cards or generate a tabular format result for the entire class.
- **Update (U):** Search and dynamically edit existing student records and marks.
- **Delete (D):** Safely remove specific student records from the database.
- **Persistent Storage:** Utilizes Python's `pickle` module to serialize data into a `.dat` binary file, ensuring no data loss between sessions.
- **Interactive UI:** Clean, nested menu-driven console interface for smooth navigation between 'Admin' and 'Report' modes.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Core Libraries:**
  - `pickle` (for object serialization/deserialization)
  - `os` (for file manipulation)
  - `time` (for UX delays)

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jishankhan357/student-report-manager.git
   ```
